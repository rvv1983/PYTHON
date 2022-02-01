# Написать программу вычисления произведения чисел от 1 до N
num = int(input("enter num: "))
mult = 1
while (num != 0):
    mult = mult * (num % 10)
    num = num // 10
print("result is : ", mult)      