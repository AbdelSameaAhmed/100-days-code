
# --------------------------------------------
# --------- PDF Files with PYTHON ------------
# --------------------------------------------
# -------------PyPDF2-------------------------

# import PyPDF2
# pip install PyPDF2

import PyPDF2
# OR
# from PyPDF2 import PdfFileReader, PdfFileWriter

# open pdf file using open('file path', 'rb') --> # rb reading in binary mode
file = open('C:\\Users\\asahmed\\Documents\\GitHub\\100DaysOfCode\\100-days-code\\py4e.pdf', 'rb')

# create reader object using PyPDF.PdfFileReader(file)
reader = PyPDF2.PdfFileReader(file)

# print(number of pages) using print(numPages)
print(reader.numPages)

# get data of specific page using reade.getPage(<numberofpage>)
pag1 = reader.getPage(0)

# assign extracted text from page of index 0 in var
datapdf = pag1.extractText()

# print var to see content
print(datapdf)

# repeat to see page2
page2 = reader.getPage(1)

datapdf2 = page2.extractText()

print(datapdf2)