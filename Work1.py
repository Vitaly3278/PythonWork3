# Вычислить число Пи c заданной точностью d

import math

lis = str(math.pi)

d = int(input('Введите точность для числа Pi: '))

l = lis[0:d+2:1]

print(f'Число PI с точностью {d} равно {l}')