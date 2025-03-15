import random

# выбор фигуры пользователем
print("Welcome to our game!")
roundGame = 1
while True:
    print(f"\nRound", roundGame)
    roundGame += 1
    user_choice = int(input("Please enter your choice: (0 - rock, 1 - scissors, 2 - paper): "))
    # print(type(user_choice))
    while user_choice < 0 or user_choice > 2:
        print("Wrong Answer. Please try again.")
        user_choice = int(input("Please enter your choice: (0 - rock, 1 - scissors, 2 - paper): "))

    print("Your choice is:", user_choice)

    # выбор фигуры компьютером
    pc_choice = random.randint(0, 2)
    print("Computer choice:", pc_choice)

    print("Results:")
    if user_choice == pc_choice:
        print("draw!")
    elif user_choice == 0:
        if pc_choice == 1:
            print("You win!")
        if pc_choice == 2:
            print("You lose!")
    elif user_choice == 1:
        if pc_choice == 0:
            print("You lose!")
        if pc_choice == 2:
            print("You win!")
    elif user_choice == 2:
        if pc_choice == 0:
            print("You win!")
        if pc_choice == 1:
            print("You lose!")
