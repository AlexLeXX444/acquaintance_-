# Принимает на вход название файла, открывает его, считывает строку с многочленом и возвращает:

# - всё уравнение в виде списка. 
def file_read (file_is):
    with open(f"{file_is}", 'r') as new_file:
        spisok_elementov = new_file.read().split()
    new_file.close()
    return spisok_elementov

# - список коэффициентов.
def spisok_koefficientov (file_is):
    spisok_elem = file_read(file_is)
    spisok_koeff = [f'{spisok_elem[0]}']
    for i in range(1, len(spisok_elem)):
        if spisok_elem[i] == '+' or spisok_elem[i] == '-':
            continue            
        elif spisok_elem[i - 1] == '-':
            spisok_koeff.append(f'-{spisok_elem[i]}')
        else:
            spisok_koeff.append(spisok_elem[i])
    return spisok_koeff