import os
import shutil
import sys

print("Welcome to file sort\nEnter 0 in any prompt to exit\nBasic ideas of files and file extensions are necessary for operation of the program")
status='not ok'
while(status=='not ok'):
    directory=str(input("Enter the location to be sorted:"))+os.sep
    if directory ==("0"+os.sep):
        sys.exit("Termination!!!")
    filename=os.listdir(directory)
    status='ok'
    if not filename:
        status='not ok'
        print("The folder doesn't exist!!Check the input and try again...\n0 for termination")
f= []
for (dirpath, dirnames, filenames) in os.walk(directory):
    f.extend(filenames)
    break
for i in range(len(filenames)):
    name,exten=os.path.splitext(filenames[i])
    if(os.path.exists(directory+exten[1:])):
            shutil.move(directory+filenames[i],directory+exten[1:])
    else:
        os.mkdir(directory+exten[1:])
        shutil.move(directory+filenames[i],directory+exten[1:])
