# Displays the wiki logs for easy reading

from wifiScanner import WifiTarget # needed for wifi targets

import pandas # used for pretty print to screen
import time # needed for sleep
import os # needed to run commands

import csv # needed for manufacturer lookup
import pickle # needed for data writing / reading

targetList = []

#open the log file
try:
    f = open('wifiLog.pkl', 'rb')
    print("Loading old Target List")
    targetList = pickle.load(f)
    #print(str(self.targetList))
    f.close()
except:
    print("Load file does not exist")


# initialize the networks dataframe that will contain all access points nearby 
pandas.set_option('display.max_rows', None)
networks = pandas.DataFrame(columns=["BSSID", "SSID", "Vendor", "dBm_Signal", "Channel", "Crypto"])
# set the index BSSID (MAC address of the AP)
networks.set_index("BSSID", inplace=True)

for target in targetList:
    networks.loc[target.bssid] = (target.ssid, target.vendor, target.dBm, target.ch, target.crypto)

print(networks)
print(f"Total length: {len(targetList)}\n")