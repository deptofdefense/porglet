from falcon.messages.py import FalconApplicationMessages_pb2 as fam
import unittest

class TestFastSearchConfig(unittest.TestCase):
  def setUp(self):
    self.fsc = fam.FastSearchConfig()
  def testDefaults(self):
    self.assertTrue(self.fsc.msgName == 'FAST_SEARCH_CONFIG')
    self.assertTrue(self.fsc.pps == fam.FastSearchConfig.PPS_OFF)
    self.assertTrue(self.fsc.ref == fam.FastSearchConfig.REF_OFF)
    self.assertTrue(self.fsc.iffrq == 30e6)
    self.assertTrue(self.fsc.writeAux == 12)
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5

    ###
    # autoControl (enum:AutoControl)
    ###
    # set to HEADLESS (succeeds)
    self.fsc.autoControl = fam.FastSearchConfig.HEADLESS
    
    ###
    # pps (enum:PPS)
    ###
    # set to PPS_OFF (succeeds)
    self.fsc.pps = fam.FastSearchConfig.REF_OFF
    ###
    # ref (enum:Ref10m)
    ###
    # set to REF_OFF (succeeds)
    self.fsc.ref = fam.FastSearchConfig.PPS_OFF

    ###
    # iffrq (float)
    ###
    # set to float (succeeds)
    self.fsc.iffrq = test_float
  
    ###
    # writeAux (int32)
    ###
    # set to int (succeeds)
    self.fsc.writeAux = test_int
#///////////////////////////////////////////////////////////////////////////////
class TestProcMacroConfig(unittest.TestCase):
  def setUp(self):
    self.pmc = fam.ProcMacroConfig()
  def testDefaults(self):
    self.assertTrue(self.pmc.msgName == 'PROC_MACRO_CONFIG')
    self.assertTrue(self.pmc.pps == fam.FastSearchConfig.PPS_OFF)
    self.assertTrue(self.pmc.ref == fam.FastSearchConfig.REF_OFF)
    self.assertTrue(self.pmc.iffrq == 30e6)
    self.assertTrue(self.pmc.writeAux == 12)
  def testTypes(self):
    # create test types
    test_string = 'string'
    test_int    = 2
    test_float  = 2.5

    ###
    # autoControl (enum:AutoControl)
    ###
    # set to HEADLESS (succeeds)
    self.pmc.autoControl = fam.FastSearchConfig.HEADLESS
    
    ###
    # pps (enum:PPS)
    ###
    # set to PPS_OFF (succeeds)
    self.pmc.pps = fam.FastSearchConfig.REF_OFF
    ###
    # ref (enum:Ref10m)
    ###
    # set to REF_OFF (succeeds)
    self.pmc.ref = fam.FastSearchConfig.PPS_OFF

    ###
    # iffrq (float)
    ###
    # set to float (succeeds)
    self.pmc.iffrq = test_float
  
    ###
    # writeAux (int32)
    ###
    # set to int (succeeds)
    self.pmc.writeAux = test_int

#///////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
  unittest.main()
