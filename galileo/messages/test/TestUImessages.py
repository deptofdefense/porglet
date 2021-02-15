###########################################################
##       Keler to UI and UI to Kepler message tests      ##
###########################################################

#python imports
import sys, json, os, time, uuid, datetime
import xml.etree.ElementTree as ET
from threading import Thread

#imports for messaging
from kepler.messaging.pools.SubscriptionPool import SubscriptionPool as sf
import falcon.messages.py.FalconExternalsMessages_pb2 as ext_msg
import falcon.messages.py.FalconRemotingMessages_pb2 as rem_msg
import falcon.messages.py.KeplerUIConnectionMessages_pb2 as ui_msg

import control.common.MessagingSupport as messaging
from control.services.ServiceGeneric import ServiceGeneric
import control.messages.py.ServiceMessages_pb2 as svc_msg
import falcon.messages.py.ThunderbirdMessages_pb2 as tb_msg

import control.messages.py.CoordinationMessages_pb2 as coord_msg

from threading import Thread
import ast
import subprocess
import logging
import uuid
import datetime

#imports for messaging
from kepler.messaging.pools.SubscriptionPool import SubscriptionPool as sf
import falcon.messages.py.KeplerUIConnectionMessages_pb2 as ui_msg
from control.services.QServiceGeneric import QServiceGeneric
from PyQt4.QtCore import *
import signal

from PyQt4.QtCore import *
import signal


class MessageSender(QThread):

    xmlConfigFile = 'config.xml'

    def __init__(self, app, listener):

        self.app = app
        self.listener = listener

        QThread.__init__(self)

        self.connectID = "none"

        self.coordSub = sf().GetSubscription('Coordination')

    def run(self):
        #self.sendExternalsHit()
        #self.sendMessages()
        self.sendEWCeaseBuzzer()
        #self.sendCoordinationResponse()
        #print '\n--------------------------- sending signal event -------------------\n'
        #self.sendSignalEvent()
        #print '\n-------------------------- send EW status ----------------------\n'
        self.sendEWstatus()
        time.sleep(1)
        self.listener.running = False
        self.app.quit()

    def sendSignalEvent(self):

        self.sigSub = sf().GetSubscription('SignalEvents')

        msg = rem_msg.SignalEvent()

        msg.eventType = 1 # for sig up
        msg.scrypt = "wrongTESTMACRO"
        msg.channel = 1
        msg.eventID = str(uuid.uuid4())
        msg.timestamp = str(datetime.datetime.now())
        msg.soiNum = "720"
        msg.rfMHz = 2440.0
        msg.antAz = 0
        msg.antEl = 0
        msg.globalID = str(uuid.uuid4())

        print 'msg:', str(msg)
        self.sigSub.sendMessage(msg)

        return

        time.sleep(5)

        msg = rem_msg.SignalEvent()

        msg.eventType = 1 # for sig up
        msg.scrypt = "TESTMACRO"
        msg.channel = 1
        msg.eventID = str(uuid.uuid4())
        msg.timestamp = str(datetime.datetime.now())
        msg.soiNum = "720"
        msg.rfMHz = 2440.0
        msg.antAz = 0
        msg.antEl = 0
        msg.globalID = str(uuid.uuid4())

        print 'msg:', str(msg)
        self.sigSub.sendMessage(msg)

    def sendCoordinationResponse(self):
        print 'sending coordination response message'
        msg = coord_msg.CoordinationResponse()
        #fill out the response message
        msg.senderName = "QAppTestMacro"
        msg.localHost = "localhost"
        msg.controlHost = "localhost"
        msg.processType = "APP"
        msg.freq = 2440.0
        self.coordSub.sendMessage(msg)


    def sendMessages(self):

        mailbox = sf().GetSubscription("KeplerToUi")
        msg = ui_msg.UIAck()
        mailbox.sendMessage(msg)
        msg = ui_msg.ICDVersionResponse()
        mailbox.sendMessage(msg)
        msg = ui_msg.DBVersionResponse()
        mailbox.sendMessage(msg)
        print 'sending ext hit'
        self.sendExternalsHit()
        print 'sending cease buzzer'
        self.sendEWCeaseBuzzer()
        print 'sending coordination query'
        self.sendCoordinationQuery()
        print 'msg:', str(msg)

    def sendEWstatus(self):
        print 'sending EW status'
        mailbox = sf().GetSubscription("KeplerToUi")

        msg = ui_msg.EWStatus()

        outchan = msg.outputChannelStatus.add()
        outchan.effect == "hopjam"
        outchan.transmitFreq == 440.0
        outchan.globalId == str(uuid.uuid4())
        outchan.antenna == 0
        outchan.state == 0
        outchan.resID == str(uuid.uuid4())
        outchan.signalName == 'RMILEC'
        #output_channel_status = []

        msg.timestamp = str(datetime.datetime.now())

        '''
        for i in range(0, len(msg.outputChannelStatus)):

            #addstat = ui_msg.OutputChannelStatus()

            addstat = msg.outputChannelStatus[i].effect
            addstat = ui_msg.outputChannelStatus[i].transmitFreq
            addstat = ui_msg.outputChannelStatus[i].globalId
            addstat = ui_msg.outputChannelStatus[i].antenna
            addstat = ui_msg.outputChannelStatus[i].resID
            addstat = ui_msg.outputChannelStatus[i].signalName

            output_channel_status.append(addstat)

        msg.outputChannelStatus.extend(output_channel_status)

        msg.effect = 'hopjam'
        msg.transmitFreq = 440.0
        msg.globalId = str(uuid.uuid4())
        msg.antenna = 0
        msg.state = 2
        msg.resID = str(uuid.uuid4())
        msg.signalName = 'RMILEC'
        '''
        print 'msg:', str(msg)
        print 'msg: outstat', str(msg.outchan)
        mailbox.sendMessage(msg)

    def sendCoordinationQuery(self):
        msg = coord_msg.CoordinationQuery()
        coordBox = sf().GetSubscription('Coordination')
        coordBox.sendMessage(msg)

    def sendExternalsHit(self):
        outBox = sf().GetSubscription('ExtHits')
        msg = ext_msg.ExternalsHit()
        msg.threatType = 0
        msg.freqMHz = 2440.0
        msg.globalId = "stuff"
        msg.psuedoUniqueId = 1
        msg.timestamp = "timestamp"
        msg.name = "analogvideo"
        outBox.sendMessage(msg)

    def sendEWCeaseBuzzer(self):
        outBox = sf().GetSubscription('EWRequest')
        msg = tb_msg.EWCeaseBuzzer()
        outBox.sendMessage(msg)


class Listener(QThread):

    def __init__(self):

        QThread.__init__(self)
        self.running = True

    def onMessage(self, msg):
        print "got message", str(msg.msgName)

    def run(self):

        while (self.running):
            try:
                time.sleep(.05)
            except:
                print '\nexception running'
                self.running = False


if __name__ == '__main__':

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QCoreApplication(sys.argv)
    # Create the class to manage the service

    listener = Listener()
    listener.start()

    test = MessageSender(app, listener)
    test.start()

    # Run the actual service
    app.exec_()
    sys.exit()
