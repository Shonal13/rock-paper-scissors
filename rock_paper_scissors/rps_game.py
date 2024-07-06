
#This is a rock paper scissors game

import random
import re

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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

run = True

def game_logic():
    global rock
    global scissors
    global paper

    #Computer sided random choice
    #available choices for the computer
    comp_avail_choice = [rock, paper, scissors]
    #random choice from available choices
    comp_choice = random.choice(comp_avail_choice)

    #User Human Choice
    human_chosen = input("Please enter the corresponding number for your choice :\n1.Rock\n2.Paper\n3.Scissors\n\nChoice : ")

    print()

    final_choice = re.sub('[a-zA-Z4-9.,"_/]', " ", human_chosen)

    if final_choice == "1":
        print(f"You chose :{rock}")
    elif final_choice == "2":
        print(f"You chose :{paper}")
    elif final_choice == "3":
        print(f"You chose :{scissors}")
    else:
        print("This is not a valid input !")

    print()
    print(f"Computer Chose:\n{comp_choice}")

    if comp_choice == rock and final_choice == "2":
        print("Congrats ! You Beat the Computer ! Well Done !")
    elif comp_choice == rock and final_choice == "1":
        print("This is a draw !")
    elif comp_choice == paper and final_choice == "3":
        print("Congrats ! You Beat the Computer ! Well Done !")
    elif comp_choice == paper and final_choice == "2":
        print("This is a draw !")
    elif comp_choice == scissors and final_choice == "1":
        print("Congrats ! You Beat the Computer ! Well Done !")
    elif comp_choice == scissors and final_choice == "3":
        print("This is a draw !")
    else:
        print("Computer Wins ! You Lose !")


game_logic()