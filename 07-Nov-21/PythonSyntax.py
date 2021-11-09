# -------------------------------------------------
# Python Syntax
# -------------------------------------------------


# -------------------------------------------------
# python line structur and indentation
# -------------------------------------------------

# A Python program is divided into a number 
# of logical lines and every logical line is terminated
# by the token NEWLINE. A logical line is created from 
# one or more physical lines.
# A line contains only spaces, tabs, formfeeds
# possibly a comment, is known as a blank line, and Python
# interpreter ignores it.
# A physical line is a sequence of characters terminated 
# by an end-of-line sequence

# ex
x = 3 
if x > 0 :
    print(f"These three lines ar logical/physical lines")

# -------------------------------------------------
# Comments in Python:
# -------------------------------------------------

# A comment begins with a hash character(#)
#  which is not a part of the string literal 
# and ends at the end of the physical line.
#  All characters after the # character up to
#  the end of the line are part of the comment
#  and the Python interpreter ignores them. 
# See the following example. It should be noted
#  that Python has no multi-lines or block comments facility.

# -------------------------------------------------
# Joining two lines:
# -------------------------------------------------
# When you want to write a long code in a single line you can break the logical
#  line in two or more physical lines using backslash character(\).
#  Therefore when a physical line ends with a backslash characters(\) 
# and not a part of a string literal or comment then it can join 
# another physical line. See the following example.
# ex2
x = 0 
y = 2 
z = 0
v = 5
l = 0
g = 9
if x == 0 and y > 0 \
    and z == 0 and v > 0\
    and l == 0 and g > 0:
    print(f"this is an example for joining lines")

# -------------------------------------------------
# Multiple Statements on a Single Line:
# -------------------------------------------------

# You can write two separate statements into a single 
# line using a semicolon (;) character between two line.
# ex3
print("this is statement1")
print("this is statement2")
# you can write the 2 statemnts in the same line
print("this is statement1") ; print("this is statement2")

# -------------------------------------------------
# indentation
# -------------------------------------------------
print(type(lambda:None))

