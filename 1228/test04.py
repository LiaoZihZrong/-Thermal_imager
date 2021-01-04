# 圖片二值化
from PIL import Image
img = Image.open('output13.jpg')

# 模式L”為灰色影象，它的每個畫素用8個bit表示，0表示黑，255表示白，其他數字表示不同的灰度。
Img = img.convert('L')
Img.save("test1.jpg")

# 自定義灰度界限，大於這個值為黑色，小於這個值為白色
Img = img.convert('1')
Img.save("test2.jpg")