import pickle # needed to read logs

freqList = []

#open the log file
try:
    f = open('logs/11freqLog.pkl', 'rb')
    print("Loading old Target List")
    freqList = pickle.load(f)
    #print(str(self.targetList))
    f.close()
except:
    print("Load file does not exist")


for freq in freqList:
    print(str(freq))