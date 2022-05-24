# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from cmath import sqrt

cords_dot_a = list(map(int, input('Введите координаты точки А через через пробел:  ').split(' ')))
cords_dot_b = list(map(int, input('Введите координаты точки B через через пробел:  ').split(' ')))

print(f'Расстояние между точками равно {sqrt(pow((cords_dot_b[0] - cords_dot_a[0]), 2) + pow((cords_dot_b[1] - cords_dot_a[1]), 2))}.')