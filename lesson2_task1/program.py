# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

import random

number = int(input('Введите количество членов последовательности:'))

for i in range (number):
    print(random.randint(-100,100), end = ' ')