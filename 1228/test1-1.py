import cv2
#七種二值化
img_name="a01-out-"


img = cv2.imread('./a01-do/out.jpg', 0)  # 直接读为灰度图像
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
img01=img_name+"out-THRESH_BINARY.jpg"
cv2.imwrite(img01, thresh1)

ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
img02=img_name+"out-THRESH_BINARY_INV1.jpg"
cv2.imwrite(img02, thresh2)


ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
img03=img_name+"out-THRESH_TRUNC.jpg"
cv2.imwrite(img03, thresh3)


ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
img04=img_name+"out-THRESH_TOZERO.jpg"
cv2.imwrite(img04, thresh4)


ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
img05=img_name+"out-THRESH_TOZERO_INV.jpg"
cv2.imwrite(img05, thresh5)


th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) #换行符号 \
img06=img_name+"out-ADAPTIVE_THRESH_MEAN_C.jpg"
cv2.imwrite(img06, th2)


th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2) #换行符号 \
img07=img_name+"out-ADAPTIVE_THRESH_GAUSSIAN_C.jpg"
cv2.imwrite(img07, th3)