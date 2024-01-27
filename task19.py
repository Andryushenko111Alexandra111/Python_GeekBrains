'''
Дана последовательность из N целых чисел и число К.
Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на К элемнтов вправо, 
К - положительное число.
Input: [1,2,3,4,5]k=3
Output:[3,4,5,1,2] 
'''

# list1 = [5,4,6,7,10]
# k = int(input())
# k = k % len(list1)

# list1_res = []

# for i in range(k):
#     list1_res.append(list1[len(list1) - 1 ])
#     print (list1_res)

# for i in range(len(list1) - k):
#     list1_res.append(list1[i])
#     print(list1_res)

a = [1, 2, 3, 4, 5]
print(a)
k = 2
for i in range(k):
    a.append(a.pop(0))
print(a)