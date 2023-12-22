import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('C:/Users/abdog/Desktop/test_images/person.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply median blur
median_blur_image = cv2.medianBlur(image, 5)  # Adjust the kernel size as needed

# Display the original and median-blurred images using Matplotlib
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(median_blur_image, cv2.COLOR_BGR2RGB))
plt.title('Median-Blurred Image')

plt.show()