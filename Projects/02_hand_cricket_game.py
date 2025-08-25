'''PROJECT DESCRIPTION:
    THIS IS A CODE OF A GAME WHICH WE USED TO PLAY IN OUR CHILDHOOD
    
    RULE: WHEN YOUR INTERGER INPUT AND COMPUTER NUMBER MATCHES YOU ARE OUT''' 
import random
import sys               #LEARNT THIS FROM AI CHATGPT
computer = random.choice([1,2,3,4,5,6])
user = int(input("enter a number(1-6): "))
a = user
x = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6"}
rev_x = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6}
print(f"YOU CHOSE: {x[user]} || COMPUTER CHOSE:{x[computer]}")

# if(c)
def hand_cricket1():       #FUNCTION DEFINITION
    if(computer==user):
        print("OUT!!")
        sys.exit()         #USED THIS TO BREAK THE FUNCTION AS SOON AS THE USER IS OUT!! IT SEEMED TO ME VERY USEFUL
    elif(computer!=user):
        print(f"YOUR SCORE: {user}")

hand_cricket1()            #FUNCTION CALL
print(f"TOTAL SCORE: {user}\n")


computer2 = random.choice([1,2,3,4,5,6])
user2 = int(input("ENTER YOUR NUMBER(0-6): "))
def hand_cricket2():
    if(computer2==user2):
        print("OUT!!")
        sys.exit()
    elif(computer2!=user2):
        print(f"YOUR SCORE: {user2}")

print(f"YOU CHOSE: {x[user2]} || COMPUTER CHOSE:{x[computer2]}")
hand_cricket2()                              
print(f"TOTAL SCORE: {user + user2}\n ")

computer3 = random.choice([1,2,3,4,5,6])
user3 = int(input("ENTER YOUR NUMBER(0-6): "))
def hand_cricket3():
    if(computer3==user3):
        print("OUT!!")
        sys.exit()
    elif(computer3!=user3):
        print(f"YOUR SCORE: {user3}")
print(f"YOU CHOSE: {x[user3]} || COMPUTER CHOSE:{x[computer3]}")
hand_cricket3()
print(f"TOTAL SCORE: {user + user2 + user3}\n ")

computer4 = random.choice([1,2,3,4,5,6])
user4 = int(input("ENTER YOUR NUMBER(0-6): "))
def hand_cricket4():
    if(computer4==user4):
        print("OUT!!") 
        sys.exit()
    elif(computer4!=user4):
        print(f"YOUR SCORE: {user4}")
print(f"YOU CHOSE: {x[user4]} || COMPUTER CHOSE:{x[computer4]}")
hand_cricket4()
print(f"TOTAL SCORE: {user + user2 + user3 + user4}\n ")

computer5 = random.choice([1,2,3,4,5,6])
user5 = int(input("ENTER YOUR NUMBER(0-6): "))
def hand_cricket5():
    if(computer5==user5):
        print("OUT!!")
        sys.exit()
    elif(computer5!=user5):
        print(f"YOUR SCORE: {user5}")
print(f"YOU CHOSE: {x[user5]} || COMPUTER CHOSE:{x[computer5]}")
hand_cricket5()
print(f"TOTAL SCORE: {user + user2 + user3 + user4 + user5}\n ")


computer6 = random.choice([1,2,3,4,5,6])
user6 = int(input("ENTER YOUR NUMBER(1-6): "))
def hand_cricket6():
    if(computer6==user6):
        print("OUT!!")
        sys.exit()
    elif(computer6!=user6):
        print(f"YOUR SCORE: {user5}")
print(f"YOU CHOSE: {x[user6]} || COMPUTER CHOSE:{x[computer6]}")
hand_cricket6()
print(f"TOTAL SCORE: {user + user2 + user3 + user4 + user5+ user6}")

#TESTED MANY TIMES NO ERROR IS EXPECTED BUT IF YOU CAN FIND TELL ME I WILL IMPROVE