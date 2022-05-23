# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
number = int(input('Введите число N: '))
string_numbers = ""
for i in range (-number, number + 1):
    string_numbers += str(f"{i}")
    if i != number:
        string_numbers += ", "

print(f'{number} -> {string_numbers}')