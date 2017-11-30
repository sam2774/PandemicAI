import random

class CureDeck():
    # This is the cure deck. There will only ever be 1 CureDeck object
    def __init__(self):
        unshuffled = ["San Francisco", "Chicago", "Montreal", "New York", "Atlanta", "Washington", "London", "Madrid", "Paris", "Essen", 
                      "Milan", "St. Petersburg", "Los Angeles", "Mexico City", "Miami", "Bogota", "Lima", "Santiago", "Buenos Aires", "Sao Paulo",
                      "Lagos", "Kinshasa", "Johannesburg", "Khartoum", "Algiers", "Istanbul", "Cairo", "Moscow", "Baghdad", "Riyadh", 
                      "Tehran", "Karaci", "Mumbai", "Delhi", "Chennai", "Kolkata", "Bangkok", "Jakarta", "Beijing", "Shanghai", 
                      "Hong Kong", "Ho Chi Minh City", "Seoul", "Taipei", "Manila", "Sydney", "Tokyo", "Osaka"]
        shuffled = []
        while (unshuffled.__len__() > 0):
            i = random.randrange(0, unshuffled.__len__())
            shuffled.append(unshuffled[i])
            unshuffled.__delitem__(i)
        self.deck = shuffled
        
    def draw(self):
        card = self.deck.pop()
        return card

    def insertEpidemics(self):
        cureDeck = []
        epidemic1 = []
        epidemic2 = []
        epidemic3 = []
        epidemic4 = []
        epidemic5 = []
        epidemicList = [epidemic1, epidemic2, epidemic3, epidemic4, epidemic5]
        for i in range(0, 5):
            for j in range(0, 8):
                epidemicList[i].append(self.deck[0])
                self.deck.__delitem__(0)
            epidemicList[i].append("Epidemic")
            while (epidemicList[i].__len__() > 0):
                k = random.randrange(0, epidemicList[i].__len__())
                cureDeck.append(epidemicList[i][k])
                epidemicList[i].__delitem__(k)
        self.deck = cureDeck
