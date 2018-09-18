#!/usr/bin/env python

import rospy
from bruin2_msgs.msg import CameraDataMsg
import os
import cv2
import numpy

rospy.init_node('camera')
rospy.loginfo("Bruin-2 Sample Camera Driver 1.0 Starting")

def sendMsg(tracking, direction, distance):
    pub.publish(tracking, direciton, distance)

pub = rospy.Publisher("CameraData", CameraDataMsg, queue_size=10)

# publish a message every second
rospy.Timer(rospy.Duration(1), sendMsg)
rospy.spin()
