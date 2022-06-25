from human import Human


class Student(Human):

    def __init__(self, last_name, first_name, phone_number, age, growth, weight, sex, nat):
        if not isinstance(last_name, str) or not isinstance(first_name, str) or not isinstance(phone_number, str):
            raise TypeError()
        if not last_name:
            raise ValueError('is not empty last_name')
        if not first_name:
            raise ValueError('is not empty first_name')
        if not phone_number:
            raise ValueError('is not empty phone_number')
        super().__init__(age, growth, weight, sex, nat)
        self.last_name = last_name.strip().title()
        self.first_name = first_name.strip().title()
        self.phone_number = phone_number

    def __str__(self):
        return f'Фамилия: {self.last_name}, \nИмя: {self.first_name}, \nНомер телефона: {self.phone_number}, \n{super().__str__()}\n'
