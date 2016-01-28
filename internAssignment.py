#!python 3

#Program to count occurrences of "the", the letter "e", total number of lines in the file, and size of the file.
#extra credit - change every occurence of "the" to "_the_"

import os, re
from tkinter.filedialog import askopenfilename

#Select any text document
filename = askopenfilename()

#Identify and count "the"
filename1 = open(filename,"r").read().lower()
theCounter = re.split(r"\W+?", filename1)
print("The occurences of the's are: " + str(theCounter.count("the")))

#Identify and count the letter "e"
eCount = filename1.count("e")
print("The occurences of e's are: " +str(eCount))

#Count the total number of lines in the file
lineCount = 1
with open(filename, "rb") as f:
    for line in f:
        lineCount+=1
print ("There are " + str(lineCount) + " lines")

#Identify the total size of the file
totalSize = os.path.getsize(filename)
print("The size of the file is " + str(totalSize) + " bytes" +" or " +str(totalSize/1000000) + " Mb")

#Change the word "the" to "_the_"
changeWord = open(filename +"New.txt","w")
theReplace = re.sub(r"(?<!\w)the(?!\w)", "_the_", filename1)
changeWord.write(theReplace)
changeWord.close()
