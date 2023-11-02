import cv2
import numpy as np
import time
import datetime

cap = cv2.VideoCapture ('bottesting.mkv')

count1 = 0
count2 = 0
count3 = 0
count4 = 0


def CarDetect():
    global count1
    global count2
    global count3
    global count4

    for contour in contours:
        area = cv2.contourArea (contour)

        (x, y, w, h) = cv2.boundingRect (contour)

        cv2.rectangle (frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        centroid = get_centroid (x, y, w, h)
        centroidX = centroid[0]
        centroidY = centroid[1]

        # def countingcar(centroidX,centroidY):

        if (720 < centroidX < 810 and 485 < centroidY < 500 and area > 300):

            count1 = count1 + 1
            if (count1 == 2):
                print("STOP")
                # stop

        elif (710 < centroidX <785  and 180 < centroidY < 195 and area > 300):
            count2 = count2 + 1
            if (count2 == 1):
                print ("STOP")
                # Stop and then turn right

        elif (855 < centroidX < 870 and 50 < centroidY < 100 and area > 300):
            count3 = count3 + 1
            if (count3 == 2):
                print ("STOP")
                #stop and make a left turn

        elif (1125 < centroidX < 1140 and 40 < centroidY < 90 and area > 300):
            count4 = count4 + 1
            if (count4 == 1):
                print("STOP")
                # Stop, drop the load and  then turn around

        # elif(500<centroidX<600 and 480<centroidY<500):
        # count3 = count3 + 1
        # print(count3)

        # elif(700<centroidX<800 and 480<centroidY<500):
        # count4 = count4 + 1
        # print(count4)

        # elif(900<centroidX<1000 and 480<centroidY<500):
        # count5 = count5 + 1
        # print(count5)

        cv2.line (frame2, (720, 490), (800, 490), (255, 0, 0), 6)
        cv2.putText (frame2, ":{}".format (count1), (760, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.line (frame2, (710, 185), (785, 185), (255, 0, 0), 6)
        cv2.putText (frame2, ":{}".format (count2), (750, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.line (frame2, (860, 50), (860, 100), (255, 0, 0), 6)
        cv2.putText (frame2, ":{}".format (count3), (840, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.line (frame2, (1130, 40), (1140, 90), (255, 0, 0), 6)
        cv2.putText (frame2, ":{}".format (count4), (1110, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # cv2.line(frame2,(500,500),(600,500),(255,0,0),6)
        # cv2.putText(frame2, ":{}".format(count3), (500, 500),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # cv2.line(frame2,(700,500),(800,500),(255,0,0),6)
        # cv2.putText(frame2, ":{}".format(count4), (700, 500),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # cv2.line(frame2,(900,500),(1000,500),(255,0,0),6)
        # cv2.putText(frame2, ":{}".format(count5), (900, 500),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


def get_centroid(x, y, w, h):
    x1 = int (w / 2)
    y1 = int (h / 2)

    cx = x + x1
    cy = y + y1

    return (cx, cy)


while True:

   # cv2.namedWindow ('frame1', cv2.WINDOW_NORMAL)
   # cv2.resizeWindow ('frame1', 1080, 1920)

    _, frame1 = cap.read ()
    _, frame2 = cap.read ()
    frame1 = cv2.resize (frame1, (1280, 720))
    frame2 = cv2.resize (frame2, (1280, 720))
    height, width, _ = frame1.shape
   # print(height)
   # print(width)
    grayFrame1 = cv2.cvtColor (frame1, cv2.COLOR_BGR2GRAY)
    grayFrame2 = cv2.cvtColor (frame2, cv2.COLOR_BGR2GRAY)
    gauBlur1 = cv2.GaussianBlur (grayFrame1, (21, 21), 0)
    gauBlur2 = cv2.GaussianBlur (grayFrame2, (21, 21), 0)
    difference = cv2.absdiff (gauBlur1, gauBlur2)
    ret, thresh = cv2.threshold (difference, 10, 255, cv2.THRESH_BINARY)
    thresh = cv2.dilate (thresh, None, iterations=2)
    thresh = cv2.erode (thresh, None, iterations=2)
    contours, hierarchy = cv2.findContours (thresh.copy (), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    frame2 = frame1
    CarDetect ()

    cv2.imshow ("Frame1", frame1)
    # cv2.imshow("Frame2",frame2)
    # cv2.imshow("Difference",difference)
    # cv2.imshow("Thresh",thresh)
    # cv2.imshow("blur",gauBlur1)
    # cv2.imshow("contour",contours)

    key = cv2.waitKey (30)
    if key == 27:
        break

cap.release ()
cv2.destroyAllWindows ()