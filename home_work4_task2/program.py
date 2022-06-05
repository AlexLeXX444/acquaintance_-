# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num_fibo = abs(int(input('Введите число: ')))
list_fibo = [-1, 0, 1]

def fibonacci(number):
    current_num = 1
    if number > 2:
        current_num = fibonacci(number-1) + fibonacci(number-2)
    return current_num

if num_fibo > 1:
    for i in range(2, num_fibo + 1):
        list_fibo.append(fibonacci(i))
        list_fibo.insert(0, (fibonacci(i) * -1))
    print(list_fibo)
elif num_fibo == 1:
    print(num_fibo)
else:
    print(num_fibo)