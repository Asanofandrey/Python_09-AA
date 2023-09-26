"""Использование встроенного filter. 
Функция filter() принимает два параметра. 
Первый — имя созданной пользователем функции, 
а второй — итерируемый объект 
(список, строка, множество, кортеж и так далее)."""

# filter(функци, последовательность)

numbers = [1, 2, 3, 4, 5, 4, 16, 2, 24]

print(list(filter(lambda number: number >= 3, numbers)))
