# функции для работы с уравнениями

# проверяем, получили на вход положительное/отрицательное целое/с плавающей точой число
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def equation_summ (eq_a, eq_b):
    eq_answer = ''
    if is_number(eq_a) and is_number(eq_b):
        return f'{int(eq_a) + int(eq_b)}'
    else:
        if equation_num(eq_a) + equation_num(eq_b) == 1:
            return f'{equation_f_x(eq_a)}'
        else:
            return f'{equation_num(eq_a) + equation_num(eq_b)}*{equation_f_x(eq_a)}'

# выделяем из куска функции целочисленный коэффициент
def equation_num (eq_func):
    index_x = eq_func.find('x')
    number_x = ''
    if index_x > 0:
        for i in range (index_x - 1):
            number_x += eq_func[i]
        return int(number_x)
    else:
        return 1

# отделяем остатки функции
def equation_f_x (eq_func):
    index_x = eq_func.find('x')
    eq_f_x = ''
    if len(eq_func) > 0:
        for i in range (index_x, len(eq_func)):
            eq_f_x += eq_func[i]
        return eq_f_x
    else:
        return eq_f_x