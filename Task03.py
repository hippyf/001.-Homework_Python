#Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = int(input(('Введите значение X ≠ 0 ')))
y = int(input(('Введите значение Y ≠ 0 ')))
if x != 0 and y != 0:
    if x > 0 and y > 0: print('I четверть')
    elif x < 0 and y > 0: print('II четверть')
    elif x < 0 and y < 0: print('III четверть')
    elif x > 0 and y < 0: print('IV четверть')
else: print('Введены неверные значения')