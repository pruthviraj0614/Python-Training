arr=list(map(int,input().split()))
n=int(input())
c=0
for i in arr:
    if i==0:
        continue
    if i<=3:
       c+=1
    else:
        if 1%3==0:
            c +=(i//3)
        else:
            c+=(i//3)+1
print(c)       