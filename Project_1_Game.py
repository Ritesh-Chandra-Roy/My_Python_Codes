import random

def check(comp_score, your_score):              #Function to decide winner!!
    if comp_score<your_score:
        return 'You Won!!'
    elif comp_score>your_score:
        return 'You Lost.'
    else:
        return 'its a Tie!!'

def batting(key):           #Function for Batting
    score = 0
    for i in range(6):
        print("Enter values 1 - 6 :- ")
        user = int(input(f"Ball {i+1}: "))
        comp = random.randint(1, 6)
        print(f"Computer got {comp}")
        if comp == user:
            print("Dot ball")
        elif user not in range(1, 7) and key == 2:
            print("Dot ball")
        else:
            if key == 1:
                score += comp
            else: 
                score += user
        print(f"Current Score: {score}  Balls left: {6-(i+1)}")
    print(f"final Score: {score}")
    return score

    


def toss_time():                #Function for Toss
    print('''Toss Time!!
        Choose Heads(1)/Tails(2):- ''')
    toss = input()
    coin = random.randint(1, 2)
    if coin == toss:
        print("You won the toss choose Bat(1)/Ball(2)")
        choice = input()
    else:
        print("You lost the toss!!")
        choice = random.randint(3, 4)
    return choice
###############################################Below is main Function#####################################################
print("~Welcome To Super Over~")
char = 'y'
while char == 'y':
    choice = toss_time()
    if choice == 2 or 3:
        print("You are Bowling First!!")
        comp_score = batting(1)
        print("Your Turn To Bat now!!")
        your_score = batting(2)
        print(check(comp_score, your_score)) 
    else:
        print("You are Batting First!!")
        your_score = batting(2)
        print("Your Turn To Bowl now!!")
        comp_score = batting(1)
        print(check(comp_score, your_score))
    char = input("Wanna Rematch?? (y/n): ")

