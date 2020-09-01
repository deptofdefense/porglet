# code for managing RF objects seen in big sweep

class RFObject:
    """ Base class for keeping track of RF detections seen during a big sweep """

    # initalization method
    def __init__(self, time, freq):
        self.startTime = str(time)
        self.endTime = str(time)
        self.minFreq = float(freq)
        self.maxFreq = float(freq)
        self.classification = "None"
        self.timeOut = 10

    def classifySignal(self, classification):
        """ Sets the signal classification """
        self.classification = str(classification)

    def resetTimeout(self):
        """ Resets the timeout counter """
        self.timeOut = 10

    def checkTimeout(self):
        """ decrements the timeout and returns true if still alive """

        self.timeOut = self.timeOut - 1

        if (self.timeOut > 0):
            return True
        else:
            return False

    def printDetection(self):

        msg = self.startTime + " " + self.endTime + " " + str(self.minFreq / 1000000) + " " + str(self.maxFreq / 1000000) + " " + self.classification

        return msg

    def updateDetection(self, time, freq, binSize):
        """ Updates the object, returns true if a match, false otherwise """

        # if frequency is within ranges, match
        if ((self.minFreq <= freq) and (self.maxFreq >= freq)):

            self.endTime = str(time)
            self.resetTimeout

            #print(self.printDetection())

            return True
        
        else:
            # if freq is within one bin, match
            # check lower first
            if ((self.minFreq - float(binSize)) <= freq) and (self.maxFreq >= freq):

                self.endTime = str(time)
                self.resetTimeout
                self.minFreq = self.minFreq - float(binSize)

                #print(str(self.minFreq) + " " + str(binSize))
                return True

            elif (self.minFreq <= freq) and ((self.maxFreq + float(binSize)) >= freq):
                self.endTime = str(time)
                self.resetTimeout
                self.maxFreq = self.maxFreq + float(binSize)
                
        return False