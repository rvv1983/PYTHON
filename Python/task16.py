# Дано число обозначающее день недели. Выяснить является номер дня недели выходным
a = int(input("input number "))
my_dict = {1:"monday", 2:"tuesday", 3:"wednesday",4:"thursday",5:"friday",6:"saturday",7:"sunday"}
print(my_dict[a]) 
if a < 6:
 print("not weekend")
else:
    print("weekend")
    
