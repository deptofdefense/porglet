import subprocess # needed for hackrf sweep

from rfObject import RFObject # needed for detection tracking
from classifier import ClassifiedFreq # nedded fir ckassifier

import sys # needed for file stuff
import os # needed for file stuff

# set up classifier list
targetList = []

with open('class.txt', 'r') as fp:
    for line in fp:
        temp = line.split()
        targetList.append(ClassifiedFreq(temp[0], temp[1], temp[2]))


bigSweep = subprocess.Popen(["hackrf_sweep", "-f 400:6000", "-w 1000000"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

# the read time of the sweep
readTime = ""

# the start frequency
startFrq = 0

# the detection list
detectList = []

# noiseFloor
noiseFloor = float(-50)

# loops through the big sweep output
while True:
    try:

        splitStr = bigSweep.stdout.readline().split(", ")

        noiseFloor = ((100 * noiseFloor) + float(splitStr[6]) + float(splitStr[7]) + float(splitStr[8]) + float(splitStr[9]) + float(splitStr[10]))/105

        binSize = float(splitStr[4])

        # check if each of the db are above the noise floor
        # Hz Low + 0
        if (float(splitStr[6]) >= (noiseFloor + 10)):
            found = False
            readTime = splitStr[0] + " " + splitStr[1]
            startFrq = float(splitStr[2]) + (0 * binSize)

            for detect in detectList:
                found = detect.updateDetection(readTime, startFrq, binSize)

                if found: 
                    break
            
            if not found:
                detectList.append(RFObject(readTime, startFrq))

        # Hz Low + 1
        if (float(splitStr[7]) >= (noiseFloor + 10)):
            found = False
            readTime = splitStr[0] + " " + splitStr[1]
            startFrq = float(splitStr[2]) + (1 * binSize)

            for detect in detectList:
                found = detect.updateDetection(readTime, startFrq, binSize)

                if found: 
                    break
            
            if not found:
                detectList.append(RFObject(readTime, startFrq))

        # Hz Low + 2
        if (float(splitStr[8]) >= (noiseFloor + 10)):
            found = False
            readTime = splitStr[0] + " " + splitStr[1]
            startFrq = float(splitStr[2]) + (2 * binSize)

            for detect in detectList:
                found = detect.updateDetection(readTime, startFrq, binSize)

                if found: 
                    break
            
            if not found:
                detectList.append(RFObject(readTime, startFrq))

        # Hz Low + 3
        if (float(splitStr[9]) >= (noiseFloor + 10)):
            found = False
            readTime = splitStr[0] + " " + splitStr[1]
            startFrq = float(splitStr[2]) + (3 * binSize)

            for detect in detectList:
                found = detect.updateDetection(readTime, startFrq, binSize)

                if found: 
                    break
            
            if not found:
                detectList.append(RFObject(readTime, startFrq))

        # Hz Low + 4
        if (float(splitStr[10]) >= (noiseFloor + 10)):
            found = False
            readTime = splitStr[0] + " " + splitStr[1]
            startFrq = float(splitStr[2]) + (4 * binSize)

            for detect in detectList:
                found = detect.updateDetection(readTime, startFrq, binSize)

                if found: 
                    break
            
            if not found:
                detectList.append(RFObject(readTime, startFrq))

        # prune list by merging contacts
        counter = 0
        prevDetect = RFObject("0",0)
        detectList.reverse()
        for detect in detectList:

            for target in targetList:
                if target.checkSignal(detect.minFreq, detect.maxFreq):
                    detect.classifySignal(target.label)
                    break

            if (detect.updateDetection(prevDetect.endTime, prevDetect.minFreq, binSize) and detect.updateDetection(prevDetect.endTime, prevDetect.maxFreq, binSize)):
                detectList.pop(counter)
                counter = counter - 1

            prevDetect = detect
            counter = counter + 1
            
        detectList.reverse()

        # display to screen:
        print("\n\n")
        for detect in detectList:
            print(detect.printDetection())

    except(KeyboardInterrupt, SystemExit):
        bigSweep.kill()
        raise