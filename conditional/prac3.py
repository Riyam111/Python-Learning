 # grade calculator
# assign a letter grade based ona student score :A(90-100),B(80-89),C(70-79),D(60-69),F(below 60)
marks=int(input("enter the total marks obtained by a student: "))
if marks>100:
    print("verify your marks as it can not be grater than 100")
    exit()
if marks>=90:
    print("student got A")
elif marks>=80:
    print("student got B")
elif marks>=70:
    print("student got C")
elif marks>=60:
    print("student got D")
else:
    print("student got E")