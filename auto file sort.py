import os
import glob
import shutil
from os import path
import sys
print("Welcome to file sort\nEnter 0 in any prompt to exit\nBasic ideas of files and file extensions are necessary for operation of the program")
status='not ok'
while(status=='not ok'):
    directory=str(input("Enter the location to be sorted:"))+"\\"
    if directory =='0\\':
        sys.exit("Termination!!!")
    filename=os.listdir(directory)
    status='ok'
    if not filename:
        status='not ok'
        print("The folder doesn't exist!!Check the input and try again...\n0 for termination")
print(filename)
f= []
for (dirpath, dirnames, filenames) in os.walk(directory):
    f.extend(filenames)
    break
for i in range(len(filenames)):
    name,exten=os.path.splitext(filenames[i])
    if(path.exists(directory+exten[1:])):
            shutil.move(directory+filenames[i],directory+exten[1:])
    else:
        os.mkdir(directory+exten[1:])
        shutil.move(directory+filenames[i],directory+exten[1:])
