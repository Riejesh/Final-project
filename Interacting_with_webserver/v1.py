#! /usr/bin/env python3
import os
import requests

script_dir = os.getcwd()
os.chdir('/home/riejesh/data/feedback')
data_dir = os.getcwd()
print ("The script is executed from {}".format(script_dir))
print ("Files are beig fetched from {}".format(data_dir))
print (" ")

i=0
dict= {}
key_value = ("title","name","date","feedback")

for root, dirs, files in os.walk(data_dir, topdown=False):
  for file in files:
    print ("Currently working on {}".format(file))
    with open(file) as f:
      while (i==0 & i<len(key_value)):
        for line in f:
          dict.update({key_value[i]:line})
          i+=1
        print (dict) 
#    i=0
