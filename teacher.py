from account import UserInfo
from student import Student


class Teacher(UserInfo):
    def __init__(self):
        super().__init__()
        self.lst_lesson = []  # список занятий учителя
        self.lst_student = []  # список учеников
