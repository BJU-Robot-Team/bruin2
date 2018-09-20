#!/usr/bin/env python

import compass_data
import compass_node
import ros_interface
from bruin2_msgs.msg import CompassDataMsg
import rospy
import os
import serial
import threading

def readSerial(my_serial):
    msg = my_serial.readline()
    if (len(msg) == 0):
        rospy.logwarn("Compass: serial.readline returned no data.")
    rospy.logdebug("Compass: got message {0} \n".format(msg))
    return msg

rospy.init_node('compass')
rospy.loginfo("Bruin-2 Compass V2.0 Starting")

ros_interface = ROSInterface()

port = "/dev/compass"
baud = 19200
fake_compass = False
raw_data = ""

try:
    my_serial = serial.Serial(port, baud, timeout=500)
except:
    rospy.logerr("Compass serial port open failed.")
    fake_compass = True

compass = CompassData(0)

manipulator = ManipulateData

if (fake_compass):
    rospy.logerr("Compass continuing with fake data (21.1 degrees)")
    raw_data = "$C21.1P-45.6R-163.4T20.5*27"

while (ros_interface.is_node_running()):

    if(!fake_compass):
        raw_data = readSerial(my_serial)

    comp_data = tester.parse_data(raw_data)

    ros_interface.publish_messages(comp_data)

    rospy.spin()
