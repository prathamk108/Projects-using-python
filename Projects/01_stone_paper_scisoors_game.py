'''PROJECT DESCRIPTION:
    THIS IS A CODE OF A GAME WHICH WE USED TO PLAY IN OUR CHILDHOOD
    THIS I HAVE SEEN AND LEARNT 
    
    RULES: IN STONE VS PAPER = PAPER WINS
    IN STONE VS SCISOOR = STONE WINS
    IN SCISOOR VS PAPER = SCISOOR WINS''' 
import random
computer = random.choice([1,2,3])
name = (input("ENTER YOUR NAME: "))
user = int(input("ENTER A NUMBER(1-3): "))

dict = {1:"stone",2:"paper",3:"scisoor"}
print(f"{name} chose: {dict[user]}")

rev_dict = {"stone":1,"paper":2,"scisoor":3}
print(f"COMPUTER chose: {dict[computer]}")

def game():  # DEFINING FUNCTION
    if(computer==user):  # USING CONDITIONS
        print("TIE")
    else:
        if(computer==1 and user==2):  # NEST IF ELSE CONDITIONALS
            print(f"{name} WINS")
        elif(computer==1 and user==3):
            print(f"COMPUTER WINS")
        elif(computer==2 and user==1):
            print(f"COMPUTER WINS")
        elif(computer==2 and user==3):
            print(f"{name} WINS")
        elif(computer==3 and user==1):
            print(f"{name} WINS")
        elif(computer==3 and user==2):
            print(f"COMPUTER WINS")
        else:
            print("INVALID")
        
game() #FUNCTION CALL