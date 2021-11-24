import random

def findDuplicates(A):
    B =[]
    duplicates = []

    for i in A:
        if i in B:
            duplicates.append(i)
        else:
            B.append(i)
    return duplicates

A = [1,2,3,5,4,3,6,5,4]

print(findDuplicates(A))