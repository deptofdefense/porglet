from falcon.messages.py import FalconAntennaMessages_pb2 as fam
import unittest


class TestRotorStep(unittest.TestCase):
  def setUp(self):
    self.rotorStep = fam.RotorStep()
  def testDefaults(self):
    self.assertTrue(self.rotorStep.msgName == 'ROTOR_STEP')
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5
    
    ###
    # resID (string)
    ###
    # set as string
    self.rotorStep.resID = test_string

    ###
    # appID (int32)
    ###
    # set as int (succeeds)
    self.rotorStep.appID = test_int

    ###
    # azimuth (float)
    ###
    # set as float (succeeds)
    self.rotorStep.azimuth = test_float

    ### 
    # elevation (float)
    ###
    # set as float (succeeds)
    self.rotorStep.elevation = test_float
#///////////////////////////////////////////////////////////////////////////////
class TestQueryRotorPosition(unittest.TestCase):
  def setUp(self):
    self.qrp = fam.QueryRotorPosition()
  def testDefaults(self):
    self.assertTrue(self.qrp.msgName == 'QUERY_ROTOR_POSITION')
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5
    
    ###
    # resID (string)
    ###
    # set as string (succeeds)
    self.qrp.resID = test_string
#///////////////////////////////////////////////////////////////////////////////
class TestRotorPosition(unittest.TestCase):
  def setUp(self):
    self.rotorPos = fam.RotorPosition()
  def testDefaults(self):
    self.assertTrue(self.rotorPos.msgName == 'ROTOR_POSITION')
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5
    
    ###
    # resID (string)
    ###
    # set as string (succeeds)
    self.rotorPos.resID = test_string
    
    ###
    # azimuth (float)
    ###
    # set as float (succeeds)
    self.rotorPos.azimuth = test_float
    
    ###
    # elevation (float)
    ###
    # set as float (succeeds)
    self.rotorPos.elevation = test_float
    
#///////////////////////////////////////////////////////////////////////////////
class TestSwitchMap(unittest.TestCase):
  def setUp(self):
    self.switchMap = fam.SwitchMap()
  def testDefaults(self):
    self.assertTrue(self.switchMap.msgName == 'SWITCH_MAP')
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5
    
    ###
    # resID (string)
    ###
    # set as string (succeeds)
    self.switchMap.resID = test_string

    ###
    # appID (int32)
    ### 
    # set as int (succeeds)
    self.switchMap.appID = test_int

    ###
    # inputPort (int32)
    ###
    # set as int (succeeds)
    self.switchMap.inputPort = test_int
 
    ###
    # outputPort (int32)
    ###
    # set as int (succeeds)
    self.switchMap.outputPort = test_int
#///////////////////////////////////////////////////////////////////////////////
class TestQuerySwitchStatus(unittest.TestCase):
  def setUp(self):
    self.qss = fam.QuerySwitchStatus()
  def testDefaults(self):
    self.assertTrue(self.qss.msgName == 'QUERY_SWITCH_STATUS')
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5
    
    ###
    # resID (string)
    ###
    # set as string (succeeds)
    self.qss.resID = test_string
#///////////////////////////////////////////////////////////////////////////////
class TestSwitchStatus(unittest.TestCase):
  def setUp(self):
    self.switchStat = fam.SwitchStatus()
  def testDefaults(self):
    self.assertTrue(self.switchStat.msgName == 'SWITCH_STATUS')


    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5
    
    ###
    # resID (string)
    ###
    # set as string (succeeds)
    self.switchStat.resID = test_string

    ###
    # inputPorts (int32)
    ###
    # append int (succeeds)
    self.switchStat.inputPorts.append(test_int)
 
    ###
    # outputPorts (int32)
    ###
    # append int (succeeds)
    self.switchStat.outputPorts.append(test_int)
#///////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
  unittest.main()
