a = eval(input())
b = eval(input())+1
sum = 0;

for i in range(a,b):
    if i%2==0:
        sum+=i
        
print(sum)