# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

num_list = list(input('Введиче список через запятую: ').split(','))
summ_elements = 0

for i in range(len(num_list)):
    if i%2 != 0:
        summ_elements += int(num_list[i])

print(f'Сумма элементов списка стоящих на нечетной позиции: {summ_elements}')