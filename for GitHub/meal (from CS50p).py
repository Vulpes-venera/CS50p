from datetime import datetime

def main():
    time = input("What time is it? ")
    clean_time = time.replace(".","").strip().upper()
    temp_ti = datetime.strptime(clean_time, "%I:%M %p")
    new_time = temp_ti.strftime("%H:%M")
    float_new_time = convert(new_time)
    if 8.0 >= float_new_time >= 7.0:
        print("breakfast time")
    elif 14.0 >= float_new_time >= 13.0:
        print("lunch time")
    elif 20.0 >= float_new_time >= 19.0:
        print("dinner time")
    else:
        print()


def convert(time):
    num1, num2 = time.split(":")
    hours = float(num1)
    mins = float(num2)
    dec_hours = float(hours + mins / 60)

    return dec_hours

if __name__ == __main__:
    main()