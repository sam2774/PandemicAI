from pawn import pawn
from DiseaseDeck import DiseaseDeck
from pandemic import Pandemic
from CureDeck import CureDeck


class Game():
    def __init__(self):
        self.pawn1 = pawn("White", "Atlanta")
        self.pawn2 = pawn("Pink", "Atlanta")
        self.pawn3 = pawn("Grey", "Atlanta")
        self.pawn4 = pawn("Blue", "Atlanta")
        self.pawnList = [self.pawn1, self.pawn2,self.pawn3,self.pawn4]
        self.diseaseDeck = DiseaseDeck()
        self.currentPawnIndex = 0
        self.board = Pandemic()
        self.cureDeck = CureDeck()

        self.epidemicTrack = [2, 2, 2, 3, 3, 4]
        self.epidemicCounter = 0

        for count in range(3, 0, -1):
            for i in range(3):
                card = self.diseaseDeck.draw()
                print(card)
                self.board.pandemic.node[card]['cubes'] = count
                print(self.board.pandemic.node[card])

        for i in range(2):
            self.pawn1.addCard(self.cureDeck.draw())
            self.pawn2.addCard(self.cureDeck.draw())
            self.pawn3.addCard(self.cureDeck.draw())
            self.pawn4.addCard(self.cureDeck.draw())
        self.cureDeck.insertEpidemics()
                
    def cure(self, city):
        if self.board.pandemic.node[city]['cubes'] > 0:
            self.board.pandemic.node[city]['cubes'] -=1
        print (self.board.pandemic.node[city]['cubes'])

    def runTurn(self, actions, pawn):
        for action in actions:
            print(action)
            if action[0] == "move":
                pawn.move(action[1])
            elif action[0] == "cure":
                self.cure(action[1])
            else:
                 pawn.move(action[1])
                 pawn.removeCard(action[1])
                 
            print (pawn.currentCity)               
            #takeAction(action[i])
        
        for i in range(2):
            card = self.cureDeck.draw()
            if card == "Epidemic":
                self.epidemicCounter += 1
                card = self.diseaseDeck.drawFromBottom()
                self.board.pandemic.node[card]['cubes'] = 3
                self.diseaseDeck.appendGraveyard()
            else:
                pawn.addCard(card)

        for i in range(self.epidemicTrack[self.epidemicCounter]):
            card = self.diseaseDeck.draw()
            self.board.infect(card)
        
        
game = Game()

#game.runTurn([("move","San Francisco"), ("cure", "San Francisco"), ("move", "Mexico City"), ("playcard", "Hong Kong")], game.pawn1)

