import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Resim Yolu")
ap.add_argument("-t", "--threshold", type = int, default = 128,
help = "Threshold value")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image2 = cv2.imread(args["image"])
mask = np.zeros(image.shape[:2],np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

# newmask is the mask image I manually labelled
(_, newmask) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

mask[newmask == 0] = 0
mask[newmask == 255] = 1

mask, bgdModel, fgdModel = cv2.grabCut(image,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)

mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = image*mask[:,:,np.newaxis]
cv2.imshow("Mask", img)
cv2.imshow("Image", image2)

outImg = np.zeros((1,65),np.float64)

orb = cv2.ORB()

kp = orb.detect(img, None)

kp, des = orb.compute(img, kp)



img2 = cv2.drawKeypoints(img, kp, outImg, color=(0,0,255), flags=2)

cv2.imshow("KEYPOINTS", img2)

cv2.waitKey()


