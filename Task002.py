# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers = [2, 3, 4, 5, 6]

print('Original list: ' + str(numbers))
  
result = []
length = len(numbers)
if length % 2 == 0:
    for i in range(0, int(length/2)):
        result.append(numbers[i] * numbers[length - (i + 1)])
else:
    for i in range(0, int(length/2 + 1)):
        result.append(numbers[i] * numbers[length - (i + 1)])

print('Resulted list: ' + str(result))