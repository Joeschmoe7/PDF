import PyPDF2

device_name = ""
keyword = "Device Name"
file_path = r"D:\23-4808\ABR16\Extractions\00008110-001918EE1A99401E.pdf"
pdfFileObj = open(file_path, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
pageObj = pdfReader.pages[0]
text = pageObj.extract_text()
lines = text.split("\n")
#print(lines)
pdfFileObj.close()
for items in lines:
    index = items.find(keyword)
    if index != -1:
        device_name = items[index + len(keyword):]
print(device_name)

