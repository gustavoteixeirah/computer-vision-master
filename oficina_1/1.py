import matplotlib.pyplot as plt
import numpy as np
import cv2


def image_blending(img1, img2, alpha):
    assert img2.shape == img1.shape
    img_blend = alpha * img1 + (1 - alpha) * img2
    return img_blend.astype("uint8")


img1 = cv2.imread("./img_man.png")
print("Shape img1", img1.shape)


img2 = cv2.imread("./img_lion.png")
print("Shape img2", img2.shape)

img2 = cv2.resize(img2, [928, 704])
print("Shape img2", img2.shape)
plt.figure()
plt.imshow(img1[:,:,::-1])
plt.show()

blended_image = image_blending(img1, img2, 0.5)
cv2.imwrite("blended_image.png", blended_image)
