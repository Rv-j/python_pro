from limit import STUDENTS_LIMIT_IN_GROUP
from checkgroup import CheckGroup


class Group:

    def __init__(self, title: str):
        self.title = title
        self.students = []

    def add_student(self, student):
        try:
            if student not in self.students and len(self.students) < STUDENTS_LIMIT_IN_GROUP:
                self.students.append(student)
            else:
               raise CheckGroup(STUDENTS_LIMIT_IN_GROUP)
        except CheckGroup as err:
                print(err)

    def del_student(self, student):
        if student not in self.students:
            raise Exception('There is no student with this last name')
        self.students.remove(student)

    def search_by_lastname(self, value):
        res = [stud for stud in self.students if stud.last_name == value]
        return res

    def __str__(self):
        return '\n'.join(map(str, self.students))
