print("The loop will continue and keep going on.")

#creating an infitnite loop
while True:

    for _ in range(3):
        print("This will keep repeating in one line", end=' ')
    stoppage = input("Stop? ")
    if stoppage.lower() == "yeah":
        break

