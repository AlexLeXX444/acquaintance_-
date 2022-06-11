# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open("some_nums.txt",'r') as f_text:  
    content = list(f_text.read().split(' '))
    counter = 0
    for i in range(1, len(content)):
        if int(content[i]) != (int(content[i-1]) + 1):
            print(f'{int(content[i]) - 1}', end = ' ')
        else:
            counter += 1
    if counter == len(content) - 1:
        print('Нет пропусков элементов.')