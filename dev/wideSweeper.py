import subprocess # needed for hackrf sweep
import sys # needed for file stuff
import os # needed for file stuff
import time # needed for sleep
from threading import Thread # needed for threads

class WideSweeper:
    ''' Class to handle sweeping RF channels for porglet '''

    def __init__(self, minFreq, maxFreq, binSize):
        ''' init method '''

        self.minFreq = minFreq
        self.maxFreq = maxFreq
        self.binSize = binSize
        self.noiseFloor = float(-50)
        self.freqList = []
        self.subscribers = set()

    def close(self):
        ''' close down the module '''
        self.bigSweep.kill()
        self.sweepThread.setDaemon(True)
        sys.exit()

    def register(self, who):
        ''' registers new subscriber to the set '''

        self.subscribers.add(who)
    
    def removeSub(self, who):
        ''' removes subscriber from set '''
        
        self.subscribers.discard(who)
    
    def updateFreqList(self, newList):
        ''' Update method used to identify when to call observer updater '''

        self.freqList = newList

        for subscriber in self.subscribers: # updates all subscribers
            subscriber.update(self.freqList)

    def sweepFrequencies(self):
        ''' spawns the hackrf_sweep process and then acts on its output '''

        self.bigSweep = subprocess.Popen(["hackrf_sweep", f"-f {self.minFreq}:{self.maxFreq}", f"-w {self.binSize}"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        #self.bigSweep = subprocess.Popen(["hackrf_sweep", "-f 400:6000", "-w 1000000"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

        startFreq = str(self.minFreq) + "000000" # minFreq is in MHz, but output is in Hz

        tempFloor = float(0)
        counter = 0
        tempFreq = []


        while True:
            #try:
            splitStr = self.bigSweep.stdout.readline().split(", ")

            if len(splitStr) >= 11: # reading a data string

                tempFloor = tempFloor + float(splitStr[6]) + float(splitStr[7]) + float(splitStr[8]) + float(splitStr[9]) + float(splitStr[10])
                counter = counter + 5

                if splitStr[2] == startFreq: # check if a loop has finished

                    self.noiseFloor = tempFloor / counter
                    self.updateFreqList(tempFreq)
                    
                    # Reset temp variables
                    counter = float(0)
                    tempFloor = float(0)
                    tempFreq = []

                    # display info for debugging
                    localTime = time.asctime(time.localtime(time.time()))
                    #print("\nLoop completed at: " + localTime)
                    #print("New noise floor: " + str(self.noiseFloor))
                    #print(f"Total Targets: {len(self.freqList)}")

                    
                if float(splitStr[6]) > self.noiseFloor: # First freqency is worth checking out
                    tempFreq.append(int(splitStr[2]) + (0 * round(float(splitStr[4]))))
                if float(splitStr[7]) > self.noiseFloor: # Second freqency is worth checking out
                    tempFreq.append(int(splitStr[2]) + (1 * round(float(splitStr[4]))))
                if float(splitStr[8]) > self.noiseFloor: # Third freqency is worth checking out
                    tempFreq.append(int(splitStr[2]) + (2 * round(float(splitStr[4]))))
                if float(splitStr[9]) > self.noiseFloor: # Fourth freqency is worth checking out
                    tempFreq.append(int(splitStr[2]) + (3 * round(float(splitStr[4]))))
                if float(splitStr[10]) > self.noiseFloor: # Fifth freqency is worth checking out
                    tempFreq.append(int(splitStr[2]) + (4 * round(float(splitStr[4]))))                    
                
                
                
            else:
                print("Something went wrong with spliting bigSweep response")
                self.bigSweep.kill()
                sys.exit()

            #except(KeyboardInterrupt, SystemExit):
                #self.bigSweep.kill()
                #raise
        
    def startSweeper(self):
        ''' spawns all the sweeper threads'''

        self.sweepThread = Thread(target=self.sweepFrequencies, daemon=False)
        self.sweepThread.start()
        


if __name__ == "__main__":

    sweeper = WideSweeper(400, 6000, 1000000)

    sweeper.startSweeper()