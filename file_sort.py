import os
import glob
import shutil
from os import path
import sys
print("Welcome to file sort\nEnter 0 in any prompt to exit\nBasic ideas of files and file extensions are necessary for operation of the program")
status='not ok'
while(status=='not ok'):
    in_loc=str(input("Enter the location to be sorted:"))+"\*"
    if in_loc =='0\*':
        sys.exit("Termination!!!")
    filename=glob.glob(in_loc)
    status='ok'
    if not filename:
        status='not ok'
        print("The folder doesn't exist!!Check the input and try again...\n0 for termination")
files=[]
FilesLocation=str(input("Enter the location to store the sorted files:"))
if FilesLocation=='0':
    sys.exit("Termination!!!")
status='continue'
while(status=='continue'):
    status='stop'
    exten=input("Enter the extention of the files to be placed in selected location:")
    if exten=='0':
        sys.quit("Termination!!!")
    files.append(str(exten))
    var=input("Do you want to enter more(0:No)(1:Yes)")
    if var==1:
        status='continue'
for file in filename:
    
    if os.path.splitext(file)[1] in files:
        print("moving...")
        if(path.exists(FilesLocation)):
            shutil.move(file,FilesLocation)
        else:
            status='error'
            while(status=='error'):
                try:
                    os.mkdir(FilesLocation)
                    shutil.move(file,FilesLocation)
                except OSError as error:
                    print(error)
                    FilesLocation=input("Enter a different location:(0 for termination)")
                    if FilesLocation=='0':
                        sys.exit("Termination!!!")
                    status='error'
