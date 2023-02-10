import sys # needed for rabbit
import os # needed for file stuff
import time # needed for sleep
from threading import Thread # needed for threads

from sklearn.cluster import KMeans # needed for clustering
from sklearn.cluster import DBSCAN # needed for DBSCAN clustering
import numpy as np # needed for clustering
from sklearn.neighbors import NearestNeighbors # needed for helping find epsilon
from kneed import KneeLocator # needed for helping to find epsilon

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
            run.append(int(data[i].decode()) / 1000000.0) # grabs the frequency and converts to MHz
        
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

        #print(f"Set length: {str(len(freqSet))}")

        if len(freqSet) != 0: # set is not empty

            # convert to numpy array
            data = np.array(list(freqSet))

            # gets distance from all neighbours
            neighbors = NearestNeighbors(n_neighbors=11).fit(data.reshape(-1,1))
            distances, indices = neighbors.kneighbors(data.reshape(-1,1))
            distances = np.sort(distances[:,10], axis=0)

            # find knee point
            knee = KneeLocator(np.arange(len(distances)), distances, S=1, curve='convex', direction='increasing', interp_method='polynomial')
            #print(f"Knee Point: {str(distances[knee.knee])}")

            # use knee point to calculate clusters
            dbClusters = DBSCAN(eps=round((distances[knee.knee] / 2)), min_samples=10).fit(np.asarray(data.reshape(-1,1)))

            # Number of Clusters
            nClusters=len(set(dbClusters.labels_))-(1 if -1 in dbClusters.labels_ else 0)
            #print(str(nClusters))

            '''
            # variable to hold the cluster count
            clusterCount = 0
            # do KMeans clustering
            if len(freqSet) > round(distances[knee.knee]): # normal operation
                kmeans = KMeans(n_clusters=round(distances[knee.knee]), n_init='auto').fit(data.reshape(-1,1))
                kmeans.predict(data.reshape(-1,1))
                clusterCount = round(distances[knee.knee])
            else: # should only happen near the start of the scan
                kmeans = KMeans(n_clusters=int(len(freqSet)), n_init='auto').fit(data.reshape(-1,1))
                kmeans.predict(data.reshape(-1,1))
                clusterCount = len(freqSet)
            '''
            #print(str(kmeans.labels_))

            
            #convert from set to list for easy navigation
            freqSet = list(freqSet)

            # empty list to be populated with paired frequencies
            #clusterList = [ [] for _ in range(clusterCount) ]
            clusterList = [ [] for _ in range(nClusters) ]

            # pair all the frequencies of each cluster into a list
            for i in range(len(freqSet)):
                if dbClusters.labels_[i] != -1:
                    clusterList[int(dbClusters.labels_[i])].append(freqSet[i])

            # empty list to contain all the frequency and bandwidth pairs
            freqList = []
            
            #for i in range(clusterCount):
            for i in range(nClusters):
                centerFreq = sum(clusterList[i]) / len(clusterList[i]) # calc average
                bandWidth = max(clusterList[i]) - min(clusterList[i])

                freqList.append([centerFreq, bandWidth])
                #print(f"CF : {str(centerFreq)} BW: {str(bandWidth)} m: {str(min(clusterList[i]))} M: {str(max(clusterList[i]))}")
                


            print("")
            for x in freqList:
                print(f"Center Freq: {str(x[0])} BandWidth: {str(round(x[1]))}")

        
        
        else: # empty set, meaning sweeper not started, do nothing
            print("Empty set, no processing")
        


if __name__ == "__main__":

    print("Starting Digital Detector")

    dsd = Detector(60, 0.8, 0.2, 10)

    dsd.linkRabbit()