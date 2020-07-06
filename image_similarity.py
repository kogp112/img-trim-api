from PIL import Image
import imagehash

def checkSImilarity():
  baseImage = imagehash.average_hash(Image.open('test.jpg'))
  referImage = imagehash.average_hash(Image.open('check.jpg'))

  print(baseImage)
  print(referImage)

  cutoff = 5
  if baseImage - referImage < cutoff:
    print(baseImage - referImage)
    
checkSImilarity()