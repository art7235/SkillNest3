from account import UserInfo
from student import Student
from teacher import Teacher


class Lesson:
    def __init__(self, name, price, checkbox_field, teacher):
        self.name = name
        self.price = price  # цена
        self.checkbox_field = checkbox_field  # показатель галочки(либо True, либо False)
        self.teacher = teacher  # у урока должен быть владелец



