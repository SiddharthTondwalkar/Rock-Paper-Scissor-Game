import random
print("Rock, Paper, Scissor")
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
        print("Rock Both Tie")

if P == "s":
    if c == "s":
        print("Scissor Both Tie")
    
if P == "p":
    if c == "p":
        print(" Paper Both Tie")

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
        print("You Lost You has Choose Paper and computer had Choose Rock ")
        player_win +=1
    
print(""+str(Comp_win))
print(""+str(player_win))