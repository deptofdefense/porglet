# PORGLET

PORGLET is a low cost and small form factor drone detection system.  The intent of this project is to have a small detector/analyzer that can be sent ahead of a rapid response team to allow for more thorough site visits and provide actionable information about which drones are flying over a location.

## Design

Porglet works by having multiple low cost sensors working together to sweep through the 1 MHz to 6 GHz spectrum and attempt to identify and log any suspected drone signals.  By using multiple low cost devices, we replicate the functionality of a large expensive SDR platform in a more disposable setup.

The standalone version of porglet can be found [here](./standAlone/).  

The integrated version of porglet is found [here](./dev/)

### Wide Sweeper

The Wide Sweeper is a HackRF SDR that rapidly scans the frequency range of 1 MHz to 6 GHz roughly every half second.  The point of this scan is to make FFT measurements of each of those frequencies with a 1 MHz wide bin size.  By comparing the dB value of an individual bin with the average amplitude across the entire scan we are able to guess which radio frequencies are being used to transmit a signal at that given instance of time.  The wide sweeper than passes this list of suspected frequencies to the other scanners, who can use this information to optimize their own scanning of the network.  

The goal is that by preemptively identifying which frequencies may contain a signal of interest, the other scanners in the system can operate in a more efficient manner than just sweeping repeatably through all of their respective channels.

### Wifi Sweeper

The Wifi sweeper works by scanning both the 2.4GHz and 5GHz bands to identify all wireless networks running in the area.  It then compares the BSSID addresses of each access point to see if they match any vendor of interest.  If there is a match it is printed out on the terminal as an alert, otherwise it gets silently added to the log file.

### Zigbee Sweeper

The Zigbee sweeper works using a modified TI Zigbee dongle to listen and decode zigbee packets sent within range of the device

### Galileo

Galileo exists as a docker program that scans the current band it is looking at for any recognizable hopping pattern that could be tied to a specific handset or drone.

### Reporting

This is a stub, but as of now we are looking at the python hyde static generator, see /web

```
pip install hyde
hyde -s ~/porglet/web create
cd web
hyde gen
hyde serve
```

### Todos

1. Integrate rxcommand with widesweeper when frequency of interest is encountered
2. Configure stomp listener to send sigdetect event to rabbitmq
3. Create main file that starts all sweepers
4. Reporting(static html - daily reports?)
5. Waterfalls in reports via [d3 waterfall lib](https://github.com/ddcc/d3-waterfall/)

## Development Environment

### Dependencies
* Python 3.x
* [hackrf tools](https://github.com/mossmann/hackrf/wiki/Operating-System-Tips)
* python packages
  * `pip install pika docopt pandas pickle stomp.py protobuf hyde`


### Rabbitmq
You need a rabbitmq server running on the host running porglet. 
Adapted instructions from [their site follow](https://www.rabbitmq.com/install-debian.html) for an Ubuntu 20.04 box
```
curl -fsSL https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc | sudo apt-key add -
sudo apt-key adv --keyserver "hkps://keys.openpgp.org" --recv-keys "0x0A9AF2115F4687BD29803A206B73A36E6026DFCA"
sudo apt-get install apt-transport-https
vim /etc/apt/sources.list.d/bintray.erlang.list
sudo tee /etc/apt/sources.list.d/bintray.erlang.list <<EOF
# This repository provides Erlang packages produced by the RabbitMQ team
# See below for supported distribution and component values
deb https://dl.bintray.com/rabbitmq-erlang/debian focal erlang-22.x
EOF
sudo apt-get update -y
sudo apt-get install -y erlang-base                         erlang-asn1 erlang-crypto erlang-eldap erlang-ftp erlang-inets                         erlang-mnesia erlang-os-mon erlang-parsetools erlang-public-key                         erlang-runtime-tools erlang-snmp erlang-ssl                         erlang-syntax-tools erlang-tftp erlang-tools erlang-xmerl
sudo apt-get install rabbitmq-server -y --fix-missing
```

### Remote Development
Ultimately, porglet will have a handful of dongles plugged into it. Although you could develop it locally to an extent, you'll most likely be developing on a remote box. You can ssh in and rock vim or you can mount the remote machine with sshfs. 
#### SSH Config
Although you can access the machine with the hostname, for example `stk-NUC10i7FNK` the keystroke conscious developer may create a shortcut in `~/.ssh/config`
```
Host porg
    HostName 192.168.1.208
    User xmmgr
```
It is recommended to add your public key(`~/.ssh/id_rsa.pub`) to the remote machines authorized_keys file(`~/.ssh/authorized_keys`). Once done you will not be prompted for a password.

#### SSHFS config
brew install --cask osxfuse
sshfs porg:/home/xmmgr/porglet ~/dev/porglet/nuc
code ~/dev/porglet/nuc

## Directory Structure
### [dev](./dev/)
This is the integrated porglet application

### [standAlone](./standAlone/)
In this version, each scanner operates as separate standalone programs operating and logging data in isolation.  This build was designed for rapid deployment because by keeping the modules isolated there's no risk of cascading failures.  However this version of porglet should also be the slowest, because there is no attempt to optimize the scanning techniques of the modules.

### [support](./support)
Utility scripts to help with various tasks like IQ file conversions.

### [rxcommand](./rxcommand/)
A class and cli POC for sending RX control messages to CFE/Galileo. When porglet detects an interesting signal it can tell galileo to investigate.

### [web](./web/)
Hyde static generated site