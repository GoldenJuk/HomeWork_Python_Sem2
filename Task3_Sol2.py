# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

from random import randint as RN 

def GetRAndomList(n):
    my_list = []
    for i in range(n):
        my_list.append(RN(0,100))
    return my_list       

# Алгоритм перемешивания внутри оригинального списка
# Для лучшего перемешивания колическтво иттераций в 2 раза больлше длины первоначального списка 

def GetShuffleList(my_list):
    for i in range(len(my_list)*2):
        index1 = RN(0,len(my_list)-1)
        index2 = RN(0,len(my_list)-1)
        my_list[index1], my_list[index2] = my_list[index2],my_list[index1]
    return my_list      

original_list = GetRAndomList(10)
print(original_list)
shuffle_list = GetShuffleList(original_list)
print(shuffle_list)