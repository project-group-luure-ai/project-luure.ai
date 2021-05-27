from pdfminer.high_level import extract_text
import fitz
import io
import camelot
from PIL import Image

pdf_file="D:\Projects\Python\data.pdf"
text = extract_text(pdf_file)
print(text)


# open the file
file = fitz.open(pdf_file)

# STEP 3
# iterate over PDF pages
for page_index in range(len(file)):
	
	# get the page itself
	page = file[page_index]
	image_list = page.getImageList()
	
	# printing number of images found in this page
	if image_list:
		print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
	else:
		print("[!] No images found on page", page_index)
	for image_index, img in enumerate(page.getImageList(), start=1):
		
		# get the XREF of the image
		xref = img[0]
		
		# extract the image bytes
		base_image = pdf_file.extractImage(xref)
		image_bytes = base_image["image"]
		
		# get the image extension
		image_ext = base_image["ext"]
tables = camelot.read_pdf(pdf_file)
print("Total tables extracted:", tables.n)
for i in range(tables.n):
	print(tables[i].df)
#tables[] contains tables
#image_list[] contains images
#text contains text
