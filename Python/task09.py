#Показать последнюю цифру трёхзначного числа
a=int(input("enter three-digit number "))
if 99 < a < 1000:
  print (a%10)
else:
    print ("not three-digit number")