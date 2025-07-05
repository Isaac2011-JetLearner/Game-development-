food = ["candy","rice","egg","bread","egg","rice","candy","bread"]
holder = {}

for i in range(len(food)):
    ask = input("enter a food: ")

    if ask in holder:
        holder[ask]+=1

    else:
        holder[ask]=1

print(holder[ask])
