from account import UserInfo
from student import Student
from teacher import Teacher


class Lesson:
    def __init__(self, name, price, is_chosen, teacher):
        self.name = name
        self.price = price  # цена
        self.is_chosen = is_chosen  # показатель галочки(либо True, либо False)
        self.teacher = teacher  # у урока должен быть владелец



