x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

dist = ((x2-x1)**2+(y2-y1)**2)**(0.5)

print("(", x1,",",y1,")")
print("(", x2,",",y2,")")
print("Distance = %.4f"%dist)