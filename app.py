import os
import time
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

cwd = os.getcwd()

class OnMyWatch:
  # Set the directory to be watched
  watchDirectory = f"{cwd}/uploads"

  def __init__(self):
      self.observer = Observer()

  def run(self):
      event_handler = Handler()
      self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
      self.observer.start()
      try:
          while True:
              time.sleep(5)
      except:
          self.observer.stop()
          print("Observer Stopped")

      self.observer.join()

class Handler(FileSystemEventHandler):
  def __init__(self):
    self.observer = Observer()

  def compress_images(self, directory=False, quality=30, customExportFolder=False):
    compressedFilesLocation = cwd+"/compressed"
    # listing out the files inside path 
    files = os.listdir(f'{cwd}/{directory}')
    if customExportFolder:
      if not os.path.exists(customExportFolder):
        os.mkdir(customExportFolder)
      compressedFilesLocation = customExportFolder
    elif not os.path.exists(compressedFilesLocation):
      os.mkdir(compressedFilesLocation)

    os.chdir(f'{cwd}/{directory}')
    # return print('cwd', os.getcwd())
    images = [file for file in files if file.endswith(('jpg', 'png', 'JPG'))]
    for image in images:
      splitImageUrl = os.path.splitext(image)
      print('image:', image)
      img = Image.open(image)
      img.save(f"{compressedFilesLocation}/"+splitImageUrl[0]+"_compressed"+splitImageUrl[1], optimize=True, quality=quality)

  def on_created(self, event):
    # print(event.src_path)
    fileType = os.path.splitext(event.src_path)[1]
    if(fileType == '.jpg' or fileType == '.png'):
      self.compress_images('uploads', 50)
    else:
      print("only .jpg and .png file types are supported")              
  
if __name__ == '__main__':
  watch = OnMyWatch()
  watch.run()


