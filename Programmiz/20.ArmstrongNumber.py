n = 123
sum = 0
while n>0:
    d = n//10
    sum += d
    n += n//10
print(sum)