# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input("Введите число: "))
i = 2
lst = []
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множителиgit commit -m ': {lst}")