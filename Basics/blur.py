from PIL import Image, ImageFilter

before = Image.open('laptop.png')
after = before.filter(ImageFilter.BLUR)
after.save('laptop_blur.png')
