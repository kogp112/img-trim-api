import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# read local file
def readFile():
  img = mpimg.imread("/test.jpg", "r")
  plt.imshow(img)
  print(img.shape)

readFile()