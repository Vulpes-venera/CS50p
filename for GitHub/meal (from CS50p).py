from datetime import datetime

def main():
    time = input("What time is it? ")
    clean_time = time.replace(".","").strip().upper()
    temp_ti = datetime.strptime(clean_time, "%I:%M %p")
    new_time = temp_ti.strftime("%H:%M")
    print(new_time)
    print(convert(new_time))


def convert(time):
    num1, num2 = time.split(":")
    hours = float(num1)
    mins = float(num2)
    dec_hours = float(hours + mins / 60)

    return dec_hours


if __name__ == "__main__":
    main()