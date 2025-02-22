from account import UserInfo


class Student(UserInfo):
    def __init__(self):
        super().__init__()
        self.lst = []  # список уроков
