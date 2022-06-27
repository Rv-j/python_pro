from uuid import uuid4
import datetime


class Order:
    count = 0
    """
class Order:
"""
    def __init__(self, customer=None):
        """

        :param customer:
        """
        self.id = uuid4()
        self.date = datetime.datetime.now()
        self.customer = customer
        self.products = []
        Order.count += 1

    def get_total_price(self):
        """

        :return:
        """
        summa = 0
        for item in self.products:
            summa += item.price
        return summa

    def __str__(self):
        """

        :return:
        """
        res = f'{self.id} \n {self.customer} \n Products: \n'
        res += '\n' .join(map(str, self.products))
        res += f'\nTotal price: {self.get_total_price() } grn. \n'
        return res

    @classmethod
    def get_orders_count(cls):
        return cls.count
