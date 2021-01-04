import cv2

# 處理二值化-兩種比較好的
#img_name="e01-7-"
#img_name="f01-7-"
img_name="g01-7-"

#img = cv2.imread('./e01-do/output7.jpg', 0)  # 直接读为灰度图像
#img = cv2.imread('./f01-do/output7.jpg', 0)  # 直接读为灰度图像
img = cv2.imread('./g01-do/output7.jpg', 0)  # 直接读为灰度图像

#img_name="no-"
#img = cv2.imread('out.jpg', 0)  # 直接读为灰度图像

ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
img05=img_name+"out-THRESH_TOZERO_INV.jpg"
cv2.imwrite(img05, thresh5)

ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
img03=img_name+"out-THRESH_TRUNC.jpg"
cv2.imwrite(img03, thresh3)