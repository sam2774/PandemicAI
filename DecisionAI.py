from game import Game

class AI():
    def __init__(self):
        self.variable = "yes"
    def chooseTurn(self):
        #AI part goes here
        choices = ["move","disinfect","playCard","tradeCard"]
        for pawn in self.pawnList:
            print("HI")
