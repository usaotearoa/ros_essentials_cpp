#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# create the callback message which will be called when a message of topic 'chatter'
# has been received
# this can also be a path, such as '/chatter/chat_msg'
# String is the type of message, which has been imported
# <from std_msgs.msg import String>
def chatter_callback(message):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)



def listener():
    # initialize the node, later with rosnode, this will
    # show as 'listener' node
    rospy.init_node('listener', anonymous=True)

    # create the subscriber to topic, define message type and callback function
    rospy.Subscriber("chatter", String, chatter_callback)

    # spin in circles
    rospy.spin()
    

if __name__ == '__main__':
    listener()



    