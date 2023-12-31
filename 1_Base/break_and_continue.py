"""Оператор break используется для прерывания выполнения цикла и выхода из него,
даже если условие цикла все еще истинно.
После выполнения оператора break программа продолжает выполнение со следующей инструкции за пределами цикла."""
for num in range(1, 11):
    if num == 5:
        break
    print(num)


print('-' * 80)
"""Оператор continue используется для пропуска текущей итерации цикла и перехода к следующей итерации.
В отличие от оператора break, который полностью прерывает цикл,
оператор continue возвращает управление в начало цикла,
и следующий элемент последовательности обрабатывается."""
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)
