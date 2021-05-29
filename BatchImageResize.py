import cv2
import glob
import os
import argparse

ap  = argparse. ArgumentParsar()
images = glob.glob("*.jpg")

for image  in images:
    img = cv2.imread(image,0)
    re = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
    cv2.imshow("Hey", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+image, re)

    
