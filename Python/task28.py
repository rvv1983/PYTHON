# Подсчитать сумму цифр в числе
num = int(input("enter number: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("sum numbers = : ", sum)         