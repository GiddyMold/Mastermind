from board import Board
from guess import Guess
from game import Game

guess = Guess()
game = Game()
colors = Board()
board = colors.createboard()

print(board)

guess.start()
for i in range(10):
    menuVAR = guess.menu()
    while(menuVAR==False):
        menuVAR = guess.menu()
    game.play(board,menuVAR,i)
game.lost(board)