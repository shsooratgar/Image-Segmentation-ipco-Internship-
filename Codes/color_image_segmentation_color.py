# -*- coding: utf-8 -*-
"""Color Image Segmentation Color.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15H2kfx4sYIgXeJtl8tZpGHKsjIhOoPEs
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2
nemo = cv2.imread('/content/Wallpapers_full_marlin.jpg')
nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)
light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask_white = cv2.inRange(hsv_nemo, light_white, dark_white)
result_white = cv2.bitwise_and(nemo, nemo, mask=mask_white)
mask = cv2.inRange(hsv_nemo, light_orange, dark_orange)
result = cv2.bitwise_and(nemo, nemo, mask=mask)
result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
cv2.imwrite("orange.jpg",result)
cv2.imwrite("white.jpg",result_white)
final_mask = mask + mask_white
final_result = cv2.bitwise_and(nemo, nemo, mask=final_mask)
final_result = cv2.cvtColor(final_result, cv2.COLOR_BGR2RGB)
cv2.imwrite("final_result.jpg",final_result)