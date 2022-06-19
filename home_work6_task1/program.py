# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

import read_function_from_file
import parse_nums_from_element

print('Первое уравнение:')
print(" ".join(read_function_from_file.file_read("file1.txt")))

print('Второе уравнение:')
print(" ".join(read_function_from_file.file_read("file2.txt")) + "\n")

first_equation = read_function_from_file.spisok_koefficientov("file1.txt")
second_equation = read_function_from_file.spisok_koefficientov("file2.txt")
answer_equation = []

for i in range (len(first_equation)):
    is_equeals = False
    for j in range(len(second_equation)):
        if parse_nums_from_element.parse_no_nums(first_equation[i]) == parse_nums_from_element.parse_no_nums(second_equation[j]):
            is_equeals = True
            first_num = int(parse_nums_from_element.parse_nums(first_equation[i]))
            second_num = int(parse_nums_from_element.parse_nums(second_equation[j]))
            answer_equation.append(f'{first_num + second_num}{parse_nums_from_element.parse_no_nums(first_equation[i])}')
    if not is_equeals:
        answer_equation.append(f'{first_equation[i]}')


for i in range (len(answer_equation)):
    if (int(parse_nums_from_element.parse_nums(answer_equation[i]))) <= 1:
        answer_equation[i] = parse_nums_from_element.parse_no_nums(answer_equation[i])

print(answer_equation)