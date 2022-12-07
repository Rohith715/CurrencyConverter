def CurrencyConverter():
    with open("currencyData.txt") as f:
        lines = f.readlines()
    bold = '\33[1m'
    currencyName = []
    currencyDict = []
    print(bold + "Currency Converter")
    for line in lines:
        parsed = line.split("\t")
        currencyName.append(parsed[0])
        currencyDict.append(parsed[1])
    d = dict(zip(currencyName,currencyDict))
    amount = eval(input("Enter the amount you want to convert:\n"))

    print("The options for conversion are as follows:")
    [print(item) for item in d.keys()]
    print("\n")
    currency = input("Please enter the currency as mentioned above:\n")
    print(f"{amount} INR is equal to {amount * float(d[currency])} {currency}")
    print("\n")

while True:
    CurrencyConverter()