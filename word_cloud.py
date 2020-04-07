#!/usr/bin/env python3 
#pip install wordcloud
#pip install fileupload
#pip install ipywidgets
#jupyter nbextension install --py --user fileupload
#jupyter nbextension enable --py fileupload
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    """Initialization"""
    file_contents=file_contents.lower()
    result = {}
    no_punctuations=""
    no_uninteresting_words=[]
    
    """Remove punctuation from input string"""
    for char in file_contents:
        if char not in punctuations:
            no_punctuations = no_punctuations+char
    #print ("This is the o/p by removing punctuations: " + no_punctuations)
    #print (type(no_punctuations))
    
    """Remove uninterested words from input string"""
    words_only = no_punctuations.split()
    #print ("")
    #print ("This is o/p of coverting the input into list: {} ".format(words_only))
    #print ("")
    for words in words_only:
        #print (words)
        if words.isalpha():
            if words not in uninteresting_words:
                no_uninteresting_words.append(words)
            
    #print ("Final list removing punctuations and uninterested words: {}".format(no_uninteresting_words))
    #print ("")
    
    """counting the number of time a word appears in the list"""
    for word in no_uninteresting_words:
        if word not in result:
            result[word]=0
        result[word]+=1
    #return result 
    #print ("")
    
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(result)
    return cloud.to_array()

# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
