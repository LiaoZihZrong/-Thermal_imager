import cv2

#七種二值化相減


for i in range(8):
    img_name = "a01-" + str(i) + "-"
    img01 = img_name + "out-THRESH_BINARY.jpg"
    img02 = img_name + "out-THRESH_BINARY_INV1.jpg"
    img03 = img_name + "out-THRESH_TRUNC.jpg"
    img04 = img_name + "out-THRESH_TOZERO.jpg"
    img05 = img_name + "out-THRESH_TOZERO_INV.jpg"
    img06 = img_name + "out-ADAPTIVE_THRESH_MEAN_C.jpg"
    img07 = img_name + "out-ADAPTIVE_THRESH_GAUSSIAN_C.jpg"


    url = "./testall/"
    rel_url02=url+img02
    img_02 = cv2.imread(rel_url02)
    if i==0:
        add_img02 = img_02
    else:
        add_img02 = cv2.add(add_img02, img_02)
        print("yes:",i)


output_name02=("output"+img02)
cv2.imwrite(output_name02, add_img02)
