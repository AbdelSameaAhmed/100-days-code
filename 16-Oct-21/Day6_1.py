# Dict methods

# clear(), update()
user = {}

user.update({"name": "ASA"})
user.update({"age": 33, "country": "USA"})
print(user)
# user.clear()
print(user)

# -----------------------
# copy()
a = user.copy()
print(a)
# --------------------
# Keys() , values()
print(user.keys())
print(user.values())


# --------------------
# setdefault(key, value=None) 

user.setdefault("phone")
print(user)
user.setdefault("skills" , "fighting")
print(user)

# ------------------------
# popitem()
user.popitem()
print(user)
user.update({"play" : "football"})
print(user)
print(user.popitem())
# ------------------------------
# items
print(user.items())

# -----------------------------------
# ex:

print("*" * 70)
a = user.items()
print(a)
# print(sorted(a))
print("*" * 70)
for k, v in a:
    print(k, v)
print(type(a))
print("*" * 70)
tem = []
for k, v in a:
    tem.append((k, v))
print(tem)
print(sorted(tem))