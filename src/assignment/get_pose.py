#!/usr/bin/env python

import rospy
#import math
#from rospy.exceptions import ROSInterruptException
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def poseCallback(pose_message):
    x= pose_message.x
    y= pose_message.y
    yaw = pose_message.theta

    #task 4. display the x, y, and theta received from the message
    print ("turtle position:")
    print ('x: ',x)
    print ('y: ', y)
    print ('yaw: ', yaw)     


if __name__ == '__main__':
    try:
        # init the node
        rospy.init_node('turtlesim_motion_pose', anonymous=True)        
        #task 2. subscribe to the topic of the pose of the Turtlesim
        pose_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(pose_topic, Pose, poseCallback) 

        #task 3. spin
        rospy.spin()    
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")