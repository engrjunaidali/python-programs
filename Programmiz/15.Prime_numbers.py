
def Prime(n):
    if n > 0:
        for i in range(2,n):
            if n%i == 0:
                return False
    return True

lower = 1
upper = 100

for i in range(lower,upper+1):
    if (Prime(i)):
        print(i,end = " ")
