from scapy.all import * # needed for reading the packets
from threading import Thread # needed for multithreading
import pandas # used for pretty print to screen
import time # needed for sleep
import os # needed to run commands

import csv # needed for manufacturer lookup

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






class WifiSweeper:
    ''' Class that handles sweeping wifi channels for porglet '''

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
        self.loadDictionary()
        self.setupInterface()
        self.channelList = []

    def loadDictionary(self):
        ''' Handles setting up the dictionary that will give the vendor '''

        with open('oui.csv', mode='r') as infile:
            reader = csv.reader(infile)

            self.vendorDict = {rows[1]:rows[2] for rows in reader}

    def update(self, freqList):
        ''' updates the scanner list based off of seen frequencies from the wide sweeper '''

        channelSet = set()

        for freq in freqList: # check each frequency

            if (int(freq) >= 2401000000) and (int(freq) <= 2495000000): # in the 2.4GHz band
                '''if (int(freq) >= 2401000000) and (int(freq) <= 2423000000): # channel 1
                    channelSet.add('1')
                elif (int(freq) >= 2406000000) and (int(freq) <= 2428000000): # channel 2
                    channelSet.add('2')
                elif (int(freq) >= 2411000000) and (int(freq) <= 2433000000): # channel 3
                    channelSet.add('3')
                elif (int(freq) >= 2416000000) and (int(freq) <= 2438000000): # channel 4
                    channelSet.add('4')
                elif (int(freq) >= 2421000000) and (int(freq) <= 2443000000): # channel 5
                    channelSet.add('5')
                elif (int(freq) >= 2426000000) and (int(freq) <= 2448000000): # channel 6
                    channelSet.add('6')
                elif (int(freq) >= 2431000000) and (int(freq) <= 2453000000): # channel 7
                    channelSet.add('7')
                elif (int(freq) >= 2436000000) and (int(freq) <= 2458000000): # channel 8
                    channelSet.add('8')
                elif (int(freq) >= 2441000000) and (int(freq) <= 2463000000): # channel 9
                    channelSet.add('9')
                elif (int(freq) >= 2446000000) and (int(freq) <= 2468000000): # channel 10
                    channelSet.add('10')
                elif (int(freq) >= 2451000000) and (int(freq) <= 2473000000): # channel 11
                    channelSet.add('11')
                elif (int(freq) >= 2456000000) and (int(freq) <= 2478000000): # channel 12
                    channelSet.add('12')
                elif (int(freq) >= 2461000000) and (int(freq) <= 2483000000): # channel 13
                    channelSet.add('13')
                else: # channel 14
                    channelSet.add('14')
            elif (int(freq) >= 5150000000) and (int(freq) <= 5815000000): # in the 5GHz band
                if (int(freq) >= 5150000000) and (int(freq) <= 5190000000): # channel 36
                elif (int(freq) >= 5170000000) and (int(freq) <= 5190000000): # channel 36
                    channelSet.add('36')
                    channelSet.add('38')'''
                if abs(int(freq) - 2412000000) <= 11:
                    channelSet.add('1')
                if abs(int(freq) - 2417000000) <= 11:
                    channelSet.add('2')
                if abs(int(freq) - 2422000000) <= 11:
                    channelSet.add('3')
                if abs(int(freq) - 2427000000) <= 11:
                    channelSet.add('4')
                if abs(int(freq) - 2432000000) <= 11:
                    channelSet.add('5')
                if abs(int(freq) - 2437000000) <= 11:
                    channelSet.add('6')
                if abs(int(freq) - 2442000000) <= 11:
                    channelSet.add('7')
                if abs(int(freq) - 2447000000) <= 11:
                    channelSet.add('8')
                if abs(int(freq) - 2452000000) <= 11:
                    channelSet.add('9')
                if abs(int(freq) - 2457000000) <= 11:
                    channelSet.add('10')
                if abs(int(freq) - 2462000000) <= 11:
                    channelSet.add('11')
                if abs(int(freq) - 2467000000) <= 11:
                    channelSet.add('12')
                if abs(int(freq) - 2472000000) <= 11:
                    channelSet.add('13')
                if abs(int(freq) - 2484000000) <= 11:
                    channelSet.add('14')


        self.channelList = list(channelSet)

        print(self.channelList)

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

            # Prunes the list
            for target in self.targetList :
                if target.updateTimeout(self.ch):
                    self.targetList.remove(target)

            # sets the new channel
            for channel in self.channelList:
                self.ch = channel

                os.system(f"iwconfig {self.interface} channel {self.ch}")

                time.sleep(0.1) # scanning time
            time.sleep(0.1) # scanning time


    def printTarget(self):
        ''' prints out the currently tracked targets to the screen \n needs to be a separate thread'''

        while True:

            os.system("clear")

            # initialize the networks dataframe that will contain all access points nearby 
            pandas.set_option('display.max_rows', None)
            networks = pandas.DataFrame(columns=["BSSID", "SSID", "Vendor", "dBm_Signal", "Channel", "Crypto"])
            # set the index BSSID (MAC address of the AP)
            networks.set_index("BSSID", inplace=True)

            for target in self.targetList: 

                networks.loc[target.bssid] = (target.ssid, target.vendor, target.dBm, target.ch, target.crypto)

            print(networks)
            print(f"Total length: {len(self.targetList)}")

            time.sleep(1)

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

        self.printerThread = Thread(target=self.printTarget, daemon=True)
        self.printerThread.start()

        self.channelHopper = Thread(target=self.loop_channels, daemon=True)
        self.channelHopper.start()

        self.snifferThread = Thread(target=self.startSniffer, daemon=False)
        self.snifferThread.start()