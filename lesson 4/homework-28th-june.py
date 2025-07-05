# for i in range(1,86):
    # print(i)

# for i in range(96,5,-1):
#     print(i)


# num = 0
# while num<200:
#     num+=2
#     print(num)


# for i in range(49,2,-2):
#     print(i)



# colours = ["blue","green","red","yellow","orange","cyan","pink"]

# for i in range(len(colours)):
#     print(colours[i])

numbers = [1,2,4,5,6,23,42,21]

# for i in range(1,len(numbers)):
#     nums_2 = numbers[i] + numbers[i-1]
#     print(nums_2)

nums = 1
    
while nums < len(numbers):
    answer=  numbers[nums] + numbers[nums-1]
    print(answer)
    nums+=1
