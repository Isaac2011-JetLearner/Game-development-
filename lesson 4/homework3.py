nums = [1,2,4,5,6,4,6,7,8,9,9,1,3,4,4,7,7,7,7]

number = int(input("enter a number"))

for i in range(len(nums)):    
    if number == nums[i]:
        print("number is in the list" + str(i))

for i in range(1):
    if number in nums:
        print(nums.index(number))