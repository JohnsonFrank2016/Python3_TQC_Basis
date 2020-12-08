def compute(x,y):
    for i in range(x,0,-1):
        if x%i==0 and y%i==0:
            return i
        
x,y = eval(input())
ans = compute(x, y)
print(ans)