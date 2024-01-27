# arr = [2, 4, 6, 8, 10]
# n = len(arr)
# max_sum = 0

# for i in range(n):
#     sum = arr[i]
#     left = (i-1) % n # 0-1%5 = -1, 1-1%5 = 0, 2-1%5 = 1, 3-1%5 = 2, 4-1%5 = 3, 5-1%5 = 4. При n==5
#     right = (i+1) % n
#     sum += arr[left] + arr[right] 
#     max_sum = max(max_sum, sum)

# print(max_sum)
berries = []
n = int(input("N> ")) # berries = list(map(int, input(f"Введите ягоды для {n} кустов > ").split()))
for i in range(n):
    berries.append(int(input(f"Куст {i+1}: ")))

max_sum = 0

for i in range(n):
    sum = berries[i]
    left = (i-1) % n # 0-1%5 = -1, 1-1%5 = 0, 2-1%5 = 1, 3-1%5 = 2, 4-1%5 = 3, 5-1%5 = 4. При n==5
    right = (i+1) % n
    sum += berries[left] + berries[right] 
    max_sum = max(max_sum, sum)

print(max_sum)
