import random


t = eval (input("How Much Time You Have To Play :"))

player_win = 0
Comp_win = 0
def Player_in():
    player = input("Select one Option :")
    if player == "Rock":
        player = "r"
    elif player == "Paper":
        player = "p"
    elif player == "Scissor":
        player = "s"
    else:
        print(player+" Not Found Try again")
    return player

def Comp_in():
    comp = ['r','p', 's']
    c = random.choice(comp)
    return c 

for i in range(1,t+1):
    print("Rock, Paper, Scissor")
    P = Player_in()
    c = Comp_in()
    if P == "r":
        if c == "p":
            print("You Lost You has Choose Rock and computer had Choose paper")
            Comp_win +=1    
            
    if P == "p":
        if c == "s":
            print("You Lost You has Choose Paper and computer had Choose Scissor ")
            Comp_win +=1    

    if P == "s":
        if c == "r":
            print("You Lost You has Choose Scissor and computer had Choose Rock ")
            Comp_win +=1
    if P == "r":
        if c == "r":
            print("Tie You and Computer Has chosed Rock")

    if P == "s":
        if c == "s":
            print("Tie You and Computer Has chosed Scissor")
     
    if P == "p":
        if c == "p":
            print("Tie You and Computer Has chosed Paper")

    if P == "r":
        if c == "s":
            print("You Won You has Choose Rock and computer had Choose Scissor")
            player_win +=1    
            
    if P == "s":
        if c == "p":
            print("You Won You had Choose Scissor and computer had Choose Paper ")
            player_win +=1    

    if P == "p":
        if c == "r":
            print("You won You has Choose Paper and computer had Choose Rock ")
            player_win +=1
    
    print("Total Score")
    print("Computer Score :"+str(Comp_win))
    print("Player Score :"+str(player_win))