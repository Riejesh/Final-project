#! /usr/bin/env python3
import os
import requests

'''Moving to the directory where we have the files to be loaded to dict'''
script_dir = os.getcwd()
os.chdir('/home/riejesh/data/feedback')
data_dir = os.getcwd()
print ("The script is executed from {}".format(script_dir))
print ("Files are beig fetched from {}".format(data_dir))
print (" ")

'''Initialize empty dict'''
'''Initializing a variable to loop through key's of DICT'''
i=0
dict= {}
key_value = ("title","name","date","feedback")

'''Creating a dictionary from file contents under a given directory'''
for root, dirs, files in os.walk(data_dir, topdown=False):
  for file in files:
    print ("Currently working on {}".format(file))
    with open(file) as f:
      while i<len(key_value):
        for line in f:
          line.strip().rstrip()
          dict.update({key_value[i]:line})
          i+=1
        print (dict) 
    i=0
