import matplotlib.pyplot as plt
import numpy as np
import cv2


def image_thresholding(img, th=127):
    _, bin_img = cv2.threshold(img, th, 255, cv2.THRESH_BINARY)
    return bin_img


img = cv2.imread("./maize-root-cluster.jpg")
print("Shape img", img.shape)

img_bin = image_thresholding(img)

plt.figure()
plt.imshow(img_bin, cmap="gray")
plt.show()

