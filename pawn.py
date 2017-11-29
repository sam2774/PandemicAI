class pawn(object):
    def __init__(self, name, currentCity):
        self.name = name
        self.currentCity = currentCity
        self.hand = []
    
    def move(self, newCity):
        self.currentCity = newCity
    
    def getCity(self):
        return str(currentCity)
    
    def addCard(self, card):
        self.hand.append(card)
    
    def getHand(self):
        for card in self.hand:
            print(card)

