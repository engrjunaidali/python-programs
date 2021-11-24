def evenOdd(n):
    # status = 'even'
    if n>=0:
        if n==0 or n%2==0:
            status = 'even'
        else:
            status = 'odd'
        return status
    else:
        return "Please enter postive number"

n = -1
print(evenOdd(n))
