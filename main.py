from account import UserInfo
from student import Student
from teacher import Teacher
from lesson import Lesson

lesson_lst = []
account_lst = []


def registration(first_name, last_name, email, password, date_of_birth, phone, name):
    new_id = UserInfo()
    new_id.last_name = last_name
    new_id.first_name = first_name
    new_id.phone = phone
    new_id.email = email
    new_id.password = password
    new_id.date_of_birth = date_of_birth
    new_id.name = name
    for i in account_lst:
        if new_id.name == i.name:
            return "такое имя уже существует"
    account_lst.append(new_id)
    return "Регистрация успешна"


def add_lesson(lesson, student):  # добавить урок в список
    student.lst.append(lesson)
    lesson.checkbox_field = True  # знак того, что под предмеьом есть галочка
    lesson.teacher.lst_student.append(student)  # добавляем ученика в список учителя


def delete_lesson(lesson, student):  # удалить урок из списка
    student.lst.remove(lesson)
    lesson.teacher.lst_student.remove(student)  # удаляем ученика из списка учителя
    lesson.checkbox_field = False  # убераем галочку


def add_lesson_teacher(lesson, teacher):  # добавить урок(функция учителя)
    teacher.lst_lesson.append(lesson)
    lesson_lst.append(lesson)


def delete_lesson_teacher(lesson, teacher):  # удалить урок
    teacher.lst_lesson.remove(lesson)
    lesson_lst.remove(lesson)


s1 = Student()  # дальше идут проверки

s1.last_name = "12345"
s1.first_name = "qwert"
s1.phone = 872093747
s1.email = "art7235"
s1.password = "1234567"
s1.date_of_birth = 230325

t1 = Teacher()

t1.last_name = "12345"
t1.first_name = "qwert"
t1.phone = 872093747
t1.email = "art7235"
t1.password = "1234567"
t1.date_of_birth = 230325

print(s1.email)
print(t1.phone)

l1 = Lesson("русс", 600, False, t1)

add_lesson(l1, s1)
print(s1.lst)

add_lesson_teacher(l1, t1)
print(t1.lst_lesson)

print(t1.lst_student)

delete_lesson(l1, s1)

print(s1.lst)
