#!/usr/bin/env python

import rospy
import numpy as np
import cv2
import time
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

rospy.init_node('VideoPublisher', anonymous=True)

VideoRaw = rospy.Publisher('VideoRaw', Image, queue_size=10)
#NeedleBorder = rospy.Publisher('NeedleBorder', Image, queue_size=10)


# get parameter from launch file or cmd_line
stream_source = ""

if (stream_source == ''):
    stream_source = "/home/administrator/catkin_ws/src/ros_essentials_cpp/src/topic03_perception/video/tennis-ball-video.mp4"

cam = cv2.VideoCapture(stream_source)


#cam = cv2.VideoCapture('output.avi')

while cam.isOpened():
    meta, frame = cam.read()

    frame_gaus = cv2.GaussianBlur(frame, (5,5), 0)

    frame_gray = cv2.cvtColor(frame_gaus, cv2.COLOR_BGR2GRAY)

    #frame_edges = cv2.Canny(frame_gray, threshold1, threshold2)

    # I want to publish the Canny Edge Image and the original Image
    msg_frame = CvBridge().cv2_to_imgmsg(frame)
    #msg_frame_edges = CvBridge().cv2_to_imgmsg(frame_edges)

    VideoRaw.publish(msg_frame, "RGB8")
    #NeedleBorder.publish(msg_frame_edges, "mono8")

    time.sleep(1000)