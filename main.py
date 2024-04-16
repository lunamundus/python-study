from random import randint

user_choice = int(input("Choose number: "))

pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print(f"You win!")
elif user_choice > pc_choice:
    print(f"Lower than your choice! Computer chose {pc_choice}.")
elif user_choice < pc_choice:
    print(f"Higher than your choice! Computer Chose {pc_choice}.")