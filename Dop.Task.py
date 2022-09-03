# Требуется найти N-е число Фибоначчи. 1 1 2 3 5 8 17

N = int(input(('Введите число от 0 до 30 ')))
a1 = 1
a2 = 1
if N == 0: print(0)
elif N == 1: print(a1)
elif N == 2: print(a2)
elif N > 2:
    for i in range (N-2):
        a3 = a1 + a2
        a1 = a2
        a2 = a3
    print(a3)
else: print('Введено неправильное число ')
