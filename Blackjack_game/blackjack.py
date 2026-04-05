import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
total_score_user=0
total_score_computer=0
user_choice=[]
computer_choice=[]

def pick_card_user():
    global total_score_user
    a=random.choice(cards)
    user_choice.append(a)
    total_score_user+=a


def pick_card_computer():
    global total_score_computer
    b=random.choice(cards)
    computer_choice.append(b)
    total_score_computer+=b


game=True
want_to_play_again=True



def blackjack_game():
    global total_score_user
    global total_score_computer
    global user_choice
    global computer_choice
    global game
    while game:
        if len(user_choice)==0:
            pick_card_user()
            pick_card_user()
        if len(computer_choice)==0:
            pick_card_computer()
    
        print(f"Your cards are : {user_choice} and score is : {total_score_user} \n ")
        print(f"Computer cards are : {computer_choice} and score is : {total_score_computer} \n")
    
        while total_score_user<21 and total_score_computer<21:
            another_card=input("Do you want to play another card, type y or n : ")
            if another_card.lower() == "y":
                pick_card_user()
    
            if another_card.lower() == "n":
                break
    
    
            print(f"Your cards are : {user_choice} and score is : {total_score_user} \n")
            print(f"Computer cards are : {computer_choice} and computer score is : {total_score_computer} \n")
    
        while total_score_computer < 17:
                pick_card_computer()
    
        if total_score_computer>21:
            print(f"Your cards are : {user_choice} and score is : {total_score_user} \n ")
            print(f"Computer cards are : {computer_choice} and computer score is : {total_score_computer} \n")
            print("You Win!")
            game=False
        elif total_score_user>21:
            print(f"Your cards are : {user_choice} and score is : {total_score_user} \n ")
            print(f"Computer cards are : {computer_choice} and computer score is : {total_score_computer} \n")
            print("Computer Win!")
            game=False
    
        elif  total_score_user>total_score_computer and total_score_user<=21:
            print(f"Your cards are : {user_choice} and score is : {total_score_user} \n ")
            print(f"Computer cards are : {computer_choice} and computer score is : {total_score_computer} \n")
            print("You Win!")
            game=False
    
        elif total_score_computer>total_score_user and total_score_computer<=21:
            print(f"Your cards are : {user_choice} and score is : {total_score_user} \n ")
            print(f"Computer cards are : {computer_choice} and computer score is : {total_score_computer} \n")
            print("Computer Win!")
            game=False
        else:
            print(f"Your cards are : {user_choice} and score is : {total_score_user} \n ")
            print(f"Computer cards are : {computer_choice} and computer score is : {total_score_computer} \n")
            print("Draw")
            game = False


print(art.logo+"\n")
choose_play=input("Do you want to play blackgame, type y or n:  ")
while want_to_play_again:
    if choose_play.lower() == "y":
        blackjack_game()
    
    play_again=input("Do you want to play this game again, type y or n:  ")
    if play_again.lower() == "y":
        blackjack_game()
    else:
        want_to_play_again=False
        print("\nThanks for playing! See you Later!\n")
        
    

