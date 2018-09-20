#!/usr/bin/env python

# ------------------------------------------------------------
# ROS interface that handles publishing and receiving messages
# ------------------------------------------------------------
import CompassDataMsg
import compass_data
import rospy
import serial

class ROSInterface:
    def __init__():
        self.pub = rospy.Publisher("CompassData", CompassDataMsg, queue_size=10)

    def is_node_running():
        return ok()

    def publish_messages(compass_data):
        if ok():
            message = CompassDataMsg

            message.heading = compass_data.heading
            message.pitch = compass_data.pitch
            message.roll = compass_data.roll
            message.temperature = compass_data.temperature

            pub.publish(message)
