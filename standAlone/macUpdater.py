# Standalone python script that grabs the latest mac address list files from the IEEE and saves them locally

import wget # needed to pull files

print("Welcome to the MAC address list downloader for Porglet.  This tool will grab the 3 MAC registry lists from the publically hosted IEE site and download them locally")

# The URL to the MA-L CSV - the Large Block Registry
malURL = "http://standards-oui.ieee.org/oui/oui.csv"

# this is the URL to the MA-M CSV - the Medium Block Registry
mamURL = "http://standards-oui.ieee.org/oui28/mam.csv"

# this is the URL to the MA-S CSV - the Small Bloc Registry
masURL = "http://standards-oui.ieee.org/oui36/oui36.csv"

print("Starting downloads:")

wget.download(malURL) # Downloading the large registry

wget.download(mamURL) # Downloading the medium registry

wget.download(masURL) # Downloading the small registry

print("Finished")

