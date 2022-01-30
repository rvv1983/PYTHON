# Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
print('enter coordinates')
x = int(input())
y = int(input())
if x>0:
 if y>0:
  print('sector 1 ')
 else: 
  print('sector 4 ')
else:
 if y>0:
  print('sector 2 ')
 else:
  print('sector 3 ')
    
