def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        # only happens when all statements in (is_valid) is True
        print("Valid")
    else: 
        # only happens when even one of the if's inside is False
        print("Invalid")


def is_valid(s):
    if s[:].isalpha() == False:
        if 2 <= len(s) <=6: 
            if s[:2].isalpha():         # if False? then move to nex if True? then move to next if
                if check_number(s):                 # only goes down if check_number is TRUE
                    if s[:].isalnum():                     # only True when no specials found
                        return True


def check_number(word):

    for i in word:              # loop through the elements one by one
        if i.isalpha() == False:     
            if i == "0":        # if it is 0, end the loop and return False
                return False
            else:
                index = word.index(i)           # else find the index 
                if word[index:].isdigit():      # check from index to the end of the word for digits or not
                    return True                 # return True if all are digits
    
main()




