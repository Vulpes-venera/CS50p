def main():

    if check_number("AA222"):

        print("True")
    else:
        print("False")


def check_number(word):

    for i in word:
        if i.isdigit():
            index = word.index(i)
            if word[index:].isdigit():   # from index to the end of the string!
                return True


    # all negate or equal to False if even one if is False



main()