#!/usr/bin/env python

import sys
import rospy
from ros_essentials_cpp.srv import RectangleAreaService
from ros_essentials_cpp.srv import RectangleAreaServiceRequest
from ros_essentials_cpp.srv import RectangleAreaServiceResponse

def rectangle_area_client(x, y):
    rospy.wait_for_service('calc_rect_area')
    try:
        calc_rect_area = rospy.ServiceProxy('calc_rect_area', RectangleAreaService)
        resp1 = calc_rect_area(x, y)
        return resp1
    except rospy.ServiceException(e):
        print ("Service call failed: %s"%e)

def usage():
    return 

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print ("%s [x y]"%sys.argv[0])
        sys.exit(1)
    print ("Requesting %s*%s"%(x, y))
    s = rectangle_area_client(x, y)
    print ("%s * %s = %s"%(x, y, s))
