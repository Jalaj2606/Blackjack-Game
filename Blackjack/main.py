import random
import art
from replit import clear
choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def add_card():
  x = random.choice(cards)
  return x
def calculate_score(cards_list):
  sum = 0
  for i in cards_list:
    sum += i
  return sum

while choice == "y":
  clear()
  print(art.logo)
  user_score = 0
  computer_score = 0
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(add_card())
    computer_cards.append(add_card())
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  if computer_score == 21:
    print("Computer got a Blackjack, You lose!..😱")
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
  elif user_score == 21 and computer_score == 21:  
    print("Its a draw!..")
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
  else:  
    print(f"Your cards: {user_cards},current score: {user_score} ")
    print(f"Computer's first card: {computer_cards[0]}")
    card_choice = input("Type 'y' to get another card, type 'n' to pass:")
    while card_choice == "y":
      user_cards.append(add_card())
      user_score = calculate_score(user_cards)
      print(f"Your cards: {user_cards},current score: {user_score} ")
      print(f"Computer's first card: {computer_cards[0]}")
      if user_score > 21 and 11 in user_cards:
        user_score -= 10
        position = user_cards.index(11)
        user_cards[position] = 1
        print(f"Your cards: {user_cards},current score: {user_score} ")
        print(f"Computer's first card: {computer_cards[0]}")
        card_choice = input("Type 'y' to get another card, type 'n' to pass:")
      elif user_score >= 21:
        card_choice = "n"
      else:
        card_choice = input("Type 'y' to get another card, type 'n' to pass:")
    while computer_score < 16:
      computer_cards.append(add_card())
      computer_score = calculate_score(computer_cards)
      if computer_score > 21 and 11 in computer_cards:
        computer_score -= 10
        position = computer_cards.index(11)
        computer_cards[position] = 1
  if user_score == 21:
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("Blackjack, You win..")
  elif user_score > 21:
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("You went over. You lose 😤")
  elif computer_score > 21:
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("Computer went over. You Win...")
  elif computer_score == 21:
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("You Lose, Computer has a Blackjack..")
  elif user_score==computer_score:
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("Its a draw..")
  elif user_score>computer_score:
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("You win..")
  else:
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("You Lose..")    
  choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    

      


   

