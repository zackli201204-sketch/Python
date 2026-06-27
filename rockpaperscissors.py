import random

while True:
    user_action=input("Enter a choice [Rock, paper, scissors]: ")
    possible_actions=["rock, paper, scissors"]
    computer_actions=random.choice(possible_actions)
    print(f"\nYou choose {user_action}, computer chose {computer_actions}.\n")

    if user_action==computer_actions:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action=="rock":
        if computer_actions=="scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action=="paper":
        if computer_actions=="rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action=="scissors":
        if computer_actions=="paper":
            print("Scissors cuts paper! You win!")
        else:
            print("rock beats scissors! You lose.")

    play_again=input("play again? (y/n): ")
    if play_again !="y":
        break