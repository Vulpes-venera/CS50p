def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        # only happens when all statements in is_valid is True
        print("Valid")
    else: 
        # only happens when even one is False
        print("Invalid")


def is_valid(s):

    if (len(s) >= 2 and len(s) <= 6):   # if True? then move to next if
        if s[0:2].isalpha():            # if True? then move to next if
            if check_number(s):   # only goes down if check_number is TRUE?
                return True




            else:
                return False
        else:
            return False
    else:
        return False

def check_number(word):

    for i in word:
        if i.isdigit():   # checks from which index does a digit start
            index = word.index(i)    # finds the index(digit index)
            if word[index:].isdigit():   # from index to the end of the string! checks if they are digits
                return True
    

main()




