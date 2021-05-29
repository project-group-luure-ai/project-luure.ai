# project-luure.ai
The project 3 primary scripts.
        + auto file sort.py
        + file_sort.py
        + pdf_to_components.py
# auto file sort.py
The auto file sort.py is a script to sort the files in a directory according to its extension. new folders are created for each new extension encountered in the directory.
Eg:The file named demo.txt will moved to the folder named txt in the current directory.
# file_sort.py
file_sort.py gives more control on where the files are to be moved and which files are to be moved. The script searches the input directory and asks the user for a prefered location. If the location doesn't exist the location is created for the user. All files with the extension/extensions entered by the user is moved to the diirectory specified by the user.
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

