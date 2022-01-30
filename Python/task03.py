#По заданному номеру дня недели вывести его название
day = int(input("введите номер дня недели "))
if day==1:
    print("понедельник")
elif day==2:
 print("вторник")
elif day==3:
 print("среда")
elif day==4:
 print("четверг")
elif day==5:
 print("пятница")
elif day==6:
 print("суббота")
elif day==7:
 print("воскресенье")
else: print("введите числа менее 8")