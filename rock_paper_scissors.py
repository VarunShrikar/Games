import random

PlayerA = input("\nEnter your choice: ")
possibilities = ["rock","paper","scissors"]
PlayerB = random.choice(possibilities)

if PlayerA == PlayerB:
    print("\nIt's a tie. Play again.\n")

elif PlayerA == "rock":
    if PlayerB == "paper":
        print(f"\n{PlayerB} beats {PlayerA}. PlayerB wins!!\n")
    elif PlayerB == "scissors":
        print(f"\n{PlayerA} beats {PlayerB}. PlayerA wins!!\n")

elif PlayerA == "paper":
    if PlayerB == "rock":
        print(f"\n{PlayerA} beats {PlayerB}. PlayerA wins!!\n")
    elif PlayerB == "scissors":
        print(f"\n{PlayerB} beats {PlayerA}. PlayerB wins!!\n")

elif PlayerA == "scissors":
    if PlayerB == "rock":
        print(f"\n{PlayerB} beats {PlayerA}. PlayerB wins!!\n")
    elif PlayerB == "paper":
        print(f"\n{PlayerA} beats {PlayerB}. PlayerA wins!!\n")