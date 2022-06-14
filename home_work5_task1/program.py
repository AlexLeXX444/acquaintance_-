# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2   =>   2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


stepen = int(input('Введите натуральную степень: '))
answer = []

# Если коэффициент равен нулю, то уравнение теряет смысл и такие значения НЕ учитываются !!!
# Приобретает вид 0*x² + 4*x + 5 = 0 => 4*x + 5 = 0
for i in range(stepen + 1):
    element = randint(0,5)
    if element > 0:
        if (stepen - i) > 1:
            answer.append(f'{element}*x^{stepen - i}')
        elif (stepen - i) < 1:
            answer.append(f'{element}')
        else:
            answer.append(f'{element}*x')
    else:
        continue

print(' + '.join(answer) + ' = 0')