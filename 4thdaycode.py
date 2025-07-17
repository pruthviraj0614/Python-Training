a1 = [1,2,3,0,4,0,7,0]
num1=[]
num2=[]
for i in a1:
   if i>0:
      num1.append(i)
   else:
      num2.append(i)
result=[] 
result.extend(num1)
result.extend(num2)
print(result)   

