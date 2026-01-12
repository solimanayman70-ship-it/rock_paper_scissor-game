import random

# the simpols of the game
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# computer_selection
game = ["rock", "paper", "scissor"]
teto = random.choice(game)

# human selection
print("Welcome to the game")
selectio_human = input("Make a selection (rock, paper, scissor)")
print("Your selection is:", selectio_human)
if selectio_human == "rock":
    print (rock)
elif selectio_human == "paper":
    print (paper)
elif selectio_human == "scissor":
    print (scissors)
else:
    print("Invalid selection")

print("Computed selection is:", teto)
if teto == "rock":
    print(rock)
elif teto == "paper":
    print(paper)
elif teto == "scissor":
    print(scissors)
else:
    print("Invalid selection")

if selectio_human == "rock" and teto == "scissor":
    print("You Win")
elif selectio_human == "rock" and teto == "rock":
    print("Draw")
elif selectio_human == "paper" and teto == "rock":
    print("You Win")
elif selectio_human == "paper" and teto == "paper":
    print("Draw")
elif selectio_human == "scissor" and teto == "paper":
    print("You Win")
elif selectio_human == "scissor" and teto == "scissor":
    print("Draw")
else:
    print("You Lose")


