from scapy.all import *
from threading import Thread
import pandas
import time
import os

# interface name, check using iwconfig

interface = "wlx9cefd5fcd434"
#interface = "wlx9cefd5fd14f7"

os.system('ifconfig ' + interface + ' down')
try:
    os.system('iwconfig ' + interface + ' mode monitor')
except:
    print("Failed to setup monitor mode")
os.system('ifconfig ' + interface + ' up')

# initialize the networks dataframe that will contain all access points nearby
networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])
# set the index BSSID (MAC address of the AP)
networks.set_index("BSSID", inplace=True)

channelList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '36', '38', '40', '42', '44', '46', '48', '52', '54', '56', '58', '60', '62', '64', '100', '102', '104', '106']

def callback(packet):
    if packet.haslayer(Dot11Beacon):
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
        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)

def print_all():
    while True:
        os.system("clear")
        print(networks)
        print(f"Total: {len(networks)}")
        time.sleep(1)


def change_channel():
    while True:
        #print(f"\n{channelList}")
        for ch in channelList:
            #print(f"{ch}")
            os.system(f"iwconfig {interface} channel {ch}")
            time.sleep(0.4)



if __name__ == "__main__":
    
    # start the thread that prints all the networks
    printer = Thread(target=print_all)
    printer.daemon = True
    printer.start()

    # start the channel changer
    channel_changer = Thread(target=change_channel)
    channel_changer.daemon = True
    channel_changer.start()

    # start sniffing
    sniff(prn=callback, iface=interface)
