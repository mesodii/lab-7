from PIL import Image
image = Image.open('watermark.png')
newimg = image.resize((image.width // 3, image.height // 3))

imge = Image.open('kapibara.jpg')
imge.paste(newimg)
imge.save('watermark1.png')