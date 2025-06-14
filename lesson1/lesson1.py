countries = {}

while True:
    print("what do you want to do?")
    print("add,remove or view?")

    ask = input("enter you choice")


    if ask == "add":
        country = input("enter a country name")
        capital = input("enter its capital")
        countries[country] = capital
        

    elif ask == "view":
        print(countries)
    

    elif ask == "remove":
        remove = input("what country do you want to remove? ")
        del countries[remove]