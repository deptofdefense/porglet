from falcon.messages.py import FalconServiceMessages_pb2 as fsm
import unittest

class TestCharManConfig(unittest.TestCase):
  def setUp(self):
    self.cmc = fsm.CharManConfig()
  def testDefaults(self):
    self.assertTrue(self.cmc.msgName == 'CHAR_MAN_CONFIG')
    self.assertTrue(self.cmc.xtalkCharReq == 'char_request')
    self.assertTrue(self.cmc.xtalkCharAns == 'char_result')
    self.assertTrue(self.cmc.snapExtraCount == 1)
    self.assertTrue(self.cmc.outputPath == '19')
    self.assertTrue(self.cmc.esiCount == 6)
    self.assertTrue(self.cmc.videoRateFFTSize == 131072)
    self.assertTrue(self.cmc.videoRateDCHz == 100)
    self.assertTrue(self.cmc.videoRateMaxFFT == 64)
    self.assertTrue(self.cmc.videoRateThresh == 2.25)
    
#///////////////////////////////////////////////////////////////////////////////
class TestFalconVisionConfig(unittest.TestCase):
  def setUp(self):
    self.fvc = fsm.FalconVisionConfig()
  def testDefaults(self):
    self.assertTrue(self.fvc.msgName == 'FALCON_VISION_CONFIG')
#///////////////////////////////////////////////////////////////////////////////
class TestGPSMonitorConfig(unittest.TestCase):
  def setUp(self):
    self.gmc = fsm.GPSMonitorConfig()
  def testDefaults(self):
    self.assertTrue(self.gmc.msgName == 'GPS_MONITOR_CONFIG')

#///////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
  unittest.main()

