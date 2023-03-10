# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

from random import randint as RN 

def GetRAndomList(n):
    my_list = []
    for i in range(n):
        my_list.append(RN(0,100))
    return my_list
             
# Алгоритм перемешивания с использованием дополнительного списка

def GetShuffleList(my_list):
    shuf_list = []
    while len(my_list) > 0:
        index = RN(0,len(my_list)-1)
        shuf_list.append(my_list[index])
        my_list.pop(index)
    return shuf_list      

original_list = GetRAndomList(10)
print(original_list)
shuffle_list = GetShuffleList(original_list)
print(shuffle_list)
