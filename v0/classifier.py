# code for managing possible RF classifications

class ClassifiedFreq:
    """ Base class for keeping track of possible classifications """

    def __init__(self, startFreq, endFreq, label):

        self.minFreq = float(startFreq) * 1000000
        self.maxFreq = float(endFreq) * 1000000
        self.bandwidth = self.maxFreq - self.minFreq
        self.label = str(label)

    def checkSignal(self, startFreq, endFreq):
        if ((self.minFreq <= float(startFreq)) and (self.maxFreq >= float(endFreq))):
            return True
        else:
            return False

