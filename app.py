from flask import Flask, render_template, request
from main import registration
import webbrowser
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/registration')
def registration():
    last_name = request.args.get('last_name', 'инкогнито')
    first_name = request.args.get('first_name', 'инкогнито')
    phone = request.args.get('phone', '')
    email = request.args.get('email', '')
    password = request.args.get('password', '')
    nickname = request.args.get('nickname', 'user')
    registration(last_name, first_name, phone, email, password, nickname)


@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return name + str(id)


@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    return render_template('hello.html', name=name)

def create_and_open_html():
    # HTML-код страницы
    html_content = """<!DOCTYPE html>
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
    <button>Переключиться</button>
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
</html>"""

    # Сохранение HTML-кода в файл
    file_path = 'student_page.html'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    # Открытие файла в веб-браузере
    webbrowser.open('file://' + os.path.realpath(file_path))

# Вызов функции
create_and_open_html()


if __name__ == "__main__":
    app.run(debug=True)
