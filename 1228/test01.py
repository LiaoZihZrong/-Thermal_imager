import cv2
for i in range(30):
    list_name1 = i +1
    imgname1=  ("./test/Produce02"+str(list_name1)+".jpg")
    img = cv2.imread(imgname1)  #讀圖
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #轉灰階
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    #影像切割-只能處理灰階
    #127=>最小門檻
    #255=>最大門檻
    #cv2.THRESH_BINARY 切割演算法

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #輪廓尋找
    cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
    #畫出輪廓
    print(len(contours), len(hierarchy))
    print(len(contours[0]), len(hierarchy[0]))

    #cv2.imshow("img", img)
    #cv2.waitKey(0)

    output_name = ("output" + str(i) + ".jpg")
    print(output_name)
    cv2.imwrite(output_name, img)