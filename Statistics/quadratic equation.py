x = list(range(1,7))
y = [1.6,4.5,13.8,40.2,125,363]
print(x)
ans = []


for i in x:
    y_dash = 118.11+(-121.97*i) + (26.383*(i*i))
    ans.append(y_dash)

print("X\tY")
for i in range(len(x)):
    print(x[i],"\t",ans[i])

print(sum)
