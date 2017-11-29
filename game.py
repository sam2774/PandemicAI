from pawn import pawn
from DiseaseDeck import DiseaseDeck
from pandemic import Pandemic


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

        self.epidemicCounter = 2

        #cureDeck goes here
    def initialInfect(self):
        for count in range(3, 0, -1):
            for i in range(3):
                card = self.diseaseDeck.draw()
                print(card)
                self.board.pandemic.node[card]['cubes'] = count
                print(self.board.pandemic.node[card])
                
    def cure(self, city):
        if self.board.pandemic.node[city]['cubes'] > 0:
            self.board.pandemic.node[city]['cubes'] -=1
        print (self.board.pandemic.node[city]['cubes'])

    
    def initialHands(self):
        for i in range(2):
            #Draw new card each time
            self.pawn1.addCard("Rando Card")
            self.pawn2.addCard("Rando Card")
            self.pawn3.addCard("Rando Card")
            self.pawn4.addCard("Rando Card")

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
                 
            print (pawn.getCity())               
            #takeAction(action[i])

        #draw 2 from cure deck
        #if(draw == epidemic):
            #doEpedimic()

        for i in range(self.epidemicCounter):
            card = self.diseaseDeck.draw()
            self.board.infect(card)
          #set pawn index  
        
        
game = Game()
game.initialInfect()
game.initialHands()

game.runTurn([("move","San Francisco"), ("cure", "San Francisco"), ("move", "Mexico City"), ("playcard", "Hong Kong")], game.pawn1)

game.cure("London")

