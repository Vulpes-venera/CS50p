#hardcode this exchange rate table
exchange_values = {
    "USD": 0.0105,
    "EUR": 0.0094,
    "GBP": 0.0079,
    "AUD": 0.0150,
    "CAD": 0.0148,
    "CHF": 0.0086,
    "JPY": 1.6532
}

print("---------------------")
amount = float(input("Enter INR Amount?: "))
print("Choose from: USD, EUR, GBP, AUD, CAD, CHF, JPY")
convert_to = input("Convert to?: ").upper()

print("---------------------")
if convert_to in exchange_values:
    final_amount = amount * exchange_values[convert_to]
    print(f"{final_amount:.2f} {convert_to}")

elif convert_to not in exchange_values:
    print("Sorry, that conversion is not available.")
    print("Available → USD, EUR, GBP, AUD, CAD, CHF, JPY")

else:
    print("Invalid!. Retry.")





