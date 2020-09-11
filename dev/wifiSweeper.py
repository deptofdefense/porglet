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
        self.validChannel = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '36', '38', '40', '42', '44', '46', '48', '52', '54', '56', '58', '60', '62', '64', '100', '102', '104', '106'}

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
            elif (int(freq) >= 5150000000) and (int(freq) <= 5835000000): # in the 5GHz range
                if abs(int(freq) - 5160000000) <= 10 and '32' in self.validChannel : 
                    channelSet.add('32')
                if abs(int(freq) - 5170000000) <= 20 and '34' in self.validChannel :
                    channelSet.add('34')
                if abs(int(freq) - 5180000000) <= 10 and '36' in self.validChannel :
                    channelSet.add('36')
                if abs(int(freq) - 5190000000) <= 20 and '38' in self.validChannel :
                    channelSet.add('38')
                if abs(int(freq) - 5200000000) <= 10 and '40' in self.validChannel :
                    channelSet.add('40')
                if abs(int(freq) - 5210000000) <= 40 and '42' in self.validChannel :
                    channelSet.add('42')
                if abs(int(freq) - 5220000000) <= 10 and '44' in self.validChannel :
                    channelSet.add('44')
                if abs(int(freq) - 5230000000) <= 20 and '46' in self.validChannel :
                    channelSet.add('46')
                if abs(int(freq) - 5240000000) <= 10 and '48' in self.validChannel :
                    channelSet.add('48')
                if abs(int(freq) - 5250000000) <= 80 and '50' in self.validChannel :
                    channelSet.add('50')
                if abs(int(freq) - 5260000000) <= 10 and '52' in self.validChannel :
                    channelSet.add('52')
                if abs(int(freq) - 5270000000) <= 20 and '54' in self.validChannel :
                    channelSet.add('54')
                if abs(int(freq) - 5280000000) <= 10 and '56' in self.validChannel :
                    channelSet.add('56')
                if abs(int(freq) - 5290000000) <= 40 and '58' in self.validChannel :
                    channelSet.add('58')
                if abs(int(freq) - 5300000000) <= 10 and '60' in self.validChannel :
                    channelSet.add('60')
                if abs(int(freq) - 5310000000) <= 20 and '62' in self.validChannel :
                    channelSet.add('62')
                if abs(int(freq) - 5320000000) <= 10 and '64' in self.validChannel :
                    channelSet.add('64')
                if abs(int(freq) - 5340000000) <= 10 and '68' in self.validChannel :
                    channelSet.add('68')
                if abs(int(freq) - 5480000000) <= 10 and '96' in self.validChannel :
                    channelSet.add('96')
                if abs(int(freq) - 5500000000) <= 10 and '100' in self.validChannel :
                    channelSet.add('100')
                if abs(int(freq) - 5510000000) <= 20 and '102' in self.validChannel :
                    channelSet.add('102')
                if abs(int(freq) - 5520000000) <= 10 and '104' in self.validChannel :
                    channelSet.add('104')
                if abs(int(freq) - 5530000000) <= 40 and '106' in self.validChannel :
                    channelSet.add('106')
                if abs(int(freq) - 5540000000) <= 10 and '108' in self.validChannel :
                    channelSet.add('108')
                if abs(int(freq) - 5550000000) <= 20 and '110' in self.validChannel :
                    channelSet.add('110')
                if abs(int(freq) - 5560000000) <= 10 and '112' in self.validChannel :
                    channelSet.add('112')
                if abs(int(freq) - 5570000000) <= 80 and '114' in self.validChannel :
                    channelSet.add('114')
                if abs(int(freq) - 5580000000) <= 10 and '116' in self.validChannel :
                    channelSet.add('116')
                if abs(int(freq) - 5590000000) <= 20 and '118' in self.validChannel :
                    channelSet.add('118')
                if abs(int(freq) - 5600000000) <= 10 and '120' in self.validChannel :
                    channelSet.add('120')
                if abs(int(freq) - 5610000000) <= 40 and '122' in self.validChannel :
                    channelSet.add('122')
                if abs(int(freq) - 5620000000) <= 10 and '124' in self.validChannel :
                    channelSet.add('124')
                if abs(int(freq) - 5630000000) <= 20 and '126' in self.validChannel :
                    channelSet.add('126')
                if abs(int(freq) - 5640000000) <= 10 and '128' in self.validChannel :
                    channelSet.add('128')
                if abs(int(freq) - 5660000000) <= 10 and '132' in self.validChannel :
                    channelSet.add('132')
                if abs(int(freq) - 5670000000) <= 20 and '134' in self.validChannel :
                    channelSet.add('134')
                if abs(int(freq) - 5680000000) <= 10 and '136' in self.validChannel :
                    channelSet.add('136')
                if abs(int(freq) - 5690000000) <= 40 and '138' in self.validChannel :
                    channelSet.add('138')
                if abs(int(freq) - 5700000000) <= 10 and '140' in self.validChannel :
                    channelSet.add('140')
                if abs(int(freq) - 5710000000) <= 20 and '142' in self.validChannel :
                    channelSet.add('142')
                if abs(int(freq) - 5720000000) <= 10 and '144' in self.validChannel :
                    channelSet.add('144')
                if abs(int(freq) - 5745000000) <= 10 and '149' in self.validChannel :
                    channelSet.add('149')
                if abs(int(freq) - 5755000000) <= 20 and '151' in self.validChannel :
                    channelSet.add('151')
                if abs(int(freq) - 5765000000) <= 10 and '153' in self.validChannel :
                    channelSet.add('153')
                if abs(int(freq) - 5775000000) <= 40 and '155' in self.validChannel :
                    channelSet.add('155')
                if abs(int(freq) - 5785000000) <= 10 and '157' in self.validChannel :
                    channelSet.add('157')
                if abs(int(freq) - 5795000000) <= 20 and '159' in self.validChannel :
                    channelSet.add('159')
                if abs(int(freq) - 5805000000) <= 10 and '161' in self.validChannel :
                    channelSet.add('161')
                if abs(int(freq) - 5825000000) <= 10 and '165' in self.validChannel :
                    channelSet.add('165')
                if abs(int(freq) - 5845000000) <= 10 and '169' in self.validChannel :
                    channelSet.add('169')
                if abs(int(freq) - 5865000000) <= 10 and '173' in self.validChannel :
                    channelSet.add('173')
                
        self.channelList = list(channelSet)

        #print(self.channelList)

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
            #for target in self.targetList :
            #    if target.updateTimeout(self.ch):
            #        self.targetList.remove(target)

            # sets the new channels and clears the list
            currentChannels = self.channelList
            self.channelList = []

            #print(currentChannels)
            #print(self.channelList)

            if len(currentChannels) < 1:
                #print('X')
                time.sleep(0.001) # wait time
            else:
                #print(f"\n{currentChannels}")
                for channel in currentChannels:
                    self.ch = channel

                    #print(self.ch)

                    os.system(f"iwconfig {self.interface} channel {self.ch}")

                    time.sleep(0.4) # scanning time
            

    def printTarget(self):
        ''' prints out the currently tracked targets to the screen \n needs to be a separate thread'''

        # initialize the networks dataframe that will contain all access points nearby 
        #pandas.set_option('display.max_rows', None)
        networks = pandas.DataFrame(columns=["BSSID", "SSID", "Vendor", "dBm_Signal", "Channel", "Crypto"])
        # set the index BSSID (MAC address of the AP)
        networks.set_index("BSSID", inplace=True)

        while True:

            os.system("clear")

            for target in self.targetList: 

                networks.loc[target.bssid] = (target.ssid, target.vendor, target.dBm, target.ch, target.crypto)

            print(networks)
            print(f"Total length: {len(self.targetList)}\n")

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