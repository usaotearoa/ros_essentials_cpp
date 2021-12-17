#!/usr/bin/env python

import rospy
from rospy.exceptions import ROSInterruptException
from std_msgs.msg import String


def talker():
    # create the publisher with topic 'chatter'.
    # this can also be a path, such as '/chatter/chat_msg'
    # String is the type of message, which has been imported
    # <from std_msgs.msg import String>
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # initialize the node, later with rosnode, this will
    # show as 'talker' node
    rospy.init_node('talker', anonymous=True)

    # rate at which to publish
    rate = rospy.Rate(1)

    i=0     # counter will be used in published text
    while not rospy.is_shutdown():
        # assemble message
        # other message types need to be instanciated
        # for example Image
        # img_msg = Image
        # img_msg.headr = ...
        # img_msg.data = ...
        # ...
        hello_str = "hello world %s" %i

        # add a log entry (optional)
        rospy.loginfo(hello_str)

        # publish the message
        pub.publish(hello_str)

        # delay with the rate
        rate.sleep()
        i=i+1



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass