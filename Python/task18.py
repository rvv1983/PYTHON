# Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
x=[0,1]
y=[1,0]
def check(x,y):
    for x in range(2):
        res=not(x or y) == (not x and not y)
        print(x,y,res)
check(x,y) 