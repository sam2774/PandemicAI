from game import Game
import copy

class AI():
    def __init__(self):
        self.variable = "yes"
    def heuristic(self, game):
        heuristic = 0
        
        cubeSumList = [0, 0, 0, 0]
        blueCities = game.board.blueCities
        blackCities = game.board.blackCities
        redCities = game.board.redCities
        yellowCities = game.board.yellowCities
        citiesList = [blueCities, blackCities, redCities, yellowCities]
        colorList = ["blue", "black", "red", "yellow"]
        
        for region in range(4):
            for city in citiesList[region]:
                probability = self.prob(game, city)
                pawnCity = self.isPawnCity(game, city)
                if game.board.pandemic.node[city]['cubes'] == 2 and pawnCity:
                    cubeSumList[region] += 2
                    cubeSumList[region] += 2 * probability
                elif game.board.pandemic.node[city]['cubes'] == 3 and pawnCity:
                    cubeSumList[region] += 3
                    cubeSumList[region] += 3 * probability
                elif game.board.pandemic.node[city]['cubes'] == 1 and pawnCity:
                    cubeSumList[region] += 0.5
                    cubeSumList[region] += 0.5 * probability
                elif game.board.pandemic.node[city]['cubes'] == 2:
                    cubeSumList[region] += 5
                    cubeSumList[region] += 5 * probability
                elif game.board.pandemic.node[city]['cubes'] == 3:
                    cubeSumList[region] += 10
                    cubeSumList[region] += 10 * probability
                else:
                    cubeSumList[region] += game.board.pandemic.node[city]['cubes']
                    cubeSumList[region] += game.board.pandemic.node[city]['cubes'] * probability

        heuristic = sum(cubeSumList)

        return heuristic

    def isPawnCity(self, game, city):
        for pawn in game.pawnList:
            if pawn.currentCity == city :
                return True
        return False

    def prob(self, game, city):
        prob = 0
        if(game.oldGraveyards == []):
            prob = 1 / len(game.diseaseDeck.deck)
            for card in game.diseaseDeck.graveyard:
                if card == city:
                    prob = 0
        else:
            for card in game.oldGraveyards[-1]:
                if card == city:
                    prob = 1 / len(game.oldGraveyards[-1])
        return prob
    
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

    def prune(self, actionList, cutoff):
        prunedList = []
        for action in actionList:
            h = self.heuristic(action.game)
            if(h <= cutoff):
                prunedList.append(action)
        return prunedList
        
    
    def chooseTurn(self, game):
        actionTuple = []
        cutoff = self.heuristic(game)
        firstActions = []
        gameRecord = GameRecord(game, [])
        firstActions += self.analyzeNeighbors(gameRecord)
        firstActions += self.analyzeCards(gameRecord)
        if game.board.pandemic.node[game.pawnList[game.currentPawnIndex].currentCity]['cubes'] > 1:
            firstActions += self.cureCity(gameRecord)
            
            #AI part goes here
        secondActions = []
        for action in firstActions:
            secondActions += self.analyzeNeighbors(action)
            secondActions += self.analyzeCards(action)
            if action.game.board.pandemic.node[action.game.pawnList[action.game.currentPawnIndex].currentCity]['cubes'] > 1:
                secondActions += self.cureCity(action)

        thirdActions = []
        for action in secondActions:
            thirdActions += self.analyzeNeighbors(action)
            thirdActions += self.analyzeCards(action)
            if action.game.board.pandemic.node[action.game.pawnList[action.game.currentPawnIndex].currentCity]['cubes'] > 1:
                thirdActions += self.cureCity(action)

        thirdActions = self.prune(thirdActions, cutoff)

        fourthActions = []
        for action in thirdActions:
            fourthActions += self.analyzeNeighbors(action)
            fourthActions += self.analyzeCards(action)
            if action.game.board.pandemic.node[action.game.pawnList[action.game.currentPawnIndex].currentCity]['cubes'] > 1:
                fourthActions += self.cureCity(action)

        print("Number of nodes: " + str(len(firstActions)) + ", " + str(len(secondActions))+ ", " + str(len(thirdActions))+ ", " + str(len(fourthActions)))

        bestAction = fourthActions[0].record
        bestHeuristic = self.heuristic(fourthActions[0].game)
        for action in fourthActions:
            newHeuristic = self.heuristic(action.game)
            if newHeuristic < bestHeuristic:
                bestHeuristic = newHeuristic
                bestAction = action.record

        return bestAction

class GameRecord():
    def __init__(self, game, record):
        self.game = game
        self.record = record

ai = AI()       
game = Game()

turn = 1
while True:
    print("Turn: " + str(turn))
    actions = ai.chooseTurn(game)
    game.runTurn(actions, game.pawnList[game.currentPawnIndex])
    turn += 1
