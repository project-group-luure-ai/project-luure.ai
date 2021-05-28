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
