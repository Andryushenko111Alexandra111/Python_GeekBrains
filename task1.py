'''
 За день машина проезжает n километров.
Ссколько нужно дней, чтобы проехать маршруть длиной m
километров? При решении этой задачи нельзя пользоваться 
условной инструкцией if и циклами.

'''

print ("За день машина проезжает: ")
n = int(input())
print ("Расстояние, которое необходимо проехать машине: ")
m = int(input())
a = (n + m - 1)//n
print(a,"дня необходимо")