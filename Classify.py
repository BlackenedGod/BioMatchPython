__author__ = 'altug'

from RGBHistogram import RGBHistogram
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
import numpy as np
import argparse
import glob
import cv2

imagePaths = sorted(glob.glob("TestImg/*.png"))
maskPaths = sorted(glob.glob("MaskImg/*.png"))
imagePath = "TestImg/picTac.png"

data = []
target = []

desc = RGBHistogram([8, 8, 8])

counter = 0
for maskPath in maskPaths:
    image = cv2.imread(imagePath)
    mask = cv2.imread(maskPath)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    counter += 1
    print counter
    features = desc.describe(image, mask)

    data.append(features)
    target.append(imagePath)

print data, '\n', target
