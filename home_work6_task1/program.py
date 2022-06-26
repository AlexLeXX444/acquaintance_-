# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

import create_polinom
import read_function_from_file
import functions_equation

# создадим файлы с уравнениями
create_polinom.create_file_polinomial(7, "file1.txt")
create_polinom.create_file_polinomial(5, "file2.txt")

func_str = read_function_from_file.spisok_koefficientov("file1.txt") + read_function_from_file.spisok_koefficientov("file2.txt")
answer_str = []

for i in range (len(func_str)):
    is_equeals = 0
    for j in range (i + 1, len(func_str)):
        if functions_equation.equation_f_x(func_str[i]) == functions_equation.equation_f_x(func_str[j]):
            is_equeals = 1
            answer_str.append(f'{functions_equation.equation_summ(func_str[i], func_str[j])}')
            func_str[i] = '0'
            func_str[j] = '0'
        elif functions_equation.is_number(func_str[i]) and functions_equation.is_number(func_str[j]):
            if func_str[i] != '0' and func_str[j] != '0':
                is_equeals = 1
                answer_str.append(f'{functions_equation.equation_summ(func_str[i], func_str[j])}')
                func_str[i] = '0'
                func_str[j] = '0'
    if is_equeals == 0:
        answer_str.append(f'{func_str[i]}')
        func_str[i] = '0'

while("0" in answer_str) :
    answer_str.remove("0")



with open("answer.txt", 'w') as new_file:
        new_file.write(f'{" + ".join(answer_str)} = 0')
new_file.close()