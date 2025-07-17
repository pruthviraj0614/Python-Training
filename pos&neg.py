arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
pos = []
neg = []
for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

result = [pos,neg]
print(result)