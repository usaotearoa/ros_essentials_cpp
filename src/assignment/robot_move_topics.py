#!/usr/bin/env python

import rospy
import math
from rospy.exceptions import ROSInterruptException
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

# =========================================================
# TASKS
# =========================================================
# 1.    create subscriber of topic that shows robot location
#           ->  /turtle1/pose
# 2.    create publisher that moves the robot
#           ->  /turtle1/cmd_vel
#           ->  geometry_msgs/Vector3 linear
#           ->  float64 x
#           ->  float64 y
#           ->  float64 z
#           ->  geometry_msgs/Vector3 angular
#           ->  float64 x
#           ->  float64 y
#           ->  float64 z

def move():
    velocity_message = Twist()
    velocity_message.linear.x = 1.0
    velocity_message.angular.x = -0.5
    
    loop_rate = rospy.Rate(1) # we publish the velocity at 10 Hz (10 times a second)    
    cmd_vel_topic='/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)


    for i in range(0,5):
        i=i+1
        rospy.loginfo("Turtlesim moves forwards")
        velocity_publisher.publish(velocity_message)

        loop_rate.sleep()
    
    # stop at the end
    velocity_message.linear.x = 0.0
    velocity_publisher.publish(velocity_message)

if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_motion_pose_own', anonymous=True)
        move()
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")