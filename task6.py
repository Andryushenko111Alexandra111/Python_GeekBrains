'''Задача 6
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
'''
n = 385916

# Введите ваше решение ниже
a = str(n)
l = int(a[0]) + int(a[1]) + int(a[2])
r = int(a[3]) + int(a[4]) + int(a[5])
if l == r:
    print('yes')
else:
    print('no')