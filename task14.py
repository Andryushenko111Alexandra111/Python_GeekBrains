'''
Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
Пример:
10 -> 1 2 4 8
'''
n = 19

# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

#или

k = 0
res = 1
while res <= n:
    print(res)
    k += 1
    res = 2 ** k