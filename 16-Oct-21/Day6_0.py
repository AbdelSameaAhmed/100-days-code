# ------------Tuple
# 
d = {}
d[1] = "as"
d[2] = "ff"
d[3] = 'qq'
d[4] = "gg"

# print(d)
# print(d.items())

# print("*"*50)
for (k,i) in d.items():
    print(k,i)

# help(dict)

# ------------------
# tow dim dictionary
lang = {
    "first" : {
        "name": "HTML",
        "type": "Web Language",
        "potential" : "middel"
    },
    "second": {
        "name" : "CSS",
        "type": "Web Language",
        "potential" : "middel"

    },
    "third": {
        "name" : "JS",
        "type": "prog",
        "potential": "good"
    }

}
print(lang)
print("*" * 60)
print(lang["third"])
print("*" * 60)
print(lang.keys())
print("*" * 60)
print(lang.items())
print("*" * 60)
print(lang.get("first"))
print("*" * 60)
print(len(lang))
print(len(lang["first"]))

