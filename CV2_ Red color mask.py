# Only Red color detection

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    low_red = np.array([161, 155, 84]) # lowest hue would be - 161,155,84( how do i found this i tested before and found this) 
    high_red = np.array([179, 255, 255])
    #mask = cv2.inRange(hsv_frame, low_red, high_red) 
        
    red_mask = cv2.inRange(hsv_frame, low_red, high_red) #we create maskk on hsv frame and then low red or high red
    red = cv2.bitwise_and(frame, frame, mask=red_mask)  # This keeps only the red-colored areas from the original image. Everything else becomes black.


    cv2.imshow("Frame", frame) 
    #cv2.imshow('Red mask', mask) 
    cv2.imshow('Red', red)
    
    
    key = cv2.waitKey(1)
    if key ==27:
        break

'''
Why HSV?

    Because:

        Hue = actual color
        Saturation = how pure is the color
        Value = brightness

HSV makes color detection much easier than BGR/RGB.

'''