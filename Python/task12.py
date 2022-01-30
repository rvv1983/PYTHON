#Удалить вторую цифру трёхзначного числа
a = int(input("enter number 3 symbols "))
if 99<a<1000:
   x=a//100
   y=a%10
   print(x*10+y)
else:
  print ("wrong enter, try again")