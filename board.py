import random
class Board():
    
    def __init__(self):
        pass

    def createboard(self):
        self.table = ['W','Y','B','O','R','M','G']
        self.colors = (self.table[random.randint(0,6)],self.table[random.randint(0,6)],self.table[random.randint(0,6)],self.table[random.randint(0,6)])
        return self.colors