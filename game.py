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
        self.colorList = ["red", "blue", "yellow", "black"]
        self.thingsCured = [False, False, False, False]

        self.oldGraveyards = []

        self.epidemicTrack = [2, 2, 2, 3, 3, 4]
        self.epidemicCounter = 0

        for count in range(3, 0, -1):
            for i in range(3):
                card = self.diseaseDeck.draw()
                self.board.pandemic.node[card]['cubes'] = count

        for i in range(2):
            self.pawn1.addCard(self.cureDeck.draw())
            self.pawn2.addCard(self.cureDeck.draw())
            self.pawn3.addCard(self.cureDeck.draw())
            self.pawn4.addCard(self.cureDeck.draw())
        self.cureDeck.insertEpidemics()
        self.board.printInfected()
        self.printPawnLocations()

    def printPawnLocations(self):
        locStr = ""
        for pawn in self.pawnList:
            locStr += pawn.name + ": " + pawn.currentCity + ", "
        print(locStr)
        print()
        
                
    def cure(self, city):
        if self.board.pandemic.node[city]['cubes'] > 0:
            self.board.pandemic.node[city]['cubes'] -=1

    def canCure(self, pawn):
        redCards = []
        blueCards = []
        yellowCards = []
        blackCards =[]
        
        for card in pawn.hand:
            if not self.thingsCured[0]:
                for city in self.board.redCities:
                    if card == city:
                        redCards += [card]
                if len(redCards) >= 3:
                    pawn.hand = [card for card in pawn.hand if card not in redCards]
                    self.thingsCured[0] = True
                    print("Cured Red!")
            if not self.thingsCured[1]:
                for city in self.board.blueCities:
                    if card == city:
                        blueCards += [card]
                if len(blueCards) >= 3:
                    pawn.hand = [card for card in pawn.hand if card not in blueCards]
                    self.thingsCured[1] = True
                    print("Cured Blue!")
            if not self.thingsCured[2]:
                for city in self.board.yellowCities:
                    if card == city:
                        yellowCards += [card]
                if len(yellowCards) >= 3:
                    pawn.hand = [card for card in pawn.hand if card not in yellowCards]
                    self.thingsCured[2] = True
                    print("Cured Yellow!")
            if not self.thingsCured[3]:
                for city in self.board.blackCities:
                    if card == city:
                        blackCards += [card]
                if len(blackCards) >= 3:
                    pawn.hand = [card for card in pawn.hand if card not in blackCards]
                    self.thingsCured[3] = True
                    print("Cured Black!")

    def runTurn(self, actions, pawn):
        currentPawn = self.pawnList[self.currentPawnIndex]
        print("Current pawn: " + currentPawn.name + ": " + currentPawn.currentCity)
        print("Cards: " + str(currentPawn.hand))
        print("Actions Taken: ")
        for action in actions:
            print(action)
            if action[1] == "move":
                pawn.move(action[2])
            elif action[1] == "cure":
                self.cure(action[2])
            else:
                 pawn.move(action[2])
                 pawn.removeCard(action[2])
        self.canCure(currentPawn)
        print("")
        
        for i in range(2):
            card = self.cureDeck.draw()
            if card == "Epidemic":
                print("Epidemic Drawn!")
                self.epidemicCounter += 1
                
                card = self.diseaseDeck.drawFromBottom()
                self.board.pandemic.node[card]['cubes'] = 3
                self.oldGraveyards += set(self.diseaseDeck.graveyard)
                
                self.diseaseDeck.appendGraveyard()
            else:
                pawn.addCard(card)

        for i in range(self.epidemicTrack[self.epidemicCounter]):
            card = self.diseaseDeck.draw()
            for city in self.board.redCities:
                if card == city and not self.thingsCured[0]:
                    self.board.infect(card)
            for city in self.board.blueCities:
                if card == city and not self.thingsCured[1]:
                    self.board.infect(card)
            for city in self.board.yellowCities:
                if card == city and not self.thingsCured[2]:
                    self.board.infect(card)
            for city in self.board.blackCities:
                if card == city and not self.thingsCured[3]:
                    self.board.infect(card)
            

        self.currentPawnIndex += 1
        if(self.currentPawnIndex == 4):
            self.currentPawnIndex = 0

        
        print(self.thingsCured)
        self.board.printInfected()
        self.printPawnLocations()
        

