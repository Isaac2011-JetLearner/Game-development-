food = ["candy","rice","egg","bread","egg","rice","candy","bread"]
holder = {}

ask = input("enter a food: ")
for i in range(len(food)):
    global ask

    if ask in holder:
        holder[ask]+=1

    else:
        holder[ask]=1

print(holder[ask])
