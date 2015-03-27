import argparse
import cv2
import numpy as np
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image to be thresholded")
ap.add_argument("-t", "--threshold", type = int, default = 128,
help = "Threshold value")
args = vars(ap.parse_args())

 
# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# initialize the list of threshold methods
methods = [
    ("THRESH_BINARY", cv2.THRESH_BINARY),
    ("THRESH_BINARY_INV", cv2.THRESH_BINARY_INV),
    ("THRESH_TRUNC", cv2.THRESH_TRUNC),
    ("THRESH_TOZERO", cv2.THRESH_TOZERO),
    ("THRESH_TOZERO_INV", cv2.THRESH_TOZERO_INV)]

cv2.imshow("GRAY", gray)
# loop over the threshold methods
for (threshName, threshMethod) in methods:
    (T, thresh) = cv2.threshold(image, args["threshold"], 255, threshMethod)
    cv2.imshow(threshName, thresh)

    cv2.waitKey(0)

rect = (0, 0, 1, 1)
(_, mask) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)
outImg = cv2.grabCut(image, mask, rect, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_MASK)

cv2.imshow("OUT", outImg)