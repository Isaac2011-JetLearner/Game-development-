nums = [2,4,2,4,2,4,3,3,3,1,4,1]

mp = {}

for i in range(len(nums)):
    numbers = nums[i]

    if numbers in mp:
        mp[numbers]+=1
    
    else:
        mp[numbers] = 1

print(mp)