# - Looping and dictionaries
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key,counts[key])

print("*" * 40)
print("*" * 40)
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10 :
        print(key, counts[key])
print("*" * 40)
print("*" * 40)

# ---------------- String Module ------------------------
# -------------------------------------------------------
import string
