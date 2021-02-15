import stomp
import os
import sys
import re
import logging
import json
import time
import Queue
import collections
from datetime import datetime

import messages.py.ServiceInfrastructureExclusive_pb2 as ex_msg


class ActiveMQListener(stomp.ConnectionListener):

    def __init__(self, msgbroker):
        self.messagebroker = msgbroker

    def on_connecting(self, host_and_port):
        print 'on_connecting %s %s' % host_and_port

    def on_error(self, headers, message):
        print 'recieved an error %s' %(headers, message)

    def on_message(self, headers, body):
        try:
            self.messagebroker.messageQueue.put_nowait((headers,body))
        except Queue.Full:
            self.clearQueue()

    def on_send(self, frame):
        print 'on_send %s %s %s' % (frame.cmd, frame.headers, frame.body)

    def on_connected(self, headers, body):
        print 'on_connected %s %s' % (headers, body)

    def on_disconnected(self):
        print 'ActiveMQListener was disconnected.'

    def on_before_message(self, headers, body):
        pass

    def clearQueue(self):
        while self.messagebroker.messageQueue.empty() == False:
            try:
                _, _ = self.messagebroker.messageQueue.get(timeout=1.0)
            except Queue.Empty:
                break
       


class Backend(object):
    def __init__(self, parent=None):
        #self(Backend, self).__init__()
        self.channelOfInterest = -1
        self.enabled = False
        self.frequency = 0.0
        self.activemqSender = True
        self.initActiveMQSender()
        self.messageQueue = Queue.Queue(maxsize=200)
        self.activemqReceive = True
        self.guid = 'rxCommander'
        self.messageList = ['placeholder']
        self.initActiveMQListener()
        
    def initActiveMQListener(self):
        try:
            #hostsAndPorts = (('172.17.0.2', 61613),)
            hostsAndPorts = (('172.17.0.1', 61613),)
            self.stompConnection = stomp.Connection()
            self.stompConnection.connect('admin', 'password', wait=True)
            self.activeMQListener = ActiveMQListener(self)
            self.stompConnection.set_listener('ActiveMQListener', self.activeMQListener)
            self.stompConnection.start()
        except Exception as e:
            self.activemqReceive = False
            print str(e)

    def subscribeToResponseTopic(self):
        self.stompConnection.subscribe('/topic/public.receiver_response', id=47, ack='auto', auto_content_length=True)
        time.sleep(1)

    def subscribeToDwellTopic(self):
        self.stompConnection.subscribe('/topic/public.receiver_command', id=47, ack='auto', auto_content_length=True)
        time.sleep(1)

    def unsubscribeToTopic(self):
        self.stompConnection.unsubscribe(47)
        while self.messageQueue.empty() == False:
            try:
                header, body = self.messageQueue.get_nowait()
            except Queue.Empty:
                print "hello world"
                break


    def disconnectActiveMQConnection(self):
        self.stompConnection.disconnect()
        self.activemqReceive = False
        print "ActiveMQ Connection has been disconnected"


    def __readQueue(self):
        while self.activemqReceive:
            try:
                header, body = self.messageQueue.get_nowait()
            except Queue.Empty:
                continue
            timestamp = datetime.utcfromtimestamp(float(header['timestamp']) / 1000.0)
            if self.enabled == False:
                try:
                    newmsg = ex_msg.RadioControlResponseTopic.FromString(body).rx_command_response
                    if int(newmsg.channel) == self.channelOfInterest and newmsg.enabled == bool(self.enabled):
                        rxLine = 'channel ' + str(newmsg.channel) + ' freq ' + str(newmsg.frequency) + ' gain ' + str(newmsg.gain) + ' enable command ' + str(bool(self.enabled)) 
                        self.setNewMessage(rxLine)
                        self.unsubscribeToTopic()
                        break
                    else:
                        continue
                except Exception as e:
                    print str(e)
            elif self.enabled == True:
                try:
                    newmsg = ex_msg.RadioControlResponseTopic.FromString(body).rx_command_response
                    if int(newmsg.channel) == self.channelOfInterest:
                        rxLine = 'channel ' + str(newmsg.channel) + ' freq ' + str(newmsg.frequency) + ' gain ' + str(newmsg.gain) + ' enable command ' + str(bool(self.enabled)) 
                        self.setNewMessage(rxLine)
                        self.unsubscribeToTopic()
                        break
                    else:
                        continue
                except Exception as e:
                    print str(e)         


    def initActiveMQSender(self):
        try:
            self.conn = stomp.Connection(auto_content_length=True)
            self.conn.connect('admin', 'password', wait=True)
            self.conn.start()
        except Exception:
            self.activemqSender = False

    def sendMessage(self, serializedMsg, topic):
        """
        provides a generic stomp connection sender which can be used for any topic that the
        user wishes to send out to.
        """
        contentLength = len(serializedMsg)
        destination = '/topic/'+str(topic)
        self.conn.send(body=serializedMsg, headers={ 'content-length': contentLength}, destination=destination, id=42)
        print("message sent!")
        self.subscribeToResponseTopic()

        time.sleep(4)
        self.__readQueue()
            
    def setUpRxCommandRequest(self, channel, frequency, gain, enabled):
        """
        Called once the send button is pressed on the GUI, the function
        takes in the parameters and sets up the protobuf message
        """
        self.channelOfInterest = int(channel)
        self.enabled = bool(enabled)
        self.frequencyOfInterest = float(frequency)
        exmsg = ex_msg.RadioControlRequestTopic()
        exmsg.rx_command_request.channel = int(channel)
        exmsg.rx_command_request.frequency = float(frequency)
        exmsg.rx_command_request.gain = int(gain)
        exmsg.rx_command_request.priority = 98
        exmsg.rx_command_request.guid = self.guid
        exmsg.rx_command_request.enabled = bool(enabled)
        serializedMsg = exmsg.SerializeToString()
        topic = 'public.receiver_command'
        self.sendMessage(serializedMsg, topic)

    def setNewMessage(self, message):
        """
        Adds the new message to a list for the frontend to read from
        """
        self.messageList.append(message)

    def getNewMessage(self):
        """
        Getter for the front end to read the message list
        """
        return self.messageList

#if __name__ == '__main__':
    #be = Backend()
    #be.setUpRxCommandRequest(1, 435, 30, 1)
    #time.sleep(4)
    #be.setUpRxCommandRequest(1, 435, 30, 0)

    #sys.exit(app.exec_())
