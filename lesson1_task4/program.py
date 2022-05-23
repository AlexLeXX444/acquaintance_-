# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

number = float(input('Введите число:'))
int_number = int((number * 10) % 10)

if int_number != 0:
    print(f'{number} -> {int_number}')
else:
    print(f'{number} -> нет')