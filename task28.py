'''
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
 неотрицательных чисел. Из всех арифметических операций допускаются 
 только +1 и -1. Также нельзя использовать циклы.

 Пример:
sum(2, 2)
# 4
'''
a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))
def r_sum(a, b):
    if a == 0:
        return b
    else:
        return r_sum(a - 1, b + 1)
print(r_sum(a, b))

ягоды