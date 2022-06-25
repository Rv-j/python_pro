class Human:

    def __init__(self, age, growth, weight, sex, nat):
        if not isinstance(age, str) or not isinstance(growth, str) or not isinstance(weight, str) or not isinstance(sex,
                                                                                                                    str) or not isinstance(
                nat, str):
            raise TypeError()
        if not age:
            raise ValueError('is not empty age')
        if not growth:
            raise ValueError('is not empty growth')
        if not weight:
            raise ValueError('is not empty weight')
        if not sex:
            raise ValueError('is not empty sex')
        if not nat:
            raise ValueError('is not empty nationality')

        self.age = age
        self.growth = growth
        self.weight = weight
        self.sex = sex
        self.nat = nat

    def __str__(self):
        return f'Возраст: {self.age},\nРост: {self.growth},\nВес: {self.weight},\nПол: {self.sex},\nНациональность: {self.nat}'
