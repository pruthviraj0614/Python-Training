'''def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None  

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result) 
'''
nums=[2,7,11,15]
target=26
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print([i,j])
        else:
            print('not found')
            break
   