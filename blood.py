# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:03:45 2024

@author: ohshi
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load the image
img_path = 'data/blood.png'
img = Image.open(img_path)
img_np = np.array(img)

# Convert the image to grayscale
gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to smooth the image
blurred = cv2.GaussianBlur(gray, (9, 9), 0)

# Adjust the minimum and maximum radius of circles to detect
min_radius = 1  # Adjust this value based on the size of the smallest target object
max_radius = 25  # Adjust this value based on the size of the largest target object

# Use Hough Circles to detect circles
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                           param1=50, param2=30, minRadius=min_radius, maxRadius=max_radius)

# Ensure some circles were found
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img_np, (x, y), r, (0, 255, 0), 4)

# Plot the original image and the one with circles marked
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB))
ax[0].set_title('Original Grayscale Image')
ax[1].imshow(cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB))
ax[1].set_title('Blood Cells Detected')
plt.show()

# Count the number of circles detected
num_circles = 0 if circles is None else len(circles)
print(num_circles)
