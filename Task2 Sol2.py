# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

def GetListAndSum(num):
    my_list = []
    sum = 0
    for i in range(1,num + 1):
        my_list.append(round(((1+1/i)**i),2))
        sum += my_list[i-1]
    return my_list,sum

n = int(input('Введите число: '))
print()
listOfN = GetListAndSum(n)
print(f'Список из {n} чисел последовательности (1 + 1/n)**n: {listOfN[0]}')
print()
print(f'Сумма элементов списка {listOfN[0]} = {listOfN[1]}')
print()