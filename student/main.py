
from student import Student
from group import Group

stud_1 = Student('Ванюшин', 'Ваня', '063111111', '21', '175', '55', 'Мужской', 'Украинец')
stud_2 = Student('Ретрцши', 'Петя', '063222222', '22', '174', '58', 'Мужской', 'Украинец')
stud_3 = Student('Герась', 'Хайлим', '063333333', '21', '168', '66', 'Мужской', 'Татарин')
stud_4 = Student('Романен', 'Гарик', '063444444', '19', '168', '63', 'Мужской', 'Узбек')
stud_5 = Student('Мукровец', 'Витя', '063555555', '21', '190', '90', 'Мужской', 'Украинец')
stud_6 = Student('Квандзи', 'Луйчи', '0636666666', '24', '160', '50', 'Мужской', 'Китаец')
stud_7 = Student('Сидоров', 'Ваня', '0637777777', '21', '175', '120', 'Мужской', 'Украинец')
stud_8 = Student('Джерсон', 'Стив', '063000000', '28', '190', '90', 'Мужской', 'Американец')
stud_9 = Student('Лерчин', 'Света', '0688888888', '24', '155', '49', 'Женский', 'Украинка')
stud_10 = Student('Вальчи', 'Виктор', '0639999999', '23', '175', '65', 'Мужской', 'Украинец')
stud_11 = Student('Джерсон', 'Стив', '063000000', '28', '190', '90', 'Мужской', 'Американец')
stud_12 = Student('Киткси', 'Саманта', '063005660', '18', '170', '50', 'Женский', 'Американка')

group_mku_87 = Group('new')
group_mku_87.add_student(stud_1)
group_mku_87.add_student(stud_2)
group_mku_87.add_student(stud_3)
group_mku_87.add_student(stud_4)
group_mku_87.add_student(stud_5)
group_mku_87.add_student(stud_6)
group_mku_87.add_student(stud_7)
group_mku_87.add_student(stud_8)
group_mku_87.add_student(stud_9)
group_mku_87.add_student(stud_10)
group_mku_87.add_student(stud_11)
group_mku_87.add_student(stud_12)

print(group_mku_87)
