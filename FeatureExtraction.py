
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

def describe(bins, image, mask = None):
		hist = cv2.calcHist([image], [0, 1, 2],
			mask, bins, [0, 256, 0, 256, 0, 256])
		hist = cv2.normalize(hist, dst=None)


		return hist.flatten()

image = cv2.imread('TestImg/crocus-1.png')
output = describe([8, 8, 8], image)

print output

