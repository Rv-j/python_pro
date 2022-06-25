from limit import STUDENTS_LIMIT_IN_GROUP

class CheckGroup(Exception):
    def __init__(self, STUDENTS_LIMIT_IN_GROUP):
        super().__init__()
        self.limit = STUDENTS_LIMIT_IN_GROUP
    def __str__(self):
        return f"Sorry, this group is full, it can't have more than {self.limit} students."