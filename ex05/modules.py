from PIL import Image
test_type_image = type(Image)
print(test_type_image)

mon_image = Image.open('./test.png')
Image._show(mon_image)
