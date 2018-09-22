"""
Create class representing money in different currencies.
It has to support the operations from main part:
"""
import requests

API_KEY = '2b9234b6039f13df6f10a63b'
CURRENCIES_URL = 'https://v3.exchangerate-api.com/bulk/{}/{}'


class Money(object):

    def __init__(self, value, currency='USD'):
        self.value = value
        self.currency = currency

    def __str__(self):
        return ('{:.2f}'.format(self.value)) + " " + self.currency

    def get_current_currencies(self):
        currencies = requests.get(CURRENCIES_URL.format(API_KEY,
                                                        self.currency))
        return currencies.json()

    def __add__(self, money):
        if not isinstance(money, self.__class__):
            return self.__radd__(money)
        if self.currency == money.currency:
            new_value = self.value + money.value
        else:
            money_currency = self.get_current_currencies()['rates'].get(money.currency, None)
            new_value = self.value + (money.value / money_currency)
        return Money(new_value, self.currency)

    def __radd__(self, money):
        if isinstance(money, self.__class__):
            return self + money
        return self

    def __sub__(self, money):
        if self.currency == money.currency:
            new_value = self.value - money.value
        else:
            money_currency = self.get_current_currencies()['rates'].get(money.currency, None)
            new_value = self.value - (money.value / money_currency)
        return Money(new_value, self.currency)

    def __mul__(self, k):
        ret = self.value * k
        return Money(ret, self.currency)

    def __rmul__(self, k):
        ret = self.value * k
        return Money(ret, self.currency)


if __name__ == '__main__':
    x = Money(10, "BYN")
    y = Money(11)  # “USD”
    z = Money(12.34, "EUR")
    print(z + 3.11 * x + y * 0.8)

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)
