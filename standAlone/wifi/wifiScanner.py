from scapy.all import * # needed for reading the packets
from threading import Thread # needed for multithreading
import pandas # used for pretty print to screen
import time # needed for sleep
import os # needed to run commands

import csv # needed for manufacturer lookup
import pickle # needed for data writing / reading

# Note, must run as root for wifi stuff

class WifiTarget:
    ''' Class that handles the wifi targets found by the sweeper '''

    def __init__(self, bssid, ssid, dBm, ch, crypto):
        ''' init method '''

        self.maxTimeout = 3

        self.bssid = bssid
        self.ssid = ssid
        self.dBm = dBm
        self.ch = ch
        self.crypto = crypto
        self.timeOut = self.maxTimeout

        # Key used for vendor lookup
        self.key = str(self.bssid).replace(':','').upper()[0:6]
        self.vendor = "Unknown"

    def setVendor(self, vendor):
        ''' Updates the vendor '''

        self.vendor = vendor

    def updateTimeout(self, ch):
        ''' updates the timeout of the target object, \n ch: the channel currently being scanned \n Return True when timeout hits zero '''

        # if the channel being scanned is the channel the target should be on
        if ch == self.ch :
            self.timeOut = self.timeOut - 1
            
            # if the timout has been reduced to zero
            if self.timeOut <= 0 : 
                return True
            else: 
                return False
        else:
            return False

    def matchTarget(self, other):
        ''' Comapares the BSSID of two objects to see if they match '''

        if self.bssid == other.bssid : 
            
            self.ch = other.ch
            self.crypto = other.crypto
            self.ssid = other.ssid
            self.dBm = other.dBm

            self.timeOut = self.maxTimeout

            return True

        else:
            return False

class WifiScanner:
    ''' Class that handles independently searching wifi frequencies for wifi networks '''

    def setupInterface(self):
        ''' Puts the interface into monitor mode '''

        print(f"Placing {self.interface} into monitor mode")
        os.system('ifconfig ' + self.interface + ' down')
        try:
            os.system('iwconfig ' + self.interface + ' mode monitor')
        except:
            print("Failed to setup monitor mode")
            return False

        os.system('ifconfig ' + self.interface + ' up')
        
        return True

    def __init__(self, interface):
        ''' init method '''

        self.interface = str(interface)
        self.ch = 1
        self.targetList = []
        self.quickList = []
        self.loadDictionary()
        self.setupInterface()
        self.validChannel = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '36', '38', '40', '42', '44', '46', '48', '52', '54', '56', '58', '60', '62', '64', '100', '102', '104', '106'}
        self.loadTargets()

    def loadDictionary(self):
        ''' Handles setting up the dictionary that will give the vendor identification'''

        with open('oui.csv', mode='r') as infile: # large registry
            reader = csv.reader(infile)

            self.vendorDict = {rows[1]:rows[2] for rows in reader}

            #print(f"{len(self.vendorDict)}")

        with open('mam.csv', mode='r') as infile: # medium registry
            reader = csv.reader(infile)

            midDict = {rows[1]:rows[2] for rows in reader}

            self.vendorDict.update(midDict)

            #print(f"{len(self.vendorDict)}")

        with open('oui36.csv', mode='r') as infile: # small registry
            reader = csv.reader(infile)

            smallDict = {rows[1]:rows[2] for rows in reader}

            self.vendorDict.update(smallDict)

            #print(f"{len(self.vendorDict)}")

    def callback(self, packet):
        ''' method to parse out the packet data and add it to the target list '''
        if packet.haslayer(Dot11Beacon): # else do nothing
            # extract the MAC address of the network
            bssid = packet[Dot11].addr2
            # get the name of it
            ssid = packet[Dot11Elt].info.decode()
            try:
                dbm_signal = packet.dBm_AntSignal
            except:
                dbm_signal = "N/A"
            # extract network stats
            stats = packet[Dot11Beacon].network_stats()
            # get the channel of the AP
            channel = stats.get("channel")
            # get the crypto
            crypto = stats.get("crypto")
            
            newTarget = WifiTarget(bssid, ssid, dbm_signal, channel, crypto)
            newTarget.setVendor(self.vendorDict.get(newTarget.key))

            self.quickList.append(newTarget)

            # Adding Target to Target List
            matched = False
            for target in self.targetList: 
                
                if target.matchTarget(newTarget) : 
                    matched = True
                    break # found match, exit loop

            if not matched : 

                self.targetList.append(newTarget)


    def loop_channels(self):
        ''' loops through the possible wifi channels \n needs to be a separate thread'''

        while True:

            for channel in self.validChannel:
                self.ch = channel

                #print(self.ch)

                os.system(f"iwconfig {self.interface} channel {self.ch}")

                time.sleep(0.2) # scanning time
                
            

    def printTarget(self):
        ''' prints out the currently tracked targets to the screen \n needs to be a separate thread'''

        # initialize the networks dataframe that will contain all access points nearby 
        pandas.set_option('display.max_rows', None)
        networks = pandas.DataFrame(columns=["BSSID", "SSID", "Vendor", "dBm_Signal", "Channel", "Crypto"])
        # set the index BSSID (MAC address of the AP)
        networks.set_index("BSSID", inplace=True)

        while True:

            os.system("clear")

            for target in self.quickList: 

                if "dji" in str(target.vendor).lower() or "skydio" in str(target.vendor).lower() or "yune" in str(target.vendor).lower() or "parrot" in str(target.vendor).lower() or "rasp" in str(target.vendor).lower() or "none" in str(target.vendor).lower():
                    networks.loc[target.bssid] = (target.ssid, target.vendor, target.dBm, target.ch, target.crypto)

            # clear the quicklist so that old signals go away
            self.quickList = []
            print(networks)
            print(f"Total length: {len(self.targetList)}\n")

            #temp
            saveFile = open('wifiLog.pkl', 'wb')
            pickle.dump(self.targetList, saveFile, -1)
            saveFile.close()

            time.sleep(1)

    def saveTargets(self):
        ''' Regularly saves the targets to a file for storage '''

        while True:

            saveFile = open('wifiLog.pkl', 'wb')
            pickle.dump(self.targetList, saveFile, -1)
            saveFile.close()

            print("Writing to log")

            time.sleep(60)

    def loadTargets(self):
        ''' Loads the old target list from a pickle '''
        try:
            f = open('wifiLog.pkl', 'rb')
            print("Loading old Target List")
            self.targetList = pickle.load(f)
            #print(str(self.targetList))
            f.close()
        except:
            print("Load file does not exist")

    def startSniffer(self):
        ''' Starts and runs the packet sniffer \n note: because this is blocking, it must be its own thread '''
        # start sniffing
        try:
            sniff(prn=self.callback, iface=self.interface)
        except TypeError:
            print("Scapy ran into a type error")
            # Restart thread
            self.snifferThread = Thread(target=self.startSniffer, daemon=False)
            self.snifferThread.start()

    def close(self):
        self.snifferThread.setDaemon(True)
        sys.exit()
                    
    def startScanner(self):
        ''' starts the channel hopper and display before starting the packet sniffer loops '''

        self.snifferThread = Thread(target=self.startSniffer, daemon=False)
        self.snifferThread.start()
        
        self.printerThread = Thread(target=self.printTarget, daemon=True)
        self.printerThread.start()

        self.channelHopper = Thread(target=self.loop_channels, daemon=True)
        self.channelHopper.start()

        self.saveThread = Thread(target=self.saveTargets, daemon=True)
        self.saveThread.start()
        
def check_root():
    ''' Checks to see if the system is running as root, wifi will break if not '''

    if not os.geteuid() == 0 : 
	    print("Run as root.")
	    exit(1)

if __name__ == "__main__":
    
    print("Starting standalone scanner: ")

    # check to see if running as root
    check_root()

    # default interface
    interface = "wlx9cefd5fd14f7"

    # looks for custom arguments
    if len(sys.argv) > 1 :
        interface = str(sys.argv[1])

    print(f"Using interface: {interface}")

    try:
        scanner = WifiScanner(interface)
        scanner.startScanner()
    except (KeyboardInterrupt, SystemExit):
        print("shutting Down")
        scanner.close()