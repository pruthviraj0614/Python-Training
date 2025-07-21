'''Given an integer array nums, return true if any value appears at
 least twice in the array, and return false if every element is
 distinct
 '''
arr=[1,2,3,4,2,5]
fre={}
for i in arr:
    if i in fre:
        fre[i]+=1
       
    else:
        fre[i]=1  
          
print(fre)        