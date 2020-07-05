import os, sys
from PIL import Image

# divide image file
def divideFile():
  file_name = "./" + sys.argv[1]
  num = sys.argv[2]
  
  im = Image.open(file_name, "r")
  
  # print image size in pixels
  print(im.size)
  imgwidth = 1200
  imgheight = 900
  
  # divide into 9 images
  height = imgheight // int(num)
  width = imgwidth // int(num)
  
  # horixontal
  for i in range(1, int(num) + 1):
      # vertical
      for j in range(1, int(num) + 1):
          box = ((j - 1) * width, (i - 1) * height, j * width, i * height)
          print(box)
          a = im.crop(box)
          path = "./IMG-" + str(i) + str(j) + "s.jpg"
          a.save(path, "JPEG")

divideFile()