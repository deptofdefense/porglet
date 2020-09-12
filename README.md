# PORGLET

PORGLET is a low cost and small form factor drone detection system.  The intent of this project is to have a small detector/analyzer that can be sent ahead of a rapid response team to allow for more thorough site visits and provide actionable information about which drones are flying over a location.

## Design

Porglet works by having multiple low cost sensors working together to sweep through the 1 MHz to 6 GHz spectrum and attempt to identify and log any suspected drone signals.  By using multiple low cost devices, we replicate the functionality of a large expensive SDR platform in a more disposable setup.

The standalone version of porglet can be found [here](./standAlone/README.md).  In this version, each scanner operates as separate standalone programs operating and logging data in isolation.  This build was designed for rapid deployment because by keeping the modules isolated there's no risk of cascading failures.  However this version of porglet should also be the slowest, because there is no attempt to optimize the scanning techniques of the modules.

The integrated version of porglet is found [here](./dev/README.md)

### Wide Sweeper

The Wide Sweeper is a HackRF SDR that rapidly scans the frequency range of 1 MHz to 6 GHz roughly every half second.  The point of this scan is to make FFT measurements of each of those frequencies with a 1 MHz wide bin size.  By comparing the dB value of an individual bin with the average amplitude across the entire scan we are able to guess which radio frequencies are being used to transmit a signal at that given instance of time.  The wide sweeper than passes this list of suspected frequencies to the other scanners, who can use this information to optimize their own scanning of the network.  

The goal is that by preemptively identifying which frequencies may contain a signal of interest, the other scanners in the system can operate in a more efficient manner than just sweeping repeatably through all of their respective channels.

### Wifi Sweeper

The Wifi sweeper works by scanning both the 2.4GHz and 5GHz bands to identify all wireless networks running in the area.  It then compares the BSSID addresses of each access point to see if they match any vendor of interest.  If there is a match it is printed out on the terminal as an alert, otherwise it gets silently added to the log file.

