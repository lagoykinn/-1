a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
if D<0:
    print("корней нет")
else:
    x1=(-b+D**0,5)/2*a
    x2=(-b-D**0.5)/2*a
    if x1==x2:
        print("корней уравнения",x1)
    else:
        print("корней уравнения",x1,x2)

