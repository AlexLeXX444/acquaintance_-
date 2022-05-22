# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
first_num = int(input("Введите первое число:"))
second_num = int(input("Введите второе число:"))
if second_num == first_num & first_num == 0:
    print(f"Оба числа равны нулю!")
elif first_num * first_num == second_num:
    print(f"Второе число {second_num} - это квадрат первого числа {first_num}!")
elif second_num * second_num == first_num:
    print(f"Первое число {first_num} - это квадрат второго числа {second_num}!")    
else:
    print(f"Числа не являются квадратами друг друга!")