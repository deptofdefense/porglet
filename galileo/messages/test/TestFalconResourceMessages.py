from falcon.messages.py import FalconResourceMessages_pb2 as frm
import unittest

class TestPICConfig(unittest.TestCase):
  def setUp(self):
    self.picConf = frm.PICConfig()
  def testDefaults(self):
    self.assertTrue(self.picConf.msgName == 'PIC_CONFIG')
    self.assertTrue(self.picConf.host == 'local')
    self.assertTrue(self.picConf.fs == 100e6)
    self.assertTrue(self.picConf.minRF == 20e6)
    self.assertTrue(self.picConf.maxRF == 3000e6)
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5


    ###
    # channel (int32)
    ###
    self.picConf.channel = test_int
 
    ###
    # baseAux (int32)
    ###
    self.picConf.baseAux = test_int

    ###
    # rx (string)
    ###
    self.picConf.rx = test_string
  
    ###
    # pic (string)
    ###
    self.picConf.pic = test_string
   
    ###
    # picflags (string)
    ###
    self.picConf.picflags = test_string

    ###
    # picside (string)
    ###
    self.picConf.picside = test_string
  
    ###
    # host (string)
    ###
    self.picConf.host = test_string
    
    ###
    # fs (float)
    ###
    self.picConf.fs = test_float

    ###
    # minRF (float)
    ###
    self.picConf.minRF = test_float
    
    ###
    # maxRF (float)
    ###
    self.picConf.maxRF = test_float
#///////////////////////////////////////////////////////////////////////////////
class TestMMSConfig(unittest.TestCase):
  def setUp(self):
    self.mmsConf = frm.MMSConfig()
  def testDefaults(self):
    self.assertTrue(self.mmsConf.msgName == 'MMS_CONFIG')
    self.assertTrue(self.mmsConf.host == 'local')
    self.assertTrue(self.mmsConf.fs == 100e6)
    self.assertTrue(self.mmsConf.minRF == 20e6)
    self.assertTrue(self.mmsConf.maxRF == 3000e6)
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5

    ###
    # channel (int32)
    ###
    self.mmsConf.channel = test_int
  
    ###
    # baseAux (int32)
    ###
    self.mmsConf.baseAux = test_int
   
    ###
    # IP (string)
    ###
    self.mmsConf.IP = test_string

    ###
    # controlPort (int32)
    ###
    self.mmsConf.controlPort = test_int

    ###
    # dataPort (int32)
    ###
    self.mmsConf.dataPort = test_int

    ###
    # interfaceIP (string)
    ###
    self.mmsConf.interfaceIP = test_string

    ###
    # receiver (int32)
    ###
    self.mmsConf.receiver = test_int

    ###
    # host (string)
    ###
    self.mmsConf.host = test_string
    
    ###
    # fs (float)
    ###
    self.mmsConf.fs = test_float

    ###
    # minRF (float)
    ###
    self.mmsConf.minRF = test_float
    
    ###
    # maxRF (float)
    ###
    self.mmsConf.maxRF = test_float
#///////////////////////////////////////////////////////////////////////////////
class TestRFSwitchConfig(unittest.TestCase):
  def setUp(self):
    self.rfsc = frm.RFSwitchConfig()
  def testDefaults(self):
    self.assertTrue(self.rfsc.msgName == 'RFSWITCH_CONFIG')
    self.assertTrue(self.rfsc.IP == 'nportserver')
    self.assertTrue(self.rfsc.slaveTimeout == 180)
    self.assertTrue(self.rfsc.energyScanSec == 10)
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5

    ###
    # IP (string)
    ###
    self.rfsc.IP = test_string

    ###
    # slaveTimeout (int32)
    ###
    self.rfsc.slaveTimeout = test_int

    ###
    # energyScanSec (float)
    ###
    self.rfsc.energyScanSec = test_float
#///////////////////////////////////////////////////////////////////////////////
class TestAntennaConfig(unittest.TestCase):
  def setUp(self):
    self.antConf = frm.AntennaConfig()
  def testDefaults(self):
    self.assertTrue(self.antConf.msgName == 'ANTENNA_CONFIG')
    self.assertTrue(self.antConf.fixedAngle == -999)
    self.assertTrue(self.antConf.latitude == 0)
    self.assertTrue(self.antConf.longitude == 0)
    self.assertTrue(self.antConf.altitude == 0)
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5

    ###
    # minRF (float)
    ###
    self.antConf.minRF = test_float

    ###
    # maxRF (float)
    ###
    self.antConf.maxRF = test_float
   
    ###
    # fixedAngle (float)
    ###
    self.antConf.fixedAngle = test_float
  
    ###
    # latitude (float)
    ###
    self.antConf.latitude = test_float
 
    ###
    # longitude (float)
    ###
    self.antConf.longitude = test_float

    ###
    # altitude (float)
    ###
    self.antConf.altitude = test_float

#///////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
  unittest.main()
