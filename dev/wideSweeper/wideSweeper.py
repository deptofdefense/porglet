import subprocess # needed for hackrf sweep
import sys # needed for rabbit
import os # needed for file stuff
import time # needed for sleep
from threading import Thread # needed for threads

import pika # needed for rabbitMQ

class WideSweeper:
    ''' Class to handle sweeping RF channels for porglet '''

    def __init__(self, minFreq, maxFreq, binSize, freqDBMadjust, pwrDBMadjust):
        """init method

        Args:
            minFreq (int): the start frequency of the scan in MHz
            maxFreq (int): the end frequency of the scan in MHz
            binSize (int): the bin size of each scan in Hz
            freqDBMadjust (float): the offset to adjust the average power of the freq scan
            pwrDBMadjust (float): the offset to adjust the average power of the pwr scan
        """

        self.minFreq = minFreq
        self.maxFreq = maxFreq
        self.binSize = binSize
        self.noiseFloor = float(-50)
        self.highPowerFloor = float(-40)
        self.freqDBMadjust = float(freqDBMadjust)
        self.pwrDBMadjust = float(pwrDBMadjust)

        # rabbitMQ setup
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='freqSweep', exchange_type='fanout')
        self.channel.exchange_declare(exchange='pwrSweep', exchange_type='fanout')


    def close(self):
        ''' close down the module '''
        self.bigSweep.kill()
        self.sweepThread.setDaemon(True)
        sys.exit()
    
    def publishLists(self, freqList, dBmList, pwrList, dBmPwr):
        """Publishes the current lists out via RabbitMQ

        Args:
            freqList (List [ints]): A list of all of the frequencies of interest for a given sweep.  In Hz
            dBmList (List [floats]): A list of the associated dBm value for each frequency of interest
            freqList (List [ints]): A list of all of the high power frequencies of interest for a given sweep.  In Hz
            dBmList (List [floats]): A list of the associated dBm value for each high power frequency of interest
        """

        freqMessage = ""
        pwrMessage = ""

        for i in range(len(freqList)):
            freqMessage += f"{str(freqList[i])} {str(dBmList[i])} "

        for i in range(len(pwrList)):
            pwrMessage += f"{str(pwrList[i])} {str(dBmPwr[i])} "


        #print(freqMessage)
        self.channel.basic_publish(exchange='freqSweep', routing_key='', body=freqMessage)
        self.channel.basic_publish(exchange='pwrSweep', routing_key='', body=pwrMessage)


    def sweepFrequencies(self):
        ''' spawns the hackrf_sweep process and then acts on its output '''

        self.bigSweep = subprocess.Popen(["hackrf_sweep", f"-f {self.minFreq}:{self.maxFreq}", f"-w {self.binSize}"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        #self.bigSweep = subprocess.Popen(["hackrf_sweep", "-f 400:6000", "-w 1000000"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

        startFreq = str(self.minFreq) + "000000" # minFreq is in MHz, but output is in Hz

        tempFloor = float(0)
        counter = 0
        tempFreq = []
        tempDBm = []

        # temp variables for high power stuff
        tempPowerFloor = float(0)
        counterPwr = 0
        tempPwr = []
        tempDBmPwr = []

        while True:
            #try:
            splitStr = self.bigSweep.stdout.readline().split(", ")

            if len(splitStr) >= 11: # reading a data string

                tempFloor = tempFloor + float(splitStr[6]) + float(splitStr[7]) + float(splitStr[8]) + float(splitStr[9]) + float(splitStr[10])
                counter = counter + 5

                if splitStr[2] == startFreq: # check if a loop has finished

                    # update noise floor
                    if counter > 0: # small edge case that counter is 0
                        self.noiseFloor = (tempFloor / counter) + self.freqDBMadjust
                    if counterPwr > 0: # small edge case that counter is 0
                        self.highPowerFloor = (tempPowerFloor / counterPwr) + self.pwrDBMadjust

                    # publish list on rabbitMQ
                    self.publishLists(tempFreq, tempDBm, tempPwr, tempDBmPwr)
                    
                    # display info for debugging
                    localTime = time.asctime(time.localtime(time.time()))
                    print("\nLoop completed at: " + localTime)
                    print("New noise floor: " + str(self.noiseFloor))
                    print(f"Total Targets: {len(tempFreq)}")
                    print(f"New high power floor: {str(self.highPowerFloor)}")
                    print(f"Total High Power Targets: {str(len(tempPwr))}")

                    # Reset temp variables
                    counter = float(0)
                    tempFloor = float(0)
                    tempFreq = []
                    tempDBm = []

                    tempPowerFloor = float(0)
                    counterPwr = 0
                    tempPwr = []
                    tempDBmPwr = []
             
                if float(splitStr[6]) > self.noiseFloor: # First freqency is worth checking out
                    tempFreq.append(int(splitStr[2]) + (0 * round(float(splitStr[4]))))
                    tempDBm.append(float(splitStr[6]))

                    # update High Power Counter
                    tempPowerFloor = tempPowerFloor + float(splitStr[6])
                    counterPwr = counterPwr + 1

                    if float(splitStr[6]) > self.highPowerFloor: # First freqency is worth checking out for HighPwr
                        tempPwr.append(int(splitStr[2]) + (0 * round(float(splitStr[4]))))
                        tempDBmPwr.append(float(splitStr[6]))
                if float(splitStr[7]) > self.noiseFloor: # Second freqency is worth checking out
                    tempFreq.append(int(splitStr[2]) + (1 * round(float(splitStr[4]))))
                    tempDBm.append(float(splitStr[7]))

                    # update High Power Counter
                    tempPowerFloor = tempPowerFloor + float(splitStr[7])
                    counterPwr = counterPwr + 1

                    if float(splitStr[7]) > self.highPowerFloor: # Second freqency is worth checking out for HighPwr
                        tempPwr.append(int(splitStr[2]) + (1 * round(float(splitStr[4]))))
                        tempDBmPwr.append(float(splitStr[7]))

                if float(splitStr[8]) > self.noiseFloor: # Third freqency is worth checking out
                    tempFreq.append(int(splitStr[2]) + (2 * round(float(splitStr[4]))))
                    tempDBm.append(float(splitStr[8]))

                    # update High Power Counter
                    tempPowerFloor = tempPowerFloor + float(splitStr[8])
                    counterPwr = counterPwr + 1

                    if float(splitStr[8]) > self.highPowerFloor: # First freqency is worth checking out for HighPwr
                        tempPwr.append(int(splitStr[2]) + (2 * round(float(splitStr[4]))))
                        tempDBmPwr.append(float(splitStr[8]))

                if float(splitStr[9]) > self.noiseFloor: # Fourth freqency is worth checking out
                    tempFreq.append(int(splitStr[2]) + (3 * round(float(splitStr[4]))))
                    tempDBm.append(float(splitStr[9]))

                    # update High Power Counter
                    tempPowerFloor = tempPowerFloor + float(splitStr[9])
                    counterPwr = counterPwr + 1

                    if float(splitStr[9]) > self.highPowerFloor: # Fourth freqency is worth checking out for HighPwr
                        tempPwr.append(int(splitStr[2]) + (3 * round(float(splitStr[4]))))
                        tempDBmPwr.append(float(splitStr[9]))

                if float(splitStr[10]) > self.noiseFloor: # Fifth freqency is worth checking out
                    tempFreq.append(int(splitStr[2]) + (4 * round(float(splitStr[4]))))   
                    tempDBm.append(float(splitStr[10]))

                    # update High Power Counter
                    tempPowerFloor = tempPowerFloor + float(splitStr[10])
                    counterPwr = counterPwr + 1

                    if float(splitStr[10]) > self.highPowerFloor: # Fifth freqency is worth checking out for HighPwr
                        tempPwr.append(int(splitStr[2]) + (4 * round(float(splitStr[4]))))
                        tempDBmPwr.append(float(splitStr[10]))                 
                
            else:
                print("Something went wrong with spliting bigSweep response")
                self.bigSweep.kill()
                self.connection.close()
                sys.exit()

            #except(KeyboardInterrupt, SystemExit):
                #self.bigSweep.kill()
                #raise
        
    def startSweeper(self):
        ''' spawns all the sweeper threads'''

        self.sweepThread = Thread(target=self.sweepFrequencies, daemon=False)
        self.sweepThread.start()
        


if __name__ == "__main__":

    sweeper = WideSweeper(400, 6000, 1000000, 0, 5)

    sweeper.startSweeper()