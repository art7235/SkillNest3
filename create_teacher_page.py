import webbrowser
import os

def create_student_page():
    html_content = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Страница ученика</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        .container {
            display: flex;
            justify-content: space-between;
        }
        .section {
            width: 48%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<header>
    <h1>Страница ученика</h1>
    <button onclick="window.location.href='teacher_page.html'">Переключиться на учителя</button>
</header>

<div class="container">
    <div class="section">
        <h2>Занятия</h2>
        <p>Список доступных занятий.</p>
    </div>
    <div class="section">
        <h2>Мои занятия</h2>
        <p>Список ваших занятий.</p>
    </div>
</div>

</body>
</html>'''

    file_path = 'student_page.html'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    webbrowser.open('file://' + os.path.realpath(file_path))

def create_teacher_page():
    html_content = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Страница учителя</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        .container {
            display: flex;
            justify-content: space-between;
        }
        .section {
            width: 48%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<header>
    <h1>Страница учителя</h1>
    <button onclick="window.location.href='student_page.html'">Переключиться на ученика</button>
</header>

<div class="container">
    <div class="section">
        <h2>Занятия</h2>
        <p>Список занятий, которые вы преподаете.</p>
    </div>
    <div class="section">
        <h2>Отклики</h2>
        <p>Список людей, которые откликнулись.</p>
    </div>
</div>

</body>
</html>'''

    file_path = 'teacher_page.html'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    webbrowser.open('file://' + os.path.realpath(file_path))

# Создаем обе страницы
create_student_page()
create_teacher_page()