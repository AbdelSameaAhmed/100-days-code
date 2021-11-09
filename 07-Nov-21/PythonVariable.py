# -------------------------------------------------
# Variable 
# -------------------------------------------------

Item_name = "computer" # string
Item_qty = 10 # Integer
Item_value = 1000.90 # float
print(Item_name)
print(Item_qty)
print(Item_value)
print("*"*60)
# swap var
x = 10
y = 20
print(x)
print(y)
print("*"*30)
x, y = y, x
print(x)
print(y)
print("*"*60)

# Local and global variables in Python
var1 = "Python" # glopal variable

def func1():
    var1 = "php" # private variable for only func1()
    return f"In side of func1 var1 = {var1}" 
def func2():
    return f"In side of func2 var1 = {var1}"

print(func1())
print(func2())
print("*"*30)

# assigning glopal variable
# ---------------------------
def funca():
    global vara # this is a GLOBAL Variable
    vara = 'php'
    print("In side funca() vara = ",vara)
def funcb():
    print("In side funcb() vara = ",vara)
print(funca())
print(funcb())

print("*"*30)
print("*"*30)

print(id(x))

