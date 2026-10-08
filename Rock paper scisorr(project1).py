import random
User_choice= int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissor \n "))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
       (____)
---.__(___)

'''

game_images=[rock,paper,scissor]
if User_choice>=3 or User_choice<0:
    print("Invalid choice")
else:
    print(game_images[User_choice])
    computer_choice=random.randint(0,2)
    print("Computer chose: ",game_images[computer_choice])
    if computer_choice==User_choice:
        print("It's a tie")
    elif computer_choice == 0 and User_choice == 1:
        print("you win")
    elif computer_choice== 0 and User_choice == 2:
        print("you lose")
    elif computer_choice == 2 and User_choice == 1:
        print("you lose")
    elif computer_choice == 2 and User_choice == 0:
        print("you win")
    elif computer_choice==1 and User_choice==2:
        print("you win")
    elif computer_choice==1 and User_choice==0:
        print("you lose")
