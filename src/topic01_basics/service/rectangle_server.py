#!/usr/bin/env python

from ros_essentials_cpp.srv import RectangleAreaService
from ros_essentials_cpp.srv import RectangleAreaServiceRequest
from ros_essentials_cpp.srv import RectangleAreaServiceResponse

import rospy

def handle_rectangle_area(req):
    print ("Returning [%s * %s = %s]"%(req.a, req.b, (req.a * req.b)))
    return RectangleAreaServiceResponse(req.a * req.b)

def rectangle_area_server():
    rospy.init_node('rectangle_area_server')
    s = rospy.Service('calc_rect_area', RectangleAreaService, handle_rectangle_area)
    print ("Ready to calc rectangle.")
    rospy.spin()
    
if __name__ == "__main__":
    rectangle_area_server()
