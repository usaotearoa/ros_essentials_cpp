#! /usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

VERBOSE=True

bridge = CvBridge()

# ===============================================
# MAIN
# ===============================================
def main(args):
    rospy.init_node('video_stream', anonymous=True)

    image_publisher = rospy.Publisher("/output/image_raw/stream", Image, queue_size=10)
    video_capture = cv2.VideoCapture('../video/ros.mp4')
    width  = video_capture.get(3)  # float `width`
    height = video_capture.get(4)  # float `height`
    
    if VERBOSE:
        print("initiated node and publisher")
    
    while not rospy.is_shutdown():
        try:
            ret, frame = video_capture.read()
            #cv_image = bridge.imgmsg_to_cv2(frame, "bgr8")

            vmsg = Image
            vmsg.header = rospy.Time.now()
            vmsg.height = height
            vmsg.width = width
            vmsg.encoding = "rgb8"
            vmsg.is_bigendian = True
            vmsg.step = 3
            vmsg.data = frame


            # Publish new image
            image_publisher.publish(vmsg)

        except KeyboardInterrupt:
            break
            print("Shutting down")    
    
    # </while>
    cv2.destroyAllWindows()

    return 0


if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Shutting down")





















# #bridge = CvBridge()

# # ===============================================
# # MAIN
# # ===============================================
# def main():
#     rospy.init_node('image_converter', anonymous=True)

#     img_msg = Image

#     image_topic = "/video_stream/live"
#     img_publisher = rospy.Publisher(image_topic, Image, queue_size=10)
#     # get parameter from launch file or cmd_line
#     stream_source = ""

#     if (stream_source == ''):
#         stream_source = "/home/administrator/catkin_ws/src/ros_essentials_cpp/src/topic03_perception/video/tennis-ball-video.mp4"
    
#     video_capture = cv2.VideoCapture(stream_source)


#     while not rospy.is_shutdown():
#         try:
#             ret, imgfile = video_capture.read()

#             img_msg.data = imgfile
            
#             # show the image
#             # cv2.imshow("Frame",imgfile)
#             # if cv2.waitKey(25) & 0xFF == ord('q'):
#             #     break

#             # publish
#             img_publisher.publish(img_msg)


#         except KeyboardInterrupt:
#             break
#             print("Shutting down")
#     # </while>
#     video_capture.release()
#     cv2.destroyAllWindows()

#     return 0


# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("Shutting down")