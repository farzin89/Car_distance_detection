from math import pow,sqrt
import numpy as np
import sys
import cv2

cap = cv2.VideoCapture(0)

while True:

    ref,frame = cap.read()

    cv2.imshow("frame",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
