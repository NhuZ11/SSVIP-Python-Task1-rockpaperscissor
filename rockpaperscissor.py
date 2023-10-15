import random
# assigning number for respective choice

rock_choice = 0
scissor_choice = 1
paper_choice = 2

possible_action = ["rock", "scissors", "paper"]  # declaring the choices of action
computer_action = random.choice(possible_action)  # selecting random action


while True:
    user_input = input("Enter your choice \n 0 for rock\n 1 for scissor\n 2 for paper")
    user_choice = int(user_input)
    if user_choice == rock_choice:
        user_chose = "rock"

    elif user_choice == scissor_choice:
        user_chose = "scissors"

    elif user_choice == paper_choice:
        user_chose = "paper"

    else:
        user_chose = "wrong value"
        print("Enter the right number!!")
        continue  # This will restart the loop if the user enters an incorrect value

    print(f"\nYou chose {user_chose}, computer chose {computer_action}.\n")

    if user_chose == computer_action:
        print(f"Both players selected {user_chose}. It's a tie!")
    elif user_chose == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_chose == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_chose == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                break
