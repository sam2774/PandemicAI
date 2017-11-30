class pawn(object):
    def __init__(self, name, currentCity):
        self.name = name
        self.currentCity = currentCity
        self.hand = []
    
    def move(self, newCity):
        self.currentCity = newCity
    
    def addCard(self, card):
        self.hand.append(card)

    def removeCard(self,removeCard):
        self.hand.remove(removeCard)

    def useCard(self, removeCard):
        self.move(removeCard)
        self.removeCard(removeCard)

