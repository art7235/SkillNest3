from account import UserInfo
from student import Student
from teacher import Teacher
from lesson import Lesson

lesson_lst = []
account_lst = []


def registration(first_name, nickname, last_name, email, password, phone):
    new_user = UserInfo()
    new_user.last_name = last_name
    new_user.first_name = first_name
    new_user.phone = phone
    new_user.email = email
    new_user.password = password
    new_user.nickname = nickname
    for i in account_lst:
        if new_user.nickname == i.nickname:
            return "такое имя уже существует"
    account_lst.append(new_user)
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


registration("миха", "миша", "шишкин", "12345", "123456789", 89650578724)

print(account_lst[0].name)
