def compute(a,b,c):
    d = b**2-4*a*c
    if d<0:
        return None
    elif d==0:
        return -b/(2*a)
    else:
        e1=(-b+d**0.5)/(2*a)
        e2=(-b-d**0.5)/(2*a)
        return str(e1)+","+str(e2)
    
a = eval(input())
b = eval(input())
c = eval(input())
e = compute(a,b,c)
if e==None:
    print("Your equation has no root.")
else:
    print(e)