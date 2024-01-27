# import modul1
# print(modul1.max1(44,109))

'''
Последовательность фибоначи
'''

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1)+fib(n-2)
list_1 = []
for i in range(1,10):
    list_1.append(fib(i))
print(list_1)