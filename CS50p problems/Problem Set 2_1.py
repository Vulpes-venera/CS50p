#taking some user input
str1 = input("camelCase: ")

list1 = []
for c in str1:
    if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        list1.append(" " + c)
    else:
        list1.append(c)


str2 = "".join(list1)
str3 = str2.replace(" ","_")
print("snake_case:",str3.lower())