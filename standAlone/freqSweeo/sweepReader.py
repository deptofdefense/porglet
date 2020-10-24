import pickle # needed to read logs
import matplotlib.pyplot as plt # needed for graphs
import numpy as np # needed for graph


class RFTarget:

    def __init__(self, freq):
        self.freq = freq
        self.count = 1

    def match(self, freq):
        if self.freq == freq:
            self.count = self.count + 1
            return True
        else:
            return False






freqList = []
tempList = []

count = 0
matched = False

while True:
    #open the log file
    try:
        f = open(f'logs/{count}freqLog.pkl', 'rb')
        print(f"loading logs/{count}freqLog.pkl")
        tempList = pickle.load(f)
        #print(str(self.targetList))

        for temp in tempList:
            matched = False

            for freq in freqList:

                if freq.match(temp):
                    matched = True
                    break
            
            if not matched:
                freqList.append(RFTarget(temp))


        f.close()
        count = count + 1
    except:
        print(f"Reached end of log files at: {count-1}")
        break

print("out of loop")
print(f'Freq list size: {str(len(freqList))}')

plotFreq = []
plotCount = []

for freq in freqList:
    plotCount.append(freq.count)
    plotFreq.append(int(freq.freq)/1000000)

    #print(f'Freq: {str(int(freq.freq)/1000000)} : {str(freq.count)}')

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.bar(plotFreq, plotCount)  # Plot some data on the axes.

plt.show()

input("Press Enter to continue...")