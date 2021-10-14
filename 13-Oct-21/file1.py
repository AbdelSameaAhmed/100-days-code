print("I love Python ")

# ----------------
# all data in python are opject
# DATA TYPE -------
# -----------------
#
print(type(10)) # integer data
print(type(10.9)) # float data
print(type((1, 2, 3, 4))) # tuple
print(type([1, 2, 3, 4, 5])) # list
print(type({"one": 1, "tow": 2, "three": 3})) # dectionary
print(type(2 == 2))  # boolean

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# --------------
# escape charachter 
#
# back slash b "\b" remove left 
print("hello\bworld") # \b removes the "o" letter

# back slash new line \
    
print( "hello \
      I love \
      Python")

print("I\nlove\nPython")
# carrage return \r
print("12345\rabc") 



mystring = """string 
is not "test" \ 'test2' \n
the same"""

print(mystring)

# ----------------------
# STRING methodes
# ----------------------
aa = "     I love python     "
len(aa)

# String functions
# strip() # lstrip() # rstrip()

print(aa.strip())
print(aa.lstrip())
print(aa.rstrip())


aa = "#######I love python########"
print(aa.strip("#"))
print(aa.lstrip("#"))
print(aa.rstrip("#"))



# ------------------ 
# Title

bb = "i love 3d and i love python and i love tech"
print(bb.title())
print(bb.capitalize())


# ------------------------
# zfill()

a , b , c = "1" , "11", "111"

print(a.zfill(1))
print(c.zfill(3))


bname = "asa"
print(bname.upper())
bname = "ASA"
print(bname.lower())

# -----------------------------
# split()

aaa = "I-Love Python very much"
alist1 = aaa.split()
print(alist1)
