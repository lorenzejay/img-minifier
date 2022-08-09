# todos
# [] check if file exists compressed then ask
# [] clear files in compressed folder?


from pickletools import optimize
from PIL import Image
import os
 
cwd = os.getcwd()

def compress_images(directory=False, quality=30):
  # if there is a directory change to it 
  if directory:
    os.chdir(directory)
  # listing out the files inside path 
  files = os.listdir()

  images = [file for file in files if file.endswith(('jpg', 'png', "JPG"))]
  for image in images:
    splitImageUrl = os.path.splitext(image)
    img = Image.open(image)
    #open in a new directory called compressed
    if not os.path.isdir(f"{cwd}/compressed"):
      os.mkdir(f"{cwd}/compressed")
    # saving with a new name
    img.save(f"{cwd}/compressed/"+splitImageUrl[0]+"_compressed"+splitImageUrl[1], optimize=True, quality=quality)

compress_images("uploads", 50)

