#Показать вторую цифру трёхзначного числа

a = int(input("введите трехзначное число "))
if 99<a<1000:
    print ((a // 10)%10)
else:
    print ("введеное число не трехзначное")