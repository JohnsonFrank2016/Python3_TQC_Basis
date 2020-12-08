def compute(a,b):
    #return a**b
    num = a
    for i in range(1,b):
        num*=a
    return num

a = eval(input())
b = eval(input())
print(compute(a,b))