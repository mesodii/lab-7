from PIL import Image, ImageFilter

def proc1():
    image = Image.open('kapibara.jpg')
    image.show()

    w, h = image.size
    f = image.format
    m = image.mode

    print('Ширина:', w)
    print('Высота:', h)
    print('Формат:', f)
    print('Цветовая модель:', m)

def proc2():
    image = Image.open('kapibara.jpg')
    newimage = image.resize((image.width//3, image.height//3))
    newimage.save('rekapibara.jpg')

    conimage = image.transpose(Image.FLIP_LEFT_RIGHT)
    conimage.save('flipkapibara.jpg')
    conimage = image.transpose(Image.FLIP_TOP_BOTTOM)
    conimage.save('kapibaraflip.jpg')

def proc3():
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for file in images:
        image = Image.open(file)
        newimg = image.filter(ImageFilter.CONTOUR)
        newimg.show()
        newimg.save('new' + file)

def proc4():
    image = Image.open('watermark.png')
    newimg = image.resize((image.width // 3, image.height // 3))

    imge = Image.open('kapibara.jpg')
    imge.paste(newimg)
    imge.save('watermark1.png')

proc1(), proc2(), proc3(), proc4()