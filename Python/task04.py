#Найти максимальное из трех чисел
a=int(input("введите число 1 "))
b=int(input("введите число 2 "))
c=int(input("введите число 3 "))
if a<b>c:
 print("число",b,"максимальное")
elif b<c>a:
 print("число",c,"максимальное")
else: 
 print("число",a,"максимальное")