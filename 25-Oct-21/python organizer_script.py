# --------------------------------------
# ----File's Organizer Application -----
# --------------------------------------
"""
This Application organizes the files according its extension and
create a new folders for each extension.
"""
# -------------- import required modules --------------
import os
import time
import shutil

# -------------- Folder abs path -------------------------
# determin the current working directory 
# for start organize its files by one of the following three methodes:
# a- use the os module
#---------
# currentDire = os.path.dirname(os.path.realpath(__file__))
# print(currentDire)
# b- use the os module
# ---------
# dir2 = os.path.abspath(os.path.dirname(__file__))
# print(dir2)
# c- recieve the folder from user
# ---------
currentDire = input("please enter the folder abs path to start organize: ")

# ----------------- Welcome statement -----------------------
print("*" * 56)
print(f"{'*' * 15} welcome to Organizer App {'*' * 15}")
print("*" * 56)

# ---------------- start organize files extentions -----------

# organize Images
# -----------------

for filename in os.listdir(currentDire):
    if filename.endswith((".png", ".jpg", ".gif", ".jpeg", ".png", ".PNG", ".ipynb", ".JPG",".vcf")):
        if not os.path.exists("Image"):
            os.mkdir("Image")
        shutil.copy(filename, "Image")
        os.remove(filename)
    print(f"Organized files: {'--->' * 2}{filename}")


# organize Excel 
# ------------------
for filename in os.listdir(currentDire):
    if filename.endswith((".xlsx", ".xlsm", "xls", ".XLS", ".csv", ".xlsb", ".xltx", ".xlt", ".xltm")):
        if not os.path.exists('excelFile'):
            os.mkdir('excelFile')
        shutil.copy(filename, 'excelfile')
        os.remove(filename)
    print(f"Organized files: {'--->' * 2}{filename}")


# organize Power Point ppt
# ------------------

for filename in os.listdire(currentDire):
    if filename.endswith((".ppt", ".pptx")):
        if not os.path.exists('powerPointFiles'):
            os.mkdir('powerPointFiles')
        shutil.copy(filename, 'powerPointFiles')
        os.remove(filename)
    print(f"Organized files: {'--->' * 2}{filename}")

# organize Word doc
# ------------------
for filename in os.listdir(currentDire):
    if filename.endswith(('.doc', '.docx', '.txt', 'Txt','.DOC', '.DOCX', '.docx2', 'DOCX2')):
        if not os.path.exists('Wordfile'):
            os.mkdir('Wordfile')
        shutil.copy(filename, 'Wordfile')
        os.remove(filename)
    print(f"Organized files: {'--->' * 2}{filename}")
        

# organize power Bi
# ------------------
for filename in os.listdir(currentDire):
    if filename.endswith((".pbix", ".pbi", ".dax")):
        if not os.path.exists('PowerBIfile'):
            os.mkdir('PowerBIfile')
        shutil.copy(filename, 'PowerBIfile')
        os.remove(filename)
    print(f"Organized files: {'--->' * 2}{filename}")


#  organize PDF
# ------------------
for filename in os.listdir(currentDire):
    if filename.endswith((".pdf", ".PDF")):
        if not os.path.exists('pdfFile'):
            os.mkdir('pdfFile')
        shutil.copy(filename, 'pdfFile')
        os.remove(filename)
    print(f"Organized files: {'--->' * 2}{filename}")


# organize zip files
for filename in os.listdir(currentDire):
    if filename.endswith((".zip", ".rar", ".gz")):
        if not os.path.exists("zipFile"):
            os.mkdir("zipFile")
        shutil.copy(filename, "zipFile")
        os.remove(filename)
    print(f"organized files:{'-->' *2}{filename}")
print("*" * 40)


# organize exe files
for filename in os.listdir(currentDire):
    if filename.endswith((".exe", ".eml", ".Rhistory", ".json", ".ica", ".msi", ".imap", ".crdownload", ".iso", ".isc")):
        if not os.path.exists("executionFiles"):
            os.mkdir("executionFiles")
        shutil.copy(filename, "executionFiles")
        os.remove(filename)
    print(f"organized files:{'-->' *2}{filename}")
print("*" * 40)
print("Organizing  finished")
time.sleep(25)