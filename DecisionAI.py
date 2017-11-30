from game import Game
import copy

class AI():
    def __init__(self):
        self.variable = "yes"

    def analyzeNeighbors(self, game):
        actionList = []
        originalPawn = game.pawnList[game.currentPawnIndex]
        neighbors = game.board.pandemic.neighbors(originalPawn.currentCity)
        for neighbor in neighbors:
            newGame = copy.deepcopy(game)
            pawn = newGame.pawnList[newGame.currentPawnIndex]
            pawn.move(neighbor)
            actionList.append((newGame, (originalPawn.currentCity, "move", neighbor)))
        return actionList

    def analyzeCards(self, game):
        actionList = []
        originalPawn = game.pawnList[game.currentPawnIndex]
        print(originalPawn.hand)
        for card in originalPawn.hand:
            newGame = copy.deepcopy(game)
            pawn = newGame.pawnList[newGame.currentPawnIndex]
            pawn.useCard(card)
            actionList.append((newGame, (originalPawn.currentCity, "playCard", card)))
        return actionList
    
    def chooseTurn(self,game):
        actionTuple = []
        
        firstActions = self.analyzeNeighbors(game)
        firstActions += self.analyzeCards(game)
            #AI part goes here
        #rest of actions
        secondActions = []
        for action in firstActions:
            secondActions += self.analyzeNeighbors(action[0])
            secondActions += self.analyzeCards(action[0])

        print(firstActions)
        print("\n")
        print(secondActions)
            
        #secondActions = prune(secondActions)        
        return actionTuple

ai = AI()       
game = Game()
actions = ai.chooseTurn(game)
