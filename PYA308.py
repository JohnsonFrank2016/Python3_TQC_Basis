dac = eval(input())+1

for i in range(1,dac):
    num = eval(input())
    tmp = num
    out = 0
    while tmp!=0:
        out += tmp%10
        tmp//=10
    print("Sum of all digits of",num,"is",out)