# Standalone Porglet: Sonic

## Design

Unlike regular porglet, the standalone version is designed to run each of the submodules (Galileo, WiFi, Zigbee, ect) independently without using the wide sweeper to coordinate which frequency the scanners are looking at.

## Programs

### Galileo

TBA

### Wifi

[wifiScanner](./wifiScanner.py) is the standalone version of the WiFi Scanner software.  To run it with a unique wifi dongle, run `sudo python3 wifiScanner.py <InterfaceName>`.  In order to use commands like `iwconfig`, the program must be run as root.  

It will write all the targets that it sees to a binary pickle file [wifiLog](./wifiLog.pkl).  This log is updated every minute, and consists of a serialized list of Wifi networks seen.  High priority targets, like DJI, Parrot, Skydio, ect targets will get printed straight to the terminal when they are noticed.  However all networks seen will get written to the log file.  To view the log file after the fact, use [wifiLogReader](./wifiLogReader.py) to display the contents of the file.

To update the dictionary of MAC addresses and vendors, run [macUpdater](./macUpdater.py) to pull the latest csv files from the IEEE.  Note: these lists do not update often and require a internet connection, so for right now there is no plan to automate updating the list.

### Zigbee

Currently using [pyCCSniffer](https://github.com/andrewdodd/pyCCSniffer) as the base code for the zigbee sniffer.  We're working on design a dummy target before we go to much deeper on the scanner design