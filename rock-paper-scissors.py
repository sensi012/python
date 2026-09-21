import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"player:{player}")
    print(f"computer: {computer}")

    if player == computer:
        print("it's a tie!")
    elif player == "rock" and computer =="scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You lose!")

    # play_again = input("Play again? (y/n): ").lower()
    # if play_again != "y":
    #     running = False
    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
