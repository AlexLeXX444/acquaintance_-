# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

num_list = list(input('Введите числа через пробел: ').split(' '))
num_min = num_max = num_list[0]

for i in range(1, len(num_list)):
    if num_max < num_list[i]:
        num_max = num_list[i]
    elif num_min > num_list[i]:
        num_min = num_list[i]
    else:
        continue

print(f'Большее число: {num_max} \nMеньшее число: {num_min}')