# Base program for porglet

import os # needed for root check
import sys # needed for arg parsing
from threading import Thread # needed for threading

from wifiSweeper import WifiSweeper # needed for wifi sweeper
from wideSweeper import WideSweeper # needed for wide sweeper

def check_root():
    ''' Checks to see if the system is running as root, wifi will break if not '''

    if not os.geteuid() == 0 : 
	    print("Run as root.")
	    exit(1)
















if __name__ == "__main__":

    print("Starting Proglet")

    # make sure running as root
    check_root()

    # defaults
    interface = "wlx9cefd5fcd434"

    # looks for custom arguments
    if len(sys.argv) > 1 :
        interface = str(sys.argv[1])

    print(f"Using interface: {interface}")

    wifiSweeper = WifiSweeper(interface)

    freqSweeper = WideSweeper(400, 6000, 1000000)

    freqSweeper.register(wifiSweeper) # link to observer

    try:
        freqSweeper.startSweeper()
        wifiSweeper.startScanner()
    except (KeyboardInterrupt, SystemExit):
        freqSweeper.close()
        wifiSweeper.close()