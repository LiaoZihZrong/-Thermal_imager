import cv2


#to zero -f01 /g01

for i in range(8):
    #img_name = "g01-" + str(i) + "-out-THRESH_TRUNC.jpg"
    img_name = "g01-" + str(i) + "-out-THRESH_TOZERO_INV.jpg"
    #url = "./g01-b/g01tr/"
    url = "./g01-b/g01to/"
    rel_url02=url+img_name
    print(rel_url02)
    img_02 = cv2.imread(rel_url02)
    if i==0:
        add_img02 = img_02
    else:
        add_img02 = cv2.add(add_img02, img_02)
        print("yes:",i)

#cv2.imwrite("g01tr.jpg", add_img02)
cv2.imwrite("g01to.jpg", add_img02)
