num = [2,3,4,5,6,7,8,9]
num_2 = [3,6,3,2,4,11,9,2]
empty = []

for i in range(len(num)+len(num_2)):
    add = num[i]+num_2[i]
    empty.append(add)
    print(empty[i])