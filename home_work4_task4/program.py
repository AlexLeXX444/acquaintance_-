# Задайте два целых числа. 
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

def finding_nod(num_1, num_2): 
    if num_1 > num_2: 
        min_num = num_2 
    else: 
        min_num = num_1 
    for i in range(1, min_num + 1): 
        if (num_1 % i == 0) and (num_2 % i == 0):
            nod = i 
    return nod
            
print(f'НОК (наименьшее общее кратное): {int(first_num * second_num / finding_nod(first_num,second_num))}')