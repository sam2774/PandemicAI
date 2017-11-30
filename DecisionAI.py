from game import Game
import copy

class AI():
    def __init__(self):
        self.variable = "yes"

    def analyzeNeighbors(self, gameRecord):
        actionList = []
        game = gameRecord.game
        originalPawn = game.pawnList[game.currentPawnIndex]
        neighbors = game.board.pandemic.neighbors(originalPawn.currentCity)
        prevCity = "Atlanta"
        if gameRecord.record != []:
            prevCity = gameRecord.record[-1][0]
        for neighbor in neighbors:
            if(neighbor == prevCity):
                continue
            newGame = copy.deepcopy(game)
            pawn = newGame.pawnList[newGame.currentPawnIndex]
            
            pawn.move(neighbor)
            newRecord = gameRecord.record + [(originalPawn.currentCity, "move", neighbor)]
            actionList.append(GameRecord(newGame, newRecord))
        return actionList

    def analyzeCards(self, gameRecord):
        actionList = []
        game = gameRecord.game
        originalPawn = game.pawnList[game.currentPawnIndex]
        prevCity = "Atlanta"
        if gameRecord.record != []:
            prevCity = gameRecord.record[-1][0]
        for card in originalPawn.hand:
            if card == prevCity or card == originalPawn.currentCity:
                continue
            newGame = copy.deepcopy(game)
            pawn = newGame.pawnList[newGame.currentPawnIndex]
            pawn.useCard(card)
            newRecord = gameRecord.record + [(originalPawn.currentCity, "playCard", card)]
            actionList.append(GameRecord(newGame, newRecord))
        return actionList

    def cureCity(self, gameRecord):
        actionList =[]
        game = gameRecord.game
        originalPawn = game.pawnList[game.currentPawnIndex]
        newGame = copy.deepcopy(game)
        city = originalPawn.currentCity
        newGame.cure(city)
        newRecord = gameRecord.record + [(city, "cure", city)]
        actionList.append(GameRecord(newGame, newRecord))
        return actionList
        
    
    def chooseTurn(self, game):
        actionTuple = []

        firstActions = []
        gameRecord = GameRecord(game, [])
        firstActions += self.analyzeNeighbors(gameRecord)
        firstActions += self.analyzeCards(gameRecord)
        if game.board.pandemic.node[game.pawnList[game.currentPawnIndex].currentCity]['cubes'] > 0:
            firstActions += self.cureCity(gameRecord)
            
            #AI part goes here
        secondActions = []
        for action in firstActions:
            secondActions += self.analyzeNeighbors(action)
            secondActions += self.analyzeCards(action)
            if action.game.board.pandemic.node[action.game.pawnList[action.game.currentPawnIndex].currentCity]['cubes'] > 0:
                secondActions += self.cureCity(action)

        thirdActions = []
        for action in secondActions:
            thirdActions += self.analyzeNeighbors(action)
            thirdActions += self.analyzeCards(action)
            if action.game.board.pandemic.node[action.game.pawnList[action.game.currentPawnIndex].currentCity]['cubes'] > 0:
                thirdActions += self.cureCity(action)

        fourthActions = []
        for action in thirdActions:
            fourthActions += self.analyzeNeighbors(action)
            fourthActions += self.analyzeCards(action)
            if action.game.board.pandemic.node[action.game.pawnList[action.game.currentPawnIndex].currentCity]['cubes'] > 0:
                fourthActions += self.cureCity(action)
    #Prune
        
##        print(firstActions)
##        print("\n")
##        print(secondActions)
##        print("\n")
##        print(thirdActions)
##        print("\n")
##        print(fourthActions)
        print("Number of nodes: " + str(len(firstActions)) + ", " + str(len(secondActions))+ ", " + str(len(thirdActions))+ ", " + str(len(fourthActions)))

        #choose best action  
        actionTuple = fourthActions[0].record
        return actionTuple

class GameRecord():
    def __init__(self, game, record):
        self.game = game
        self.record = record

ai = AI()       
game = Game()
actions = ai.chooseTurn(game)

game.runTurn(actions, game.pawnList[game.currentPawnIndex])

actions = ai.chooseTurn(game)
