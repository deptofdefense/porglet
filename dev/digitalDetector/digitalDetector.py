import sys # needed for rabbit
import os # needed for file stuff
import time # needed for sleep
from threading import Thread # needed for threads

from sklearn.cluster import KMeans # needed for clustering
import numpy as np # needed for clustering

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
        """Method that contains the code to do digital detection, separated for ease of use
        """

        freqSet = set() # set that will contain every unique freq in the window

        #fill the set with every unique freq
        for run in self.freqList:
            for freq in run:
                freqSet.add(freq)

        print(f"Set length: {str(len(freqSet))}")

        # convert to numpy array
        data = np.array(list(freqSet))

        # do KMeans clustering
        kmeans = KMeans().fit(data.reshape(-1,1))
        kmeans.predict(data.reshape(-1,1))

        print(str(kmeans.labels_))
        


if __name__ == "__main__":

    print("Starting Digital Detector")

    dsd = Detector(20, 0.8, 0.2, 10)

    dsd.linkRabbit()