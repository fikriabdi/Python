import random

# rock, scissor, paper

def game_Win(comp, you):
    # if values are equal, declare a tie!
    if comp == you:
        return None
        
    # Check for all possibilities when computer chose "rock"
    elif comp == 'rock':
        if you == 'scissors':
            return False
        elif you == 'paper':
            return True
            
    # Check for all possibilities when computer chose "scissors"
    elif comp == 'scissors':
        if you == 'paper':
            return False
        elif you == 'rock':
            return True
            
    # Check for all possibilities when computer chose "paper"
    elif comp == 'paper':
        if you == 'rock':
            return False
        elif you == 'scissors':
            return True
    
print("Computer Turn: Rock(r), Scissors(s) or Paper(p)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 's'
elif randNo == 3:
    comp = 'p'

you = input("Your Turn: Rock(r) Scissors(s) or Paper(p)?")
Statements = game_Win(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if Statements == None:
    print("The game is a tie!")
elif Statements:
    print("You Win!")
else:
    print("You Lose!")

    