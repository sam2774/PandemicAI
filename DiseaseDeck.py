import random

class DiseaseDeck():
    # This is the disease deck. There will only ever be 1 DiseaseDeck object
    def __init__(self):
        unshuffled = ["San Francisco", "Chicago", "Montreal", "New York", "Atlanta", "Washington", "London", "Madrid", "Paris", "Essen", 
                      "Milan", "St. Petersburg", "Los Angeles", "Mexico City", "Miami", "Bogota", "Lima", "Santiago", "Buenos Aires", "Sao Paulo",
                      "Lagos", "Kinshasa", "Johannesburg", "Khartoum", "Algiers", "Istanbul", "Cairo", "Moscow", "Baghdad", "Riyadh", 
                      "Tehran", "Karachi", "Mumbai", "Delhi", "Chennai", "Kolkata", "Bangkok", "Jakarta", "Beijing", "Shanghai", 
                      "Hong Kong", "Ho Chi Minh City", "Seoul", "Taipei", "Manila", "Sydney", "Tokyo", "Osaka"]
        shuffled = []
        while (unshuffled.__len__() > 0):
            i = random.randrange(0, unshuffled.__len__())
            shuffled.append(unshuffled[i])
            unshuffled.__delitem__(i)
        self.deck = shuffled
        self.graveyard = []
        
    def draw(self):
        card = self.deck.pop()
        self.graveyard.append(card)
        print(card)
        return card

    def appendGraveyard(self):
        grave = self.graveyard
        while (grave.__len__() > 0):
            i = random.randrange(0, grave.__len__())
            self.deck.append(grave[i])
            grave.__delitem__(i)
        self.graveyard = grave
        
    def drawFromBottom(self):
        card = self.deck[0]
        self.deck.__delitem__(0)
        self.graveyard.append(card)
        print (card)
        return card
