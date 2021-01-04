import cv2


#高斯法特別拿出來加-雜質過多

for i in range(8):
    img_name = "a01-" + str(i) + "-out-ADAPTIVE_THRESH_GAUSSIAN_C.jpg"
    url = "./ga/"
    rel_url02=url+img_name
    img_02 = cv2.imread(rel_url02)
    if i==0:
        add_img02 = img_02
    else:
        add_img02 = cv2.add(add_img02, img_02)
        print("yes:",i)


cv2.imwrite("ga.jpg", add_img02)
