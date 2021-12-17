#! /usr/bin/env python

import numpy as np
import cv2
import imutils

image = cv2.imread("images/tennisball03.jpg")
cv2.imshow("Original", image)

# convert image from RGB to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV image", hsv)

# find upper and lower limit of yellow color
yellowLower = (30, 150, 100)
yellowUpper = (50, 255,255)

# define mask using lower and upper color limits declared previously
mask = cv2.inRange(hsv, yellowLower, yellowUpper)

cv2.imshow("masked", mask)


cv2.waitKey(0)
cv2.destroyAllWindows()