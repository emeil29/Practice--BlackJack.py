import random

user_cards = []
computer_cards = []
game_over = False

""" radom cards"""
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

""" number cards to be drawns"""
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

"""" take a list of card and return the score calculated from the cards  """
def calculate_score(cards):
    if sum(cards) == 21 and len(cards)== 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

""" compare the cards """
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It is a draw"
    elif computer_score == 0:
        return "Lose, Computer has a BlackJack😣"
    elif user_score == 0:
        return "Winner, You have a BlackJack😣"
    elif user_score > 21:
        return " You went over, You lose"
    elif computer_score > 21:
        return " Computer went over, You win😜😜"
    elif user_score > computer_score:
        return " You win😊"
    else:
        return" You lose"

""" while loop to add more cards if needed for the user"""
while game_over != True:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Player have {user_cards} total {user_score}")
    print(f"Computer first card is {computer_cards[0]}")
    if user_score == 0 or computer_score ==0 or user_score >21:
        game_over = True
    else:
        draw_new_card = input("Would like to draw a new card 'y' or 'n' \n")
        if draw_new_card == 'y':
            user_cards.append(deal_card())
        else:
            game_over = True

""" while loop for the computer """
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f" computer has {computer_cards}")
print(compare(user_score, computer_score))
