from datetime import datetime

def main():
    time = input("What time is it? ")
    clean_time = time.replace(".","").strip().upper()
    temp_ti = datetime.strptime(clean_time, "%I:%M %p")
    new_time = temp_ti.strftime("%H:%M")
    hours = convert(new_time)
    if 8.0 >= hours >= 7.0:
        print("breakfast time")
    elif 14.0 >= hours >= 13.0:
        print("lunch time")
    elif 20.0 >= hours >= 19.0:
        print("dinner time")
    else:
        print()


def convert(time):
    num1, num2 = time.split(":")
    hours = float(num1)
    mins = float(num2)
    dec_hours = float(hours + mins / 60)

    return dec_hours


main()