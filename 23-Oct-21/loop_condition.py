# --------------------------------------
# re-study loop and condtion statement
# --------------------------------------

# --------------------------------------
# by exercises
# ---------------------------------------

# --------------------------------------
# ex1
# --------------------------------------
# create program can open text file and read its Content
#  --------------------------------------
print(" ", end = '\n')
print("*" * 50)
# solution
# -----------------------------------------
def readtxtcontent(filename):
    fil = open(filename, 'r')
    for line in fil:
        line = line.strip()
        print(line)

# test function
readtxtcontent('test1.txt')


print(" ", end = '\n')
print("*" * 50)
# --------------------------------------
# ex2
# --------------------------------------
# create program return the number of lines in file
# -------------------------------------
# solution
# -----------------------------------------
def numofline(filename):
    count = 0
    fil = open(filename, 'r')
    fil = fil.readline().strip()
    for line in fil:
        le = len(fil)
        count +=1
    print(f"the number of lines of \'{filename}\' is: {count}")

# test function
numofline('test1.txt')

print(" ", end = '\n')
print("*" * 50)

# --------------------------------------
# ex2
# --------------------------------------
# create create program can open PDF file 
# and read its Content 
# and the number of pages in file
# -------------------------------------
# solution
# -------------------------------------
# import requird module
def pdfpages_count(filename, pageNum_toPrint):
    import PyPDF2
    from PyPDF2 import PdfFileReader, PdfFileWriter
    filed = open(filename, 'rb')
    reader = PyPDF2.PdfFileReader(filed)
    pagetoprint = reader.getPage(pageNum_toPrint)

    print(f"the number of pages is {reader.numPages}")
    print(pagetoprint.extractText().strip())

# test Function
pdfpages_count(filename='C:\\Users\\asahmed\\Documents\\GitHub\\100DaysOfCode\\100-days-code\\py4e.pdf',pageNum_toPrint= 16 )