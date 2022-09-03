#Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

from math import sqrt
from turtle import distance


x1 = float(input(('Введите координаты точки A ')))
y1 = float(input())
x2 = float(input(('Введите координаты точки B ')))
y2 = float(input())
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(round(distance, 3))
