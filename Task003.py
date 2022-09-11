# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 5, 10.01]

def only_decimal(list):
    decimal = []
    for i in range(0, len(list)):
        if list[i] % 1 != 0:
            decimal.append(round(list[i] % 1, 2))
    return decimal
    
def diff(list):
    for i in range(0, len(list)):
        diff = max(list) - min(list)
    return diff

decimal = (only_decimal(numbers))
print(diff(decimal))