# project-luure.ai
The project 3 primary scripts.
        + auto file sort.py
        + file_sort.py
        + pdf_to_components.py
# auto file sort.py
The auto file sort.py is a script to sort the files in a directory according to its extension. new folders are created for each new extension encountered in the directory.
Eg:The file named demo.txt will moved to the folder named txt in the current directory.
# file_sort.py
file_sort.py gives more control on where the files are to be moved and which files are to be moved. The script searches the input directory and asks the user for a prefered location. If the location doesn't exist the location is created for the user. All files with the extension/extensions entered by the user is moved to the diirectory specified by the user.<br><br>

```python
import os
import shutil
import sys

print("Welcome to file sort\nEnter 0 in any prompt to exit\nBasic ideas of files and file extensions are necessary for operation of the program")
status='not ok'
while(status=='not ok'):
    in_loc=str(input("Enter the location to be sorted:"))+os.sep
    if in_loc =='0\*':
        sys.exit("Termination!!!")
    file_n=os.listdir(in_loc)
    status='ok'
    if not file_n:
        status='not ok'
        print("The folder doesn't exist!!Check the input and try again...\n0 for termination")
filename=[]
for i in range(len(file_n)):
    filename.append(os.path.join(in_loc,file_n[i]))
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
print(filename)
for file in filename:
    
    if os.path.splitext(file)[1] in files:
        if os.path.exists(FilesLocation):
            print("path exist")
            shutil.move(file,FilesLocation)
        else:
            print("in else block")
            status='error'
            while(status=='error'):
                try:
                    print("in try block")
                    os.mkdir(FilesLocation)
                    shutil.move(file,FilesLocation)
                    status='ok'
                    pass
                except OSError as error:
                    print(error)
                    FilesLocation=input("Enter a different location:(0 for termination)")
                    if FilesLocation=='0':
                        sys.exit("Termination!!!")
                    status='error'
                    pass
```<br><br>
# pdf_to_components
This script is used to scrape pdf files. The user needs to enter a file with its full location. The script find the file amd using different libraries takes the pdf apart to retreive non inline images, tables and text from the pdf.
# Modules to be installed 
we need to install some python modules  using `pip install` to work with all the above scripts,they are
* camelot-py[cv]
```
pip install camelot-py[cv]
```
* Pillow
```
pip install Pillow
```
* pymupdf
```
pip install pymupdf
```
* pdfminer.six
```
pip install pdfminer.six
```

