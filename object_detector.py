import cv2 as cv
import numpy as np
from windowcapture import window_capture


wincap = window_capture('window_name')

cascade_brim = cv.CascadeClassifier('cascade.xml')

while(True):
    screenshot = wincap.window_capture()
    screenshot = np.array(screenshot)
    
    rectangles = cascade_brim.detectMultiScale(screenshot)
    for (x,y,w,h) in rectangles:
        cv.rectangle(screenshot,(x,(y-100)),(x+w,(y-100)+h),(0,255,0),4)
        try:
        except:
            print("not detected")

    cv.imshow('AimBot',screenshot)
    key = cv.waitKey(1)
    if(key == ord('q')):
         cv.destroyAllWindows()
         break
print('done')
