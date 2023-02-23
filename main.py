import random
from board import Board

def createboard():
    table = ['W','Y','B','O','R','M','G']
    colors = (table[random.randint(0,6)],table[random.randint(0,6)],table[random.randint(0,6)],table[random.randint(0,6)])
    return colors

def menu():
    guess = input("Guess: ")
    if len(guess) != 4:
        print("You mistyped, try again:")
        return False
    for i in guess:
        if i.islower():
            print("CAPS ON THIS TIME! No lowercase letters!")
            return False
        if i.isdigit():
            print("No digits fellow friend! Only letters!")
            return False        
    return guess

def win(left,board):
    print("Congratulations! You won with",left,"guesses left!")
    print("The board was:",board)
    exit()

def play(colors,guess,iteration):

    correctPOS = 0
    incorrectPOS = 0
    flag = [False,False,False,False]
    flag2 = [False,False,False,False]

    for k in range(4):
        if guess[k] == colors[k]:
            correctPOS += 1
            flag[k] = True
    
    for k in range(4):
        if flag[k] == False:
            if guess[k] == colors[0] and flag[0] == False and flag2[0] == False:
                incorrectPOS += 1
                flag2[0] = True
                continue
            if guess[k] == colors[1] and flag[1] == False and flag2[1] == False:
                incorrectPOS += 1
                flag2[1] = True
                continue
            if guess[k] == colors[2] and flag[2] == False and flag2[2] == False:
                incorrectPOS += 1
                flag2[2] = True
                continue
            if guess[k] == colors[3] and flag[3] == False and flag2[3] == False:
                incorrectPOS += 1
                flag2[3] = True
                continue
    
    if(correctPOS==4):
        win(9-iteration,colors)

    print("Correct positions: "+str(correctPOS))
    print("Incorrect positions: "+str(incorrectPOS))
    print(str(9-iteration)+" guesses left!")  



board = createboard()
print(board)
for i in range(10):
    menuVAR = menu()
    while(menuVAR==False):
        menuVAR = menu()
    play(board,menuVAR,i)