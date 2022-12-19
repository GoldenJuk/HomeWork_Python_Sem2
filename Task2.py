# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

def GetList(num):
    my_list = []
    for i in range(1,num + 1):
        my_list.append(round(((1+1/i)**i),2)) 
    return my_list

def GetSumOfList(my_list):
    sum = 0
    for i in range(len(my_list)):
        sum += my_list[i]
    return round(sum,2)    

n = int(input('Введите число: '))
print()
listOfN = GetList(n)
print(f'Список из {n} чисел последовательности (1 + 1/n)**n: {listOfN}')
sum = GetSumOfList(listOfN)
print()
print(f'Сумма элементов списка {listOfN} = {sum}')
print()