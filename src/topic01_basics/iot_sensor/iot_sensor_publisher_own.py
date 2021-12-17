#!/usr/bin/env python

import rospy
from ros_essentials_cpp.msg import IoTSensor
import random

# create new publisher
pub = rospy.Publisher('iot_sensor_topic', IoTSensor, queue_size=10)

# initialize the node
rospy.init_node('iot_sensor_publisher_node', anonymous=True)

# set loop rate
rate =rospy.Rate(10.0)

# publish until terminated
i = 0
while not rospy.is_shutdown():
    iot_sensor = IoTSensor()
    iot_sensor.id = 1
    iot_sensor.name = "iot_parking_01"
    iot_sensor.temperature = 24.33 + (random.random()*2)
    iot_sensor.humidity = 33.41 + (random.random()*2)
    rospy.loginfo("I publish")
    rospy.loginfo(iot_sensor)
    pub.publish(iot_sensor)
    #rate.sleep()
    i=i+1
    
    