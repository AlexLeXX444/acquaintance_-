# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# https://en.wikipedia.org/wiki/Run-length_encoding
# входные и выходные данные хранятся в отдельных текстовых файлах.

import rle_zip
import rle_unzip

def read_file (file_name):
    with open(file_name, 'r') as new_file:
        data = new_file.read()
    new_file.close()
    return data

def write_file (file_name, data):
    with open(file_name, 'w') as new_file:
        new_file.write(data)
    new_file.close()

print('Что требутеся сделать?')
print('Выберете нужный пункт(введите 1 или 2):\n 1. Сжать данные;\n 2. Разжать данные.')
user_answer = input()

if user_answer == '1':
    print(f'Входные данные:\n{read_file("data.txt")}')
    print(f'Данные записаны в файл zip_data.txt.')
    write_file("zip_data.txt", rle_zip.zip_data(read_file("data.txt")))
elif user_answer == '2':
    print(f'Входные данные:\n{read_file("zip_data.txt")}')
    print(f'Данные записаны в файл un_zip_data.txt.')
    write_file("un_zip_data.txt", rle_unzip.un_zip_data(read_file("zip_data.txt")))
else:
    print('Неверный ввод!')


""" data_zipped = rle_zip.zip_data(read_file("data.txt"))
write_file("zip_data.txt", data_zipped)
print(f'После сжатия:\n{data_zipped}') """



