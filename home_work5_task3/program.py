# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

input_list = list(input('Введите числа через пробел: ').split(' '))
unique_list = list(set(input_list))
answer_list = []


for i in range(len(unique_list)):
    counter = 0
    for j in range(len(input_list)):
        if unique_list[i] == input_list[j]:
            counter += 1
    if counter > 1:
        answer_list.append(unique_list[i])
        
answer_list.sort()
print(answer_list)