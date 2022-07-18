import random

print("Let's play a better of 3!")

games = 0
user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while games < 3:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break

    elif user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == 'rock' and computer_pick == 'scissors':
        user_wins += 1
        games += 1
        print("You won!")
    elif user_input == 'paper' and computer_pick == 'rock':
        games += 1
        user_wins += 1
        print("You won!")
    elif user_input == 'scissors' and computer_pick == 'paper':
        games += 1
        user_wins += 1
        print("You won!")
    elif user_input == computer_pick:
        print("Tie!")
    else:
        games += 1
        print("You lost!")
        computer_wins += 1

    if computer_wins == 2 and user_wins == 0:
        break
    elif user_wins == 2 and computer_wins == 0:
        break

if computer_wins > user_wins:
    print(f"Computer won by {computer_wins} x {user_wins}.")
else:
    print(f"You won by {user_wins} x {computer_wins}.")