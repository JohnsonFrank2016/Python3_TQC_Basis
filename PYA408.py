array = [0]*10
for i in range(0,10):
    array[i] = eval(input())
    
E = 0;
O = 0;
for i in array:
    if i%2==0:E+=1
    if i%2==1:O+=1
    
print("Even numbers:",E)
print("Odd numbers:",O)