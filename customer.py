class Customer:
    """
class Customer
"""

    def __init__(self, last_name, first_name, patronymic, phone_number):
        """

        :param last_name:
        :param first_name:
        :param patronymic:
        :param phone_number:
        """
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def __str__(self):
        """

        :return:
        """
        return f'{self.last_name} {self.first_name} {self.patronymic}; {self.phone_number}'



