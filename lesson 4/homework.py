# holder = {} 
animals = ["dog", "cat","bird", "cat", "dog", "cat"]
# for i in range(len(animals)):
#     cat = animals[i]

#     if cat in holder:
#         holder[cat]+=1

#     else:
#         holder[cat]=1

#     print(holder)

# print(holder["cat"])
# cats = 0
# for i in range(len(animals)):

#     if animals[i] == "cat":
#         # cats+=1
#         animals[i] = "boy"
# print(animals)

word = "apple"

dash = ["_","_","_","_","_"]

print(dash)

print(" ".join(dash))

for i in range(5):
    guess = input("guess a letter")

    for i in range(len(word)):
        if word[i] == guess:
            dash[i] = guess
    print(" ".join(dash))



