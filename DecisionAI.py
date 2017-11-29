from game import Game
import copy

class AI():
    def __init__(self):
        self.variable = "yes"
    def chooseTurn(self,game):
        actionTuple = []
        pawn = game.pawnList[game.currentPawnIndex]
        neighbors = game.board.pandemic.neighbors(pawn.currentCity)
        firstActions = []
        for neighbor in neighbors:
            newGame = copy.deepcopy(game)
            pawn = newGame.pawnList[newGame.currentPawnIndex]
            pawn.move(neighbor)
            firstActions.append((newGame, "move", neighbor))
            #AI part goes here
        #rest of actions
        secondActions = []
        for action in firstActions:
            pawn = action[0].pawnList[action[0].currentPawnIndex]
            neighbors = action[0].board.pandemic.neighbors(pawn.currentCity)
            for neighbor in neighbors:
                newGame = copy.deepcopy(action[0])
                pawn = newGame.pawnList[newGame.currentPawnIndex]
                pawn.move(neighbor)
                secondActions.append((newGame, "move", neighbor))
            
        #secondActions = prune(secondActions)        
        return actionTuple

ai = AI()       
game = Game()
game.initialInfect()
game.initialHands()
actions = ai.chooseTurn(game)
