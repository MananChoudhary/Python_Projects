dict_collection={}
def new_user():
    user_name=input("Enter your name \n")
    
    while True:
        try:
            bid_amount=int(input("Enter your bid amount\n"))
            break
        except:
            print("Please enter valid value")
    dict_collection[user_name]=bid_amount
running =True
while running:
    new_user()
    while True:
            more_players=input("Do you have more players? Type yes or no\n").lower()
            if more_players=="yes":
                print("\n"*100)
                break
                
            elif more_players=='no':
                max_key=max(dict_collection,key=dict_collection.get)
                print(f"The winner is {max_key} and amount : {dict_collection[max_key]}")
                running=False
                break
            else:
                 print("Invalid input")
            