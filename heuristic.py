def heuristic(self, game):
    heuristic = 0
    
    heuristicCubeSumBlue = 0
    heuristicCubeSumBlack = 0
    heuristicCubeSumRed = 0
    heuristicCubeSumYellow = 0
    
    cubeSumList = [heuristicCubeSumBlue, heuristicCubeSumBlack, heuristicCubeSumRed, heuristicCubeSumYellow]
    blueCities = game.board.pandemic.node['blue']
    blackCities = game.borad.pandemic.node['black']
    redCities = game.board.pandemic.node['red']
    yellowCities = game.board.pandemic.node['yellow']
    citiesList = [blueCities, blackCities, redCities, yellowCities]
    colorList = ["blue", "black", "red", "yellow"]
    
    for region in range(4):
        for city in citiesList[region]:
            probability = self.prob(self, game, city)
            for pawn in self.game.pawnList:
                pawnCity = self.game.pawn.currentCity
                if game.board.pandemic.node[city]['cubes'] == 2 and city == pawnCity:
                    cubeSumList[region] += 2
                    cubeSumList[region] += 2 * probability
                elif game.board.pandemic.node[city]['cubes'] == 3 and city == pawnCity:
                    cubeSumList[region] += 3
                    cubeSumList[region] += 3 * probability
                elif game.board.pandemic.node[city]['cubes'] == 1 and city == pawnCity:
                    cubeSumList[region] += 0.5
                    cubeSumList[region] += 0.5 * probability
                elif game.board.pandemic.node[city]['cubes'] == 2:
                    cubeSumList[region] += 3
                    cubeSumList[region] += 3 * probability
                elif game.board.pandemic.node[city]['cubes'] == 3:
                    cubeSumList[region] += 5
                    cubeSumList[region] += 5 * probability
                else:
                    cubeSumList[region] += game.board.pandemic.node[city]['cubes'] * probability
        for pawn in self.game.pawnList:
            city = self.game.pawn.currentCity
            if game.board.pandemic.node[city]['color'] == colorList[region]:
                cubeSumList[region] -= 10

    heuristic = heuristicCubeSumBlue + heuristicCubeSumBlack + heuristicCubeSumRed + heuristicCubeSumYellow

    return heuristic

def prob(self, game, city):
    prob = 0
    for card in game.diseaseDeck.deck:
        if card == city:
            prob = 1 / len(game.diseaseDeck.deck) #will probably need to change this to len(deck) choose 2 probability
    return prob
