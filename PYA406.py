cm = eval(input())
while cm!=-9999:
    kg = eval(input())
    BMI = kg/((cm/100)*(cm/100))
    print("BMI:%.2f"%BMI)
    if BMI<18.5:
        print("State:under weight")
    elif 18.5<=BMI and BMI<25:
        print("State:normal")
    elif 25.0<=BMI and BMI<30:
        print("State:over weight")
    else:
        print("State:fat")
    cm = eval(input())