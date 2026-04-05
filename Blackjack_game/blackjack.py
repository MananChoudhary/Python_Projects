import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def pick_card():
    return random.choice(cards)
def calculate_score(hand):
    if sum(hand)==21 and len(hand)==2:
        return 0
    if 11 in hand and sum(hand)>21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def blackjack_game():
    user_choice = []
    computer_choice = []
    game=True

    for i in range(2):
        user_choice.append(pick_card())
        computer_choice.append(pick_card())
    while game:
        total_score_user = calculate_score(user_choice)
        total_score_computer = calculate_score(computer_choice)
        print(f"Your cards are : {user_choice} and score is : {total_score_user} \n ")
        print(f"Computer cards are : {computer_choice[0]} \n")

        if total_score_user==0 or total_score_computer==0 or total_score_user>21:
            game=False
        else :
            user_pick_another_card=input("Do you want to play another card, type y or n : ")
            if user_pick_another_card.lower() == "y":
                user_choice.append(pick_card())
            else:
                game=False
    while total_score_computer!=0 and  total_score_computer<17:
        computer_choice.append(pick_card())
        total_score_computer = calculate_score(computer_choice)

    print(f"Your cards are : {user_choice} and score is : {total_score_user} \n ")
    print(f"Computer cards are : {computer_choice} and score is : {total_score_computer} \n")


        # while total_score_user<21 and total_score_computer<21:
        #     another_card=input("Do you want to play another card, type y or n : ")
        #     if another_card.lower() == "y":
        #         pick_card_user()
        #
        #     if another_card.lower() == "n":
        #         break
        #
        #
        #     print(f"Your cards are : {user_choice} and score is : {total_score_user} \n")
        #     print(f"Computer cards are : {computer_choice} and computer score is : {total_score_computer} \n")
        #
        # while total_score_computer < 17:
        #         pick_card_computer()

    if total_score_user > 21:
        print("You went over. You lose!")
    elif total_score_computer > 21:
        print("Opponent went over. You win!")
    elif total_score_user == total_score_computer:
        print("Draw!")
    elif total_score_computer == 0:
        print("Lose, opponent has Blackjack!")
    elif total_score_user == 0:
        print("Win with a Blackjack!")
    elif total_score_user > total_score_computer:
        print("You win!")
    else:
        print("You lose!")


print(art.logo+"\n")
another_chance=True
while another_chance:
    a=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if a.lower()=="y":
        blackjack_game()
    else:
        print("Thanks for playing with us! See you :) ")
        another_chance=False



