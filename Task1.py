# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def GetSum(num):
    sum = 0
    for char in num:
        if char.isdigit():
            sum += int(char)
    return sum    
n = input('Введите число: ')
res = GetSum(n)
print()
print(f'Сумма цифр введенного числа = {res}')
print()