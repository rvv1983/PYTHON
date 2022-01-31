# Найти кубы чисел от 1 до N
N = int(input("enter number  "))
i = 1
while i ** 3 <= N:
    print(i ** 3)
    i += 1