class pawn(object):
    def __init__(self, name, currentCity):
        self.name = name
        self.currentCity = currentCity
        self.hand = []
    
    def move(self, newCity):
        self.currentCity = newCity
    
    def getCity(self):
        return str(self.currentCity)
    
    def addCard(self, card):
        self.hand.append(card)

    def removeCard(self,removeCard):
        for i in range (len(self.hand)):
            if self.hand[i] == removeCard:
                self.hand.__delitem__(i)
    
    def getHand(self):
        for card in self.hand:
            print(card)

