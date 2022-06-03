# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Если остается 1 элемент без пары - умножаем его самого на себя.

num_list = list(input('Введиче список через запятую: ').split(','))
len_list = int(len(num_list))

if len_list % 2 != 0:
    len_list = int(len_list / 2) + 1
else:
    len_list = int(len_list / 2)

for i in range(len_list):
    print(int(num_list[i]) * int(num_list[int(len(num_list)) - (i + 1)]), end = " ")