# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2   =>   2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def create_file_polinomial (stepen, file_name):
    answer = []

    # Если коэффициент равен нулю, то уравнение теряет смысл и такие значения НЕ учитываются !!!
    # Приобретает вид 0*x² + 4*x + 5 = 0 => 4*x + 5 = 0
    for i in range(stepen + 1):
        element = randint(0,100)
        if element > 0:
            if (stepen - i) > 1:
                answer.append(f'{element}*x^{stepen - i}')
            elif (stepen - i) < 1:
                answer.append(f'{element}')
            else:
                answer.append(f'{element}*x')
        else:
            continue

    answer_str = ' + '.join(answer) + ' = 0'

    with open(file_name, 'w') as new_file:
        new_file.write(answer_str)
    new_file.close()