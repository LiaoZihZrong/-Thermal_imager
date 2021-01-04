import cv2
import matplotlib.pyplot as plt
#倒退走-tozreo-inv二值化
import os

try:
    os.makedirs('./walk02-out/to/')
except:
    print("OK:build=./walk02-out/to/")

for i in range(9):
    #讀取第一張
    if i == 0 :
        img_name = "./walk02/walk02" + str(i + 1) + ".jpg"
        img_color = cv2.imread(img_name, cv2.IMREAD_COLOR)
        img = cv2.imread(img_name, 0)  # 直接读为灰度图像

        titles = ['img_original', 'gray']
        b, g, r = cv2.split(img_color)
        img_color_merg = cv2.merge([r, g, b])
        images = [img_color_merg,img]
        #畫圖
        plt.figure()
        plt.subplot(1,2,1),plt.imshow(images[0])
        plt.title(titles[0])
        plt.subplot(1,2,2),plt.imshow(images[1],'gray')
        plt.title(titles[1])
        plt.xticks([]), plt.yticks([])
        plt.ion()
        plt.pause(0.4)  #显示秒数
        plt.close()
    else:
        img_name = "./walk02/walk02" + str(i + 1) + ".jpg"
        img_color = cv2.imread(img_name, cv2.IMREAD_COLOR)

        img_name1= "./walk02/walk02" + str(i ) + ".jpg"
        img_name2= "./walk02/walk02" + str(i + 1) + ".jpg"
        #print(i+2,"-YES")
        img_color_1 = cv2.imread(img_name1) # 直接读为灰度图像
        img_color_2 = cv2.imread(img_name2) # 直接读为灰度图像
        img_sub = cv2.subtract(img_color_1, img_color_2)
        #相減後相加(灰圖)
        if i == 1:
            add_img_sub = img_sub
        else:
            add_img_sub = cv2.add(add_img_sub, img_sub)

        #剪完後二值化
        img1 = cv2.imread(img_name1, 0) # 直接读为灰度图像
        img2 = cv2.imread(img_name2, 0) # 直接读为灰度图像
        img_sub = cv2.subtract(img1, img2)
        ret_2, thresh3 = cv2.threshold(img_sub, 127, 255, cv2.THRESH_TOZERO_INV)
        #儲存thresh3

        output_tru_name="./walk02-out/to/walk02-out-to-"+str(i)+".jpg"
        cv2.imwrite(output_tru_name,thresh3)
        #二值化相加
        if i == 1:
            tru_add_img_sub= thresh3
        else:
            tru_add_img_sub= cv2.add(tru_add_img_sub, thresh3)



        img_name_pl="img"+str(i+1)
        titles = [img_name_pl, 'TOZERO_INV-cut']

        b, g, r = cv2.split(img_color)
        img_color_merg = cv2.merge([r, g, b])
        images = [img_color_merg, thresh3]
        #畫圖
        plt.figure()
        plt.subplot(1,2,1),plt.imshow(images[0])
        plt.title(titles[0])
        plt.subplot(1,2,2),plt.imshow(images[1],'gray')
        plt.title(titles[1])
        plt.xticks([]), plt.yticks([])
        plt.ion()
        plt.pause(0.4)  #显示秒数
        plt.close()

#顯示相減相加的結果
#彩圖相減後相加add_img_sub
#二值化後相加tru_add_img_sub
cv2.imwrite("./walk02-out/walk02-color-out.jpg", add_img_sub)
cv2.imwrite("./walk02-out/walk02-to-out.jpg", tru_add_img_sub)
#顯示最終結果
titles = ["all-add", 'THRESH_TOZERO_INV-cut-all']
b, g, r = cv2.split(add_img_sub)
img_color_merg_out = cv2.merge([r, g, b])
images = [img_color_merg_out, tru_add_img_sub]
#畫圖
plt.figure()
plt.subplot(1,2,1),plt.imshow(images[0])
plt.title(titles[0])
plt.subplot(1,2,2),plt.imshow(images[1],'gray')
plt.title(titles[1])
plt.xticks([]), plt.yticks([])
plt.ion()
plt.pause(3)  #显示秒数
plt.close()

print("Done!")