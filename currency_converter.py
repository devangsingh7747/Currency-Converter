# def currency_converter(amount, from_currency, to_currency):
#     # Hardcoded exchange rates (replace with actual rates or fetch from an API)
#     exchange_rates = {
#         'INR': {'EUR': 0.011, 'JPY': 1.86, 'USD': 0.012},
#         'USD': {'EUR': 0.94, 'JPY': 154.90, 'INR': 83.3},
#         'EUR': {'USD': 1.07, 'JPY': 165.58, 'INR': 89.04},
#         'JPY': {'USD': 0.0065, 'EUR': 0.0060, 'INR': 0.54}
#     }

#     if from_currency == to_currency:
#         return amount

#     if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
#         return "Invalid conversion"

#     rate = exchange_rates[from_currency][to_currency]
#     converted_amount = amount * rate
#     return converted_amount

# def main():
#     print("Welcome to the Currency Converter")
#     print("---------------------------------")
#     amount = float(input("Enter the amount to convert: "))
#     from_currency = input("Enter the currency to convert from (e.g., USD, EUR, INR, JPY): ").upper()
#     to_currency = input("Enter the currency to convert to (e.g., USD, EUR, INR, JPY): ").upper()

#     converted_amount = currency_converter(amount, from_currency, to_currency)
#     if isinstance(converted_amount, str):
#         print(converted_amount)
#     else:
#         print("Converted amount:", converted_amount)

# if __name__ == "__main__":
#     main()
