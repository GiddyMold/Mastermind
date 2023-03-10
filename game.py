class Game():
    def __init__(self) -> None:
        pass

    def lost(self,board):
        print("\nGAME OVER! You lost!")
        print("The board was:",board)
        self.temp = input()
        exit()

    def win(self,left,board):
        print("\nCongratulations! You won with",left,"guesses left!")
        print("The board was:",board)
        self.temp = input()
        exit()

    def play(self,colors,guess,iteration):

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
            self.win(9-iteration,colors)

        if iteration < 9:
            print("Correct positions: "+str(correctPOS))
            print("Incorrect positions: "+str(incorrectPOS))
            if iteration < 8:
                print(str(9-iteration)+" guesses left!\n")
            else:
                print("1 guess left!\n")