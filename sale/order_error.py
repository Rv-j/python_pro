class NegativeValueError(Exception):

    def __init__(self, price):
        super().__init__()
        self.price = price

    def __str__(self):
        return "Error.Input positive number."


try:
    price = float(input("Input price - "))
    if price >= 0:
        print (price)
    if price < 0:
        raise NegativeValueError(price)
except ValueError as err:
    print("Error. Use only numbers.")
except NegativeValueError as err:
    print(err)
