# Задать номер четверти, показать диапазоны для возможных координат
quarter = int(input("enter sector"))
if quarter ==1:
    print ("x>0,y>0 ")
if quarter ==2:
    print ("x<0,y>0 ")
if quarter ==3: 
    print ("x<0,y<0 ")
if quarter ==4:
    print ("x>0,y<0 ")
else:
    print ("please enter number < 5")