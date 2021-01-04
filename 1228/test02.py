import cv2

# img1 = cv2.imread('./Produce0128.jpg')  #讀圖
# img2 = cv2.imread('./Produce0129.jpg')  #讀圖
img1 = cv2.imread('./27-28.jpg')  #讀圖
img2 = cv2.imread('./28-29.jpg')  #讀圖
#img = cv2.subtract(img1,img2)
img = cv2.add(img1,img2)
cv2.imshow("img", img)
cv2.waitKey(0)

cv2.imwrite('output3.jpg', img)