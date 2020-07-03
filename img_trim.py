import os, sys
from PIL import Image

# divide image file
def divideFile():
  img = Image.open("./test.jpg", "r")
  img.show()
  
  # print image size in pixels
  width = img.size[0]
  height = img.size[1]
  
  # cut image (left, upper, right, lower)
  box = (0, 0, width / 2, height)
  print(box)
  croppedImage = img.crop(box)
  outfile = "./croppedTest.jpg"
  croppedImage.save(outfile, "JPEG")
  
divideFile()