#!/usr/bin/env python3
import glob
import os
from PIL import Image
import shutil

path = os.getcwd()
os.chdir ('supplier-data/images')
src=os.getcwd()
#print ("The present dir is {}".format(os.getcwd()))


for root, dirs, files in os.walk(src, topdown=False):
  for name in files:
    if name.endswith(".tiff"):
      outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpeg"
      print ("Currently working on file {}".format(name))
      im = Image.open(os.path.join(root, name))
      #m.resize((600,400))
      print ("Image to be modified is {}".format(im))
      mod_im=im.convert('RGB')
      mod_im.resize((600,400)).save(outfile, "JPEG", quality=100)
      print ("Modified image is {}".format(mod_im))

