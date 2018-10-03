#!/usr/bin/env python

# ------------------------------------------------------------
# ROS interface that handles publishing and receiving messages
# ------------------------------------------------------------
from bruin2_msgs.msg import CompassDataMsg
import compass_data
import rospy
import serial

class ROSInterface:
    def __init__(self):
        self.pub = rospy.Publisher("CompassData", CompassDataMsg, queue_size=10)

    #def is_node_running(self):
     #   return ok()

    def publish_messages(self, compass_data):
        message = CompassDataMsg

        message.heading = compass_data.heading
        message.pitch = compass_data.pitch
        message.roll = compass_data.roll
        message.temperature = compass_data.temperature

        self.pub.publish(message)
