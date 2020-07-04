import os, sys
from PIL import Image

# divide image file
def divideFile():
  im = Image.open("./test.jpg", "r")
  
  # print image size in pixels
  print(im.size)
  imgwidth = 1200
  imgheight = 900
  
  height = imgheight // 3
  width = imgwidth // 3
  print(height)
  print(width)
  # divide into 9 images
  # horixontal
  for i in range(1, 4):
      # vertical
      for j in range(1, 4):
          box = ((j - 1) * width, (i - 1) * height, j * width, i * height)
          print(box)
          a = im.crop(box)
          path = "./IMG-" + str(i) + str(j) + "s.jpg"
          a.save(path, "JPEG")

divideFile()