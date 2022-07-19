# excercise 01
# # reverse every word in str1 where str1 = 'My Name is Jessa'
# # output: 'Jessa is Name My'
str1 = 'My Name is Jessa'
str2 = ''
for i in range(len(str1)):
    if str1[i] == ' ':
        str2 = str2 + str1[i]
    else:
        str2 = str2 + str1[len(str1)-i-1]
print(str2)
