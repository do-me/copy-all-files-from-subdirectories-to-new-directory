# copy all files from all subdirectories to new directory

import glob
from shutil import copyfile

path = 'C:/source/'
files = [f for f in glob.glob(path + "**/*.txt", recursive=True)] # list comprehension, get file by extension
clean = [file.replace("\\", '/') for file in files] # windows specific: replace "\" 
    
dst="D:/destination/"

for i in clean:
    
    filn=i.split("/")[-1] # get filename
    findest= dst+filn
    copyfile(i, findest)
