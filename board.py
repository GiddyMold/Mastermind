import random
class Board():
    
    def __init__(self):
        pass

    def createboard(self):
        self.table = ['W','Y','B','O','R','M']
        self.colors = (self.table[random.randint(0,5)],self.table[random.randint(0,5)],self.table[random.randint(0,5)],self.table[random.randint(0,5)])
        return self.colors