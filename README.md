# project-luure.ai
The project's 3 primary scripts.<br>
* auto file sort.py
* file_sort.py
* pdf_to_components.py<br>
# auto file sort.py
The auto file sort.py is a script to sort the files in a directory according to its extension. new folders are created for each new extension encountered in the directory.
Eg:The file named demo.txt will moved to the folder named txt in the current directory.<br><br>
## Code<br>
```python
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
```
<br><br>
# file_sort.py
file_sort.py gives more control on where the files are to be moved and which files are to be moved. The script searches the input directory and asks the user for a prefered location. If the location doesn't exist the location is created for the user. All files with the extension/extensions entered by the user is moved to the diirectory specified by the user.<br><br>
## Code<br>
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
```
<br><br>
# pdf_to_components
This script is used to scrape pdf files. The user needs to enter a file with its full location. The script find the file amd using different libraries takes the pdf apart to retreive non inline images, tables and text from the pdf.<br><br>
## Code<br>
```python
from pdfminer.high_level import extract_text
import fitz
import io
import camelot
from PIL import Image
import os
import sys

status='not ok'
while(status=='not ok'):
	in_loc=input("Enter the full path of PDF file::")
	if in_loc =='0':
		sys.exit("Termination!!!")
	if os.path.exists(in_loc):
		status='ok'
		pdf_file=in_loc
	else:
		status='not ok'
		print("The file doesn't exist!!Check the input and try again...\n0 for termination")

parent=os.path.dirname(pdf_file)
filename=os.path.splitext(os.path.basename(pdf_file))[0]
if os.path.exists(os.path.join(parent,filename)):
	directory=os.path.join(parent,filename)
else:
	os.mkdir(os.path.join(parent,filename))
	directory=os.path.join(parent,filename)

text = extract_text(pdf_file)
file = fitz.open(pdf_file)
for page_index in range(len(file)):
	page = file[page_index]
	image_list = page.getImageList()
	if image_list:
		print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
	else:
		print("[!] No images found on page", page_index)
	for image_index, img in enumerate(page.getImageList(), start=1):
		xref = img[0]
		base_image = file.extractImage(xref)
		image_bytes = base_image["image"]
		image_ext = base_image["ext"]
		image = Image.open(io.BytesIO(image_bytes))
		img_loc=os.path.join(directory,f"{filename}_image{page_index+1}_{image_index}.{image_ext}")
		image.save(open(img_loc, "wb"))
tables = camelot.read_pdf(pdf_file)
print("Total tables extracted:", tables.n)
for i in range(tables.n):
	print(tables[i].df)
	tab_loc=os.path.join(directory,f"{filename}_table{i}.xlsx")
	tables[i].to_excel(tab_loc)
text_loc=os.path.join(directory,f"{filename}_text.txt")
print(text)
file1 = open(text_loc,"w",encoding='utf-8')
file1.write(text)
file1.close()
```
<br><br>
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

