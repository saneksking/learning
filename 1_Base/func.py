"""Функции в Python - это как функции в математике.
Они принимают некоторые значения (входные данные),
выполняют некоторые операции над ними и возвращают результат (выходные данные).
"""


def hello(name):
    print(f"Hello {name}!")


hello('Alex')
print('-' * 80)


def summa(num1, num2):
    equals = num1 + num2
    return equals


result = summa(55, 57)
print(result)
"""Определение функции:
Определение функции - это создание функции с определённым именем,
параметрами (если они есть) и блоком кода, который будет выполняться при вызове функции."""
print('-' * 80)


def say_hello():
    print('Hello, world!')


"""Вызов функции: Вызов функции означает выполнение блока кода, который определен в функции."""
say_hello()
print('-' * 80)
"""Параметры функций - это переменные,
которые объявляются в определении функции и используются для принятия значений,
передаваемых в функцию при ее вызове.
Параметры помогают функции работать с разными данными, которые передаются в нее."""


def greet(name, age=30):
    print(f"Hello {name}, you're {age}")


greet("Steve")
"""Аргументы функций - это конкретные значения, передаваемые в функцию при ее вызове.
Аргументы используются для заполнения параметров функции и предоставления функции нужных данных для работы."""
print('-' * 80)
"""Возвращаемое значение функции - это результат выполнения функции,
который она "возвращает" после своей работы. Когда функция выполняет определенные операции,
она может использовать эти результаты и вернуть их в виде значения,
которое мы можем сохранить или использовать дальше в программе."""


def multiply(num1, num2):
    res = num1 * num2
    return res


print(multiply(45, 5))
print('-' * 80)
"""Также важно учитывать, что функция может вернуть только одно значение.
Однако, это значение может быть составным типом данных,
таким как список (list) или кортеж (tuple), чтобы вернуть несколько значений одновременно."""


def get_name_length(name):
    length = len(name)
    uppercase_name = name.upper()
    return length, uppercase_name


name_info = get_name_length("Smith")
print(name_info)
print(f"Длина имени: {name_info[0]}, Имя заглавными буквами: {name_info[1]}")
