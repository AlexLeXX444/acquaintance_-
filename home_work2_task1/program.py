# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр(отсекаем минус, считаем все в плюс).
import re

number_string = re.sub("[-|.|,| ]","",input('Введите число: '))
counter = 0

for i in range(len(number_string)):
    counter += int(number_string[i])

print(counter)