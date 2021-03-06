# -*- coding: utf-8 -*-
"""Image Segmentation Hough Transformation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/157UY5UqO-Stxbx19c7G8rh6Igtxc6Cde
"""

import cv2
import numpy as np

# Read image 
img = cv2.imread('/content/download.png', cv2.IMREAD_COLOR) # download.png is the filename
# Convert the image to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 200)
# Detect points that form a line
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=10)
# Draw lines on the image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

cv2.imwrite("Hough Lines.jpg",img)