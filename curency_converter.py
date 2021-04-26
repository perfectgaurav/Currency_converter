with open("t.txt") as f:
    lines = f.readlines()

gk = {}

for items in lines:
    parsed = items.split("\t")
    gk[parsed[0]] = parsed[1]


while True:
    
    amount=int(input("Enter the amount: "))

    [print(i) for i in gk.keys()]

    currency= input("Enter the country name  in which you want convert your Money: ")
    
    if currency in gk.keys():
        print(f"your converted amount is {amount* float(gk[currency])}")
        
    else:
        print("Please enter a valid country")
        


    
