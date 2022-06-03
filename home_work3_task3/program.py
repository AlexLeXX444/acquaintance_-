# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

input_list = list(input('Введите список вещественных чисел через запятую: ').split(','))
maximum_num = float(input_list[0]) % 1
minimum_num = float(input_list[0]) % 1

def find_maximum (num_a: float, num_b: float):
    if (num_a % 1) > (num_b % 1):
        return num_a % 1
    else:
        return num_b % 1

def find_minimum (num_a: float, num_b: float):
    if (num_a % 1) < (num_b % 1):
        return num_a % 1
    else:
        return num_b % 1

for i in range(len(input_list)):
    if float.is_integer(float(input_list[i])) == False:
        maximum_num = find_maximum(float(input_list[i]), maximum_num)
        minimum_num = find_minimum(float(input_list[i]), minimum_num)
    else:
        maximum_num = find_maximum(float(input_list[i]), maximum_num)

print(f'Ответ: {round(maximum_num, 2) - round(minimum_num, 2)}')