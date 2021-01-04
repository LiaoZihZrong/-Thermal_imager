import cv2
import matplotlib.pyplot as plt
#五種二值化
img = cv2.imread('output13.jpg', 0)  # 直接读为灰度图像
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("out-THRESH_BINARY.jpg", thresh1)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite("out-THRESH_BINARY_INV1.jpg", thresh2)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.imwrite("out-THRESH_TRUNC.jpg", thresh3)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.imwrite("out-THRESH_TOZERO.jpg", thresh4)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imwrite("out-THRESH_TOZERO_INV.jpg", thresh5)
titles = ['img', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()