import cv2

vc = cv2.VideoCapture('Produce02.mp4')  # 读入视频文件
c = 2
fps = vc.get(cv2.CAP_PROP_FPS)
if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False
    print("404")

print("fpa:",fps)
timeF = 10  # 视频帧计数间隔频率

while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (c % timeF == 0):  # 每隔timeF帧进行存储操作
        imgname='./1221/' + str(c) + '.jpg'
        cv2.imwrite(imgname, frame)  # 存储为图像

        print("YES: ",imgname)
    c = c + 1
    print(c)
    cv2.waitKey(1)
vc.release()
