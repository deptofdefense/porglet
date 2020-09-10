import os # needed for root check
import sys # needed for arg parsing
import subprocess # needed to run subprocesses


# defaults
interface = "wlx9cefd5fcd434"

output = ""
test = subprocess.check_output(["iwlist", "channel"], text=True, stderr=subprocess.STDOUT)


#print(test)
