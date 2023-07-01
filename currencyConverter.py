from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "7e72d893bfe95e29cdb1"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url_test = BASE_URL + endpoint
    data = get(url_test).json()['results']
    data = list(data.items())
    data.sort()
    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', "")
        print(f"{_id} - {name} - {symbol} ")


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()
    if len(data) == 0:
        print('Invalid currencies.')
        return
    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    return rate


def convert(currency1, currency2, amount):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print('invalid amount')

    result = amount * rate
    print(f"{amount} {currency1} is equal to {result} {currency2}")
    return result


def main():
    print("Welcome to the currency converter!\nList - lists the different currencies\nConvert - "
          "convert from one currency to another\nRate - get the exchange rate of two currencies\n")

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == 'q':
            break
        elif command == 'list':
            get_currencies()
        elif command == 'convert':
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == 'rate':
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print('Unrecognized command')

main()