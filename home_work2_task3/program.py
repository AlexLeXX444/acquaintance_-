# Реализуйте случайное перемешивания списка.

import random

input_list = list(input('Введите список через запятую: ').split(','))
random.shuffle(input_list)
print(f'Перемешали список: {input_list}')