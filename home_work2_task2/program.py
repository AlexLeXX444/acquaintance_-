# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input('Введите число N: '))

def multi_num (number):
    counter = 1
    for i in range(1, number + 1):
        counter *= i
    return counter

for i in range(1, num + 1):
    print(multi_num(i), end = " ")