# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Enter a number: '))

# Method 1
print(bin(num)[2:])

# Method 2
# def decimal_to_binary(num):
#     if int(num) >= 1:
#         decimal_to_binary(int(num) // 2)
#     print(int(num) % 2, end = '')
# decimal_to_binary(num)

# Method 3
# def decimal_to_binary(n):
#     return "{0:b}".format(int(n))
# print(decimal_to_binary(num))