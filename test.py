# 1 На минимальное знание python: Написать функцию, получающую параметр строку и
# возвращающую "перевёрнутую" строку, например 'abc' -> 'cba'. Написать программу,
# использующую эту функцию. В тестирующей программе достаточно простого фиксированного
# набора обрабатываемых строк. Реализовать 2мя способами.

# Реализация 1

def reverse_string(str):
    return str[::-1]


test_string = 'abc'

print(reverse_string(test_string))


# Реализация 2

def reverse_string(str):
    reversed_str = ''
    for i in range(len(str) - 1, -1, -1):
        reversed_str += str[i]
    return reversed_str


test_string = 'abc'

print(reverse_string(test_string))

# 2 На минимальное владение Qt: Написать программу, которая будет использовать форму для
# ввода исходной строки и выводить перевёрнутую.Необходимо использовать функцию,
# написанную для задачи 1

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


def reverse_string(string):
    return string[::-1]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем виджет для ввода исходной строки
        self.input_line_edit = QLineEdit(self)
        self.input_line_edit.setGeometry(50, 50, 200, 30)

        # Создаем кнопку для запуска функции переворота строки
        self.reverse_button = QPushButton("Перевернуть", self)
        self.reverse_button.setGeometry(50, 100, 200, 30)
        self.reverse_button.clicked.connect(self.reverse_string)

        # Создаем виджет для вывода перевернутой строки
        self.output_label = QLabel(self)
        self.output_label.setGeometry(50, 150, 200, 30)
        self.output_label.setAlignment(Qt.AlignCenter)

        # Настраиваем окно
        self.setWindowTitle("Перевернуть строку")
        self.setGeometry(100, 100, 300, 250)
        self.show()

    def reverse_string(self):
        # Получаем исходную строку из виджета QLineEdit
        input_string = self.input_line_edit.text()

        # Вызываем функцию переворота строки из задачи 1
        reversed_string = reverse_string(input_string)

        # Выводим перевернутую строку в виджет QLabel
        self.output_label.setText(reversed_string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


# 3 На минимальное владение SQL: написать запросы:
# 3.1. Создать таблицу c описанием простейшего списка людей - фамилия, имя, отчество, возраст.
CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT,
    first_name TEXT,
    middle_name TEXT,
    age INTEGER
);

# 3.2. Заполнить эту таблицу 5-10 записями.
INSERT INTO people (last_name, first_name, middle_name, age)
VALUES
    ('Иванов', 'Иван', 'Иванович', 30),
    ('Петров', 'Петр', 'Петрович', 25),
    ('Сидоров', 'Сидор', 'Сидорович', 40),
    ('Кузнецов', 'Андрей', 'Андреевич', 22),
    ('Смирнова', 'Мария', 'Александровна', 28),
    ('Ковалев', 'Виктор', 'Игоревич', 35);

# 3.3. Выбрать людей с заданной фамилией
SELECT * FROM people WHERE last_name = 'Иванов';

# 3.4. Увеличить возраст на 1 для людей с заданной фамилией
UPDATE people SET age = age + 1 WHERE last_name = 'Иванов';

# 3.5. Удалить записи с заданной фамилией
DELETE FROM people WHERE last_name = 'Иванов';

#4 Написать модуль отправки пациентов на python 2.7.
# Описание сервиса http://r23-rc.zdrav.netrika.ru/exlab_example/doc/oip.pdf раздел «4.5.1.
# Передача пациента (POST Patient)» , требуется добавить только обязательные параметры, которые
# имею кратность 1.1. в качесте адреса указать «www.test.wsdl»

import requests
import json

url = 'www.test.wsdl/Patient?_format=json'

headers = {'Content-Type': 'application/json'}

data = {
  "resourceType": "Patient",
  "name": [
    {
      "use": "anonymous",
      "given": [
        "Анонимный"
      ],
      "family": "Аноним"
    }
  ],
  "identifier": [
    {
      "system": "МИС/ЛИС",
      "value": "идентификатор пациента в МИС"
    }
  ],
  "managingOrganization": {
    "display": "OID передающей системы"
  }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 201:
    print('Пациент успешно зарегистрирован в сервисе ДЛИ')
    patient = response.json()
    print('Идентификатор пациента в сервисе ДЛИ:', patient['id'])
else:
    print('Ошибка регистрации пациента в сервисе ДЛИ:', response.text)
