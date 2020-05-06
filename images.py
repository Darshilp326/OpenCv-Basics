import cv2


class ImageName:
    def __init__(self, image):
       self.name = image
       self.img = cv2.imread(image)


bird = ImageName('bird.jpg')
height, width, channels = bird.img.shape
intensity = bird.img[213,320]
print(bird.name, width, height, channels,intensity)


cat = ImageName('cat.jpg')
height, width, channels = cat.img.shape
intensity = cat.img[195,320]
print(cat.name, width, height, channels,intensity)


flowers = ImageName('flowers.jpg')
height, width, channels = flowers.img.shape
intensity = flowers.img[142, 320]
print(flowers.name, width, height, channels,intensity)

horse = ImageName('horse.jpg')
height, width, channels = horse.img.shape
intensity = horse.img[202, 320]
print(horse.name, width, height, channels,intensity)

