# -*- coding: utf-8 -*-
"""Image Segmentation Edge Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ylodOrg9cA6GbiXECBPB9P7a9ThNkd5I
"""

import cv2
# Read the original image

img = cv2.imread('/content/388bf7617036dc17eabc459af0329f5eb6a0753d_1603372570.jpg')

# Display original image

cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
# img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_gray, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
# cv2.imshow('Sobel X', sobelx)
# cv2.waitKey(0)
# cv2.imshow('Sobel Y', sobely)
# cv2.waitKey(0)
# cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
# cv2.waitKey(0)
# Canny Edge Detection
edges = cv2.Canny(image=img_gray, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
# cv2.imshow('Canny Edge Detection', edges)
# cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("sobel.jpg",sobelxy)
cv2.imwrite("canny.jpg",edges)