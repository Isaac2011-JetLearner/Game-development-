sample = {}
string = "this is a beautiful day"

for i in range(len(string)):
    leter = string[i]

    if leter == " ":
        continue
    
    if leter in sample:
        sample[leter]+=1

    else:
        sample[leter]=1

print(sample)




    



