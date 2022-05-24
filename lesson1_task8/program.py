# Напишите программу, которая проверит истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
counter = 0

def is_true (x,y):
    if (not(x or y)) == (not(x) and not(y)):
        return True
    else:
        return False

x = True
y = True
print(f'При Х = 1 и Y = 1 функция возвращает значение {is_true(x,y)}.')
if is_true(x,y): counter += 1

x = True
y = False
print(f'При Х = 1 и Y = 0 функция возвращает значение {is_true(x,y)}.')
if is_true(x,y): counter += 1

x = False
y = True
print(f'При Х = 0 и Y = 1 функция возвращает значение {is_true(x,y)}.')
if is_true(x,y): counter += 1

x = False
y = False
print(f'При Х = 0 и Y = 0 функция возвращает значение {is_true(x,y)}.')
if is_true(x,y): counter += 1

print()

if counter == 4: print('Функция истинна!')
else: print('Функция ложна!')