# todos
# [] check if file exists compressed then ask
# [] clear files in compressed folder?


from pickletools import optimize
from PIL import Image
import os
 
cwd = os.getcwd()

def compress_images(directory=False, quality=30, customExportFolder=False):
  compressedFilesLocation = cwd+"/compressed"
  # if there is a directory change to it 
  if directory:
    os.chdir(directory)
  # listing out the files inside path 
  files = os.listdir()
  if customExportFolder:
    if not os.path.exists(customExportFolder):
      os.mkdir(customExportFolder)
    compressedFilesLocation = customExportFolder
  elif not os.path.exists(compressedFilesLocation):
    os.mkdir(compressedFilesLocation)

  images = [file for file in files if file.endswith(('jpg', 'png', "JPG"))]
  for image in images:
    splitImageUrl = os.path.splitext(image)
    img = Image.open(image)
    # print('splitImageUrl:',splitImageUrl) 
    # print(compressedFilesLocation)
    img.save(f"{compressedFilesLocation}/"+splitImageUrl[0]+"_compressed"+splitImageUrl[1], optimize=True, quality=quality)

# compress_images("uploads", 50)

compress_images("uploads", 50)
# def fireFromCustomFolder(folderName=False):
#   print(folderName)
#   if not os.path.isdir(folderName):
#     os.mkdir(folderName)
#   else:


# fireFromCustomFolder(f"{cwd}/compressed-test")
