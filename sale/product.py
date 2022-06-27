class Product:
    """
class Product:
"""
    def __init__(self, title, dimensions, price):
        """

        :param title:
        :param dimensions:
        :param price:
        """
        self.title = title
        self.dimensions = dimensions
        self.price = price

    def __str__(self):
        """

        :return:
        """
        return f'{self.title}: {self.dimensions}: {self.price:.2f} UAH'