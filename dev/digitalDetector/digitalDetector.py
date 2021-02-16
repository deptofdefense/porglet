import sys # needed for rabbit
import os # needed for file stuff
import time # needed for sleep
from threading import Thread # needed for threads

import pika # needed for rabbitMQ

class Detector:

    def __init__(self, windowSize, maxPercentage, minPercentage, bandwidth):
        """Simple init method

        Args:
            windowSize (int): How many cycles to look through
            maxPercentage (float): min precentage needed to be considered a digital signal
            minPercentage ([type]): max precentage needed to be considered a digital signal
            bandwidth (int): How close do detects need to be in MHz to merge
        """

        self.freqList = []
        self.maxPrecent = maxPercentage
        self.minPrecent = minPercentage
        self.bandwidth = bandwidth
        self.windowSize = windowSize

        # fill out the freqList with empty arrays
        for i in range(int(windowSize)):
            self.freqList.append([]) # creates empty window

    def linkRabbit(self):
            """Setup and start lisenting for RabbitMQ messages
            """

            print("Listening for RabbitMQ messages")

            # RabbitMQ setup
            connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()

            #channel.exchange_declare(exchange='freqSweep', exchange_type='fanout')
            channel.exchange_declare(exchange='pwrSweep', exchange_type='fanout')

            result = channel.queue_declare(queue='', exclusive=True)
            queue_name = result.method.queue

            # channel.queue_bind(exchange='freqSweep', queue=queue_name)
            channel.queue_bind(exchange='pwrSweep', queue=queue_name)
            channel.basic_consume(queue=queue_name, on_message_callback=self.rabbitCallback, auto_ack=True)
            channel.start_consuming()

    def rabbitCallback(self, ch, method, properties, body):
        """Callback method for rabbitMQ

        Args:
            ch ([type]): [description]
            method ([type]): [description]
            properties ([type]): [description]
            body (String): The message body as a string
        """

        data = body.split( )

        run = []

        for i in range(0, len(data), 2):
            run.append(int(int(data[i].decode()) / 1000000)) # converts freq to MHz
        
        # remove the oldest entry from the window and add this new one
        self.freqList.pop(0)
        self.freqList.append(run)

        #print(f"WindowSize: {str(len(self.freqList))} , run size: {str(len(run))}")

        self.digitalDetect() # run the detector on the new window

    def digitalDetect(self):
        """Method that contains the code to do digital detection, seperated for ease of use
        """

        freqSet = set() # set that will contain every unique freq in the window

        #fill the set with every unique freq
        for run in self.freqList:
            for freq in run:
                freqSet.add(freq)

        #print(f"Set length: {str(len(freqSet))}")

        counterList = [0] * len(freqSet) # list of freq counter corresponding to the freqSet

        # convert set to a list for easier mapping
        freqSet = list(freqSet)

        # count how often each freq occurs in the window
        for i in range(len(self.freqList)):
            for j in range(len(freqSet)):
                counterList[j] = counterList[j] + self.freqList[i].count(freqSet[j])

        digitalSignals = [] # list of validated digital signals

        # check each of the counters and compare them to the precentages we gave for digital signal detection
        for i in range(len(freqSet)):
            precent = float(counterList[i] / self.windowSize)

            if self.minPrecent <= precent and self.maxPrecent >= precent:
                #print(f"{str(freqSet[i])} : {str(precent)}")
                digitalSignals.append(freqSet[i])

        self.bundleDetections(digitalSignals)

    def bundleDetections(self, digitalSignals):
        """Bundles the digital signals based off of a given bandwidth

        Args:
            digitalSignals (List[(int)]): A list of the frequencies of detected digital signals
        """
        
        # lists of signal center freqs an bandwidths - this should probably become a custom object
        centerFreq = []
        bandwidth = []

        # helper varibles for calculating center freq
        startFreq = 0
        stopFreq = 0

        digitalSignals.sort() # order the list

        for freq in digitalSignals:
            if startFreq == 0: # start state
                startFreq = freq
            elif freq > startFreq and freq <= (startFreq + self.bandwidth): # freq is able to match with start freq
                stopFreq = freq
            else: # start new target bin
                # add old target to the list
                centerFreq.append(float(startFreq) + (float(stopFreq - startFreq) / 2))
                bandwidth.append(float(stopFreq - startFreq) + 1)

                #start new target
                startFreq = freq

        # at the end add the last unfinished target
        centerFreq.append(float(startFreq) + (float(stopFreq - startFreq) / 2))
        bandwidth.append(float(stopFreq - startFreq) + 1)


        '''
        for i in range(len(digitalSignals)):
            startFreq = digitalSignals[i]

            # checks for signals within bandwidth and removes them
            while (i+1) < len(digitalSignals) and ((digitalSignals[i+1] - startFreq) <= self.bandwidth):
                stopFreq = digitalSignals[i+1]
                i = i+1
            
            # updates the lists
            centerFreq.append(float(startFreq) + (float(stopFreq - startFreq) / 2))
            bandwidth.append(int(stopFreq - startFreq) + 1)
        '''
        for i in range(len(centerFreq)):
            print(f"Freq: {str(centerFreq[i])} : {str(bandwidth[i])} MHz Bandwidth")

        print(f"Total targets: {str(len(centerFreq))}")        



if __name__ == "__main__":

    print("Starting Digital Detector")

    dsd = Detector(20, 1.0, 0.2, 50)

    dsd.linkRabbit()