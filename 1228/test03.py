# 一般照片兩兩相減後儲存 相加
import cv2

for i in range(8):
    list_name1 = i + 1
    imgname1=  ("./ttest/g01" + str(list_name1)+".jpg")
    print(imgname1)
    list_name2 = i + 2
    imgname2 = ("./ttest/g01" + str(list_name2) + ".jpg")
    print(imgname2)
    img1 = cv2.imread(imgname1)
    img2 = cv2.imread(imgname2)
    img = cv2.subtract(img1, img2)
    if i==0:
        add_img=img
    else:
        add_img = cv2.add(add_img, img)
    output_name=("output"+str(i)+".jpg")
    print(output_name)
    cv2.imwrite(output_name, img)

cv2.imwrite("out.jpg", add_img)