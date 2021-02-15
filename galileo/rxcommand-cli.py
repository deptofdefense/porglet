"""RX Commander.

Usage:
  rxcommand-cli.py  send --channel=<int> --frequency=<mhz> --gain=<int>  --enabled=<int>
  rxcommand-cli.py -h | --help
  rxcommand-cli.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --channel=<int>  Channel to use 
  --gain=<int>  Gain to use 
  --enabled=<int>   Enable or disable the scan 
  --frequency=<mhz>  Frequency to use Mhz

"""
from docopt import docopt
from rxcommand import Backend

if __name__ == '__main__':
    arguments = docopt(__doc__, version='RX Commander 1.0')
    print(arguments['--channel'])
    channel=arguments['--channel']
    frequency=arguments['--frequency']
    gain=arguments['--gain']
    enabled=arguments['--enabled']
    be = Backend()
    be.setUpRxCommandRequest(channel, frequency, gain, enabled)
