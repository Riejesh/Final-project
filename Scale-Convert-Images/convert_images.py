#!/usr/bin/env python3
import glob
import os
from PIL import Image
import shutil

path = os.getcwd()
os.chdir ('images')
src=os.getcwd()
dest="/opt/icons"

print ("Your src path is {}".format(src))

for root, dirs, files in os.walk(src, topdown=False):
    for name in files:
      outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
      try:
        im = Image.open(os.path.join(root, name))
        im = im.transpose(Image.ROTATE_270).resize((128, 128))
        mod_im=im.convert('RGB')
        mod_im.save(outfile, "JPEG", quality=100)
      except :
        pass
    for jpgfile in glob.iglob(os.path.join(src, "*.jpg")):
      print (jpgfile)
      #print ("Entering jpg loop")
      shutil.move(jpgfile,dest)
    #print("")

print ("All files successfully moved to {}".format(dest))


