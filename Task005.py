# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def Fibonacci(n):
#     first = 0
#     second = 1
#     print(first, second, end= " ")
#     for i in range(2, n):
#         next = first + second
#         print(next, end = " ")
#         first = second
#         second = next

n = 8
positive = []
negative = []

def fib(list, n):
    list.append(0)
    list.append(1)
    for i in range(2, n + 1):
        list.append(list[i - 2] + list[i - 1])
    return list

def neg_fib(list, n):
    list.append(0)
    list.append(1)
    for i in range(2, n + 1):
        list.append(list[i - 2] - list[i - 1])
    list.pop(0)
    list.reverse()
    return list

# res_list = [y for x in [neg_fib(negative, n), fib(positive, n)] for y in x]
# print (str(res_list))

res_list = neg_fib(negative, n) + fib(positive, n)
print (str(res_list))