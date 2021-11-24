def Table(a):
    print("TABLE OF ",a,end="\n")
    for i in range(1,11):
        print(i," X ", a , " = ", i*a)


n = 10
for i in range(n+1):
    Table(i)