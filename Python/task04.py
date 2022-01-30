#Найти максимальное из трех чисел
a=int(input("введите число 1 "))
b=int(input("введите число 2 "))
c=int(input("введите число 3 "))
if a<b>c:
 print("number",b,"is max")
elif b<c>a:
 print("number",c,"is max")
else: 
 print("number",a,"is max")