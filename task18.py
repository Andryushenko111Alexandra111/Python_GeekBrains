'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к 
заданному числу X. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X

Пример:
5 
1 2 3 4 5 
6 -> 5
'''

# from random import randint
# input_set = [randint(1, 99) for i in range(int(input('Введите размер массива: ')))]
# print(input_set)
# num = int(input('Введите искомое число: '))
# input_set = set(input_set)
# dif = 0
# if num > max(input_set):
#     print(max(input_set))
# elif num < min(input_set):
#     print(min(input_set))
# else:
#     while True:
#         if num - dif in input_set and num + dif in input_set and num - dif != num + dif:
#             print(num - dif, num + dif)
#             break
#         elif num - dif in input_set:
#             print(num - dif)
#             break
#         elif num + dif in input_set:
#             print(num + dif)
#             break
#         else:
#             dif += 1


list_1 = [1, 10, 3, 4, 5, 8, 11]
k = 2
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)