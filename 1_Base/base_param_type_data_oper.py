"""Переменные являются контейнерами для хранения данных в программе.
Вы можете думать о переменных как о коробках, в которых можно положить различные значения.
Переменные имеют имя, по которому вы можете обращаться к ним, и значение, которое они содержат."""
x = 5
"""Типы данных определяют, какие виды значений можно хранить в переменных.
В Python есть несколько основных типов данных:"""
'''Целые числа (integer) - это числа без десятичной точки. Например: 1, 10, -5.'''
y = 10
'''Вещественные числа (float) - это числа с десятичной точкой. Например: 3.14, -0.5, 2.0.'''
z = 5.54
'''Строки (string) - это последовательности символов, заключенные в кавычки. Например: "Привет", 'Мир'.'''
string = 'Hello'
'''Булевы значения (boolean) - это значения True (истина) или False (ложь).
Они используются для логических операций.'''
is_true = True
print(type(y), type(z), type(string), type(is_true))
"""Операторы - это символы или ключевые слова, которые позволяют выполнять операции над данными.
В Python есть различные виды операторов,
включая арифметические операторы, операторы сравнения и логические операторы."""
summa = 5 + 8
subtraction = 15 - 8
multiplication = 8 * 2
division = 14 / 2
print('-' * 80)
print(summa, '-', subtraction, '-', multiplication, '-', division)
print('-' * 80)
one = 56
two = 75
is_greater = two > one
print(is_greater)
print('-' * 80)
true = True
false = False
result = true and false
print(result)

