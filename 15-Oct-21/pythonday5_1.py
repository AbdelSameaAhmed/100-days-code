# python file day 5 

# Ex for Dict
# Create dict and chick if specific key is existed or not,
# if not add with its value
# -----------------------------
# Solution
# -----------------------------

Employee = {
    "name" : "AS",
    "Age" : 33,
    "country" : "USA"
}

def testKey(key=""):
    if key in Employee.keys():
        print("this key is already in")
    else:
        Employee[key] = "val"
print(Employee)
# test function
testKey("phone")