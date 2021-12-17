#!/usr/bin/env python

import numpy as np
import cv2


image_name = "tree"

print("read an image from file")
color_image = cv2.imread("images/tree.jpg", cv2.IMREAD_COLOR)

print("Display image in native color")
cv2.imshow("Original image", color_image)
cv2.moveWindow("Original image", 0,0)
print(color_image.shape)

height,width,channels = color_image.shape

print ("split the image into three channels")
blue,green,red = cv2.split(color_image)

cv2.imshow("red channel", red)
cv2.moveWindow("red_channel", 0,height)

cv2.imshow("gree channel", green)
cv2.moveWindow("blue_channel", 0,height)

cv2.imshow("blue channel", blue)
cv2.moveWindow("blue_channel", 0,height)

print("split image int Hue, Saturation, Value channls")
hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_image = np.concatenate((h,s,v),axis=1)
cv2.imshow("Hue, Saturation, Value image", hsv_image)

print("--- convert image to grayscale ---")
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", gray_image)



cv2.waitKey(0)
cv2.destroyAllWindows()















