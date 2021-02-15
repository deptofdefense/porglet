from falcon.messages.py import FalconTriggerMessages_pb2 as ftm
import unittest

class TestIntercept(unittest.TestCase):
  def setUp(self):
    self.intercept = ftm.Intercept()
  def testDefaults(self):
    self.assertTrue(self.intercept.msgName    == 'INTERCEPT')
    self.assertTrue(self.intercept.isTrigger  == True)
    self.assertTrue(self.intercept.azimuth    == 0)
    self.assertTrue(self.intercept.elevation  == 0)
    self.assertTrue(self.intercept.snr        == 0)
    self.assertTrue(self.intercept.searchTier == 1)
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5

    ###
    # isTrigger (bool)
    ###
    self.intercept.isTrigger = True

    ###
    # signal (string)
    ###
    self.intercept.signal = test_string
    ###
    # frequency (float)
    ###
    self.intercept.frequency = test_float
    ###
    # bandwidth (float)
    ###
    self.intercept.bandwidth = test_float
    ###
    # receiver (string)
    ###
    self.intercept.receiver = test_string
    ###
    # antenna (string)
    ###
    self.intercept.antenna = test_string
    ###
    # azimuth (float)
    ###
    self.intercept.azimuth = test_float
    ###
    # elevation (float)
    ###
    self.intercept.elevation = test_float
    ###
    # snr (float)
    ###
    self.intercept.snr = test_float
    ###
    # timestamp (string)
    ###
    self.intercept.timestamp = test_string
    ###
    # searchScrypt (string)
    ###
    self.intercept.searchScrypt = test_string
    ###
    # searchTier (int32)
    ###
    self.intercept.searchTier = test_int
#///////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
  unittest.main()
