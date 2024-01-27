num = int(input("Введите число: "))
total = num
again = "y"
while again == "y":
     num1 = int(input("Введите число: "))
     total = total + num1
     again = input("Хотите прибавить это число? (y/n)")
print("Сумма равна", total)