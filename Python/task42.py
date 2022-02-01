# Найти сумму чисел списка стоящих на нечетной позиции
n = int(input('n'))
sum = 0
for i in range(0,n):
 if i % 2 != 0:
  sum += i
print(sum)
