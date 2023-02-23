class Guess():

    def __init__(self):
        pass

    def menu(self):
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