mydict = {1, 3, 5, 10, 9}

mydict1 = {
    "name" : "asa",
    "mail" : "asa@gmail.com",
    "address" : "12 fsd st",
    "phone" : "22345353"
}
print(mydict1)

print(mydict1.get("name"))


Emp = {
  "name": "asa",
  "age": 33,
  "phone": 1964,
  "country" : "USA"
}
# x = Emp["age"]
# print(x)
# print(Emp.keys())
# print(Emp.values())
# print(Emp.items())
Emp["Height"] = 170

print(Emp.items())
print(Emp)