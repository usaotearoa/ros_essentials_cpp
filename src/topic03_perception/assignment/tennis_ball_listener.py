#!/usr/bin/env python3

 
# Import the necessary libraries
import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
 
def callback(data):
 
  # CvBridge conversion ROS <-> OpenCV images
  br = CvBridge()
 
  # debug info
  rospy.loginfo("receiving video frame")
   
  # Convert ROS Image message to OpenCV image
  current_frame = br.imgmsg_to_cv2(data)
   
  # Display image
  cv2.imshow("camera", current_frame)
   
  cv2.waitKey(1)
      
def receive_message():
 
  # init node with name video_sub_py
  # Anonymous = True makes sure the node has a unique name.
  rospy.init_node('tennis_ball_listener', anonymous=True)
   
  # subscriber to tennis_ball_image topic
  rospy.Subscriber('tennis_ball_image', Image, callback)
 
  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()
 
  # Close down the video stream when done
  cv2.destroyAllWindows()
  
if __name__ == '__main__':
  receive_message()