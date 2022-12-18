# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def GetSum(num):
    sum = 0     
    my_list = num.split('.')
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            sum = sum + int(my_list[i][j])
    return sum    
n = input('Введите число: ')
res = GetSum(n)
print()
print(f'Сумма цифр введенного числа = {res}')
print()
