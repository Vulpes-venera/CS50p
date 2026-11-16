def main():

    user = input("Enter the plate: ")

    if check_number(user):
        print("True")
    else:
        print("False")


def check_number(word):

    for i in word:
        print(i)
        if i == "0":
            return False
        else:
            index = word.index(i)
            if word[index:].isdigit():
                return True
            

    # all negate or equal to False if even one if is False

main()