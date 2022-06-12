print("Welcome to the Rock-Paper-Scissors game")
print("How to play:")
print("Rock(r) beats Scissors(s)")
print("Scissors(s) beats Paper(p)")
print("Paper(p) beats Rock(r)")

import random

while True:
    user_entry = input("Enter a choice (r, p, s): ")
    user_action = user_entry.lower()
    possible_actions = ["r", "p", "s"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou ({user_action}) : computer ({computer_action}).\n")

 
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        print("Another round...go!")
        continue
    elif user_action == "r":
        if computer_action == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "p":
        if computer_action == "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "s":
        if computer_action == "p":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    else:
        print("Invalid selection")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
