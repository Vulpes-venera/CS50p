#user input as usual
user_in = input("Input: ")

#storing words in list
list1 = []
for i in user_in:
    # checking going on here, if yes then pass if no then append to list
    if i in "aeiou":
        pass
    else:
        list1.append(str(i))

#print final word without list brackets
final_word = print("".join(list1))
