import networkx as nx

class Pandemic():
    def __init__(self):
        self.pandemic = nx.Graph()
        self.pandemic.add_nodes_from(["San Francisco", "Chicago", "Montreal", "New York", "Atlanta", "Washington", "London", "Madrid", "Essen", "Paris", "Milan", "St. Petersburg"], color="blue", cubes=0)
        self.pandemic.add_nodes_from(["Los Angeles", "Mexico City", "Miami", "Bogota", "Lima", "Santiago", "Buenos Aires", "Sao Paulo", "Lagos", "Kinshasa", "Johannesburg", "Khartoum"], color="yellow", cubes=0)
        self.pandemic.add_nodes_from(["Algiers", "Istanbul", "Cairo", "Moscow", "Baghdad", "Riyadh", "Tehran", "Karachi", "Mumbai", "Delhi", "Chennai", "Kolkata"], color="black", cubes=0)
        self.pandemic.add_nodes_from(["Bangkok", "Jakarta", "Beijing", "Shanghai", "Hong Kong", "Ho Chi Minh City", "Seoul", "Taipei", "Manila", "Sydney", "Tokyo", "Osaka"], color="red", cubes=0)

        nx.add_star(self.pandemic, ["San Francisco", "Tokyo", "Manila", "Los Angeles", "Chicago"])
        nx.add_star(self.pandemic, ["Chicago", "San Francisco", "Los Angeles", "Mexico City", "Atlanta", "Montreal"])
        nx.add_star(self.pandemic, ["Montreal", "Chicago", "Washington", "New York"])
        nx.add_star(self.pandemic, ["New York", "Montreal", "Washington", "London", "Madrid"])
        nx.add_star(self.pandemic, ["Atlanta", "Chicago", "Washington", "Miami"])
        nx.add_star(self.pandemic, ["Washington", "Miami", "Atlanta", "Montreal", "New York"])
        nx.add_star(self.pandemic, ["London", "New York", "Madrid", "Paris", "Essen"])
        nx.add_star(self.pandemic, ["Madrid", "Washington", "London", "Paris", "Algiers", "Sao Paulo"])
        nx.add_star(self.pandemic, ["Essen", "London", "Paris", "Milan", "St. Petersburg"])
        nx.add_star(self.pandemic, ["Paris", "London", "Madrid", "Algiers", "Milan", "Essen"])
        nx.add_star(self.pandemic, ["Milan", "Essen", "Paris", "Istanbul"])
        nx.add_star(self.pandemic, ["St. Petersburg", "Essen", "Istanbul", "Moscow"])

        nx.add_star(self.pandemic, ["Los Angeles", "Sydney", "San Francisco", "Chicago", "Mexico City"])
        nx.add_star(self.pandemic, ["Mexico City", "Los Angeles", "Chicago", "Miami", "Bogota", "Lima"])
        nx.add_star(self.pandemic, ["Miami", "Atlanta", "Washington", "Bogota", "Mexico City"])
        nx.add_star(self.pandemic, ["Bogota", "Mexico City", "Miami", "Sao Paulo", "Buenos Aires", "Lima"])
        nx.add_star(self.pandemic, ["Lima", "Mexico City", "Bogota", "Santiago"])
        nx.add_star(self.pandemic, ["Santiago", "Lima", "Buenos Aires"])
        nx.add_star(self.pandemic, ["Buenos Aires", "Santiago", "Bogota", "Sao Paulo"])
        nx.add_star(self.pandemic, ["Sao Paulo", "Bogota", "Buenos Aires", "Madrid", "Lagos"])
        nx.add_star(self.pandemic, ["Lagos", "Sao Paulo", "Kinshasa", "Khartoum"])
        nx.add_star(self.pandemic, ["Kinshasa", "Lagos", "Johannesburg", "Khartoum"])
        nx.add_star(self.pandemic, ["Johannesburg", "Kinshasa", "Khartoum"])
        nx.add_star(self.pandemic, ["Khartoum", "Lagos", "Kinshasa", "Johannesburg", "Cairo"])

        nx.add_star(self.pandemic, ["Algiers", "Madrid", "Paris", "Istanbul", "Cairo"])
        nx.add_star(self.pandemic, ["Istanbul", "Milan", "St. Petersburg", "Moscow", "Baghdad", "Cairo", "Algiers"])
        nx.add_star(self.pandemic, ["Cairo", "Algiers", "Istanbul", "Baghdad", "Riyadh"])
        nx.add_star(self.pandemic, ["Moscow", "St. Petersburg", "Tehran", "Istanbul"])
        nx.add_star(self.pandemic, ["Baghdad", "Istanbul", "Cairo", "Riyadh", "Karachi", "Tehran"])
        nx.add_star(self.pandemic, ["Algiers", "Cairo", "Baghdad", "Karachi"])
        nx.add_star(self.pandemic, ["Tehran", "Moscow", "Delhi", "Karachi", "Baghdad"])
        nx.add_star(self.pandemic, ["Karachi", "Tehran", "Delhi", "Mumbai", "Riyadh", "Baghdad"])
        nx.add_star(self.pandemic, ["Mumbai", "Karachi", "Delhi", "Chennai"])
        nx.add_star(self.pandemic, ["Delhi", "Tehran", "Karachi", "Mumbai", "Chennai", "Kolkata"])
        nx.add_star(self.pandemic, ["Chennai", "Mumbai", "Delhi", "Kolkata", "Bangkok", "Jakarta"])
        nx.add_star(self.pandemic, ["Kolkata", "Delhi", "Chennai", "Bangkok", "Hong Kong"])

        nx.add_star(self.pandemic, ["Bangkok", "Chennai", "Kolkata", "Hong Kong", "Ho Chi Minh City", "Jakarta"])
        nx.add_star(self.pandemic, ["Jakarta", "Chennai", "Bangkok", "Ho Chi Minh City", "Sydney"])
        nx.add_star(self.pandemic, ["Beijing", "Seoul", "Shanghai"])
        nx.add_star(self.pandemic, ["Shanghai", "Beijing", "Seoul", "Tokyo", "Taipei", "Hong Kong"])
        nx.add_star(self.pandemic, ["Hong Kong", "Shanghai", "Taipei", "Manila", "Ho Chi Minh City", "Bangkok", "Kolkata"])
        nx.add_star(self.pandemic, ["Ho Chi Minh City", "Bangkok", "Hong Kong", "Manila", "Jakarta"])
        nx.add_star(self.pandemic, ["Seoul", "Beijing", "Shanghai", "Tokyo"])
        nx.add_star(self.pandemic, ["Taipei", "Bangkok", "Hong Kong", "Manila", "Osaka"])
        nx.add_star(self.pandemic, ["Manila", "Taipei", "Hong Kong", "Ho Chi Minh City", "Sydney", "San Francisco"])
        nx.add_star(self.pandemic, ["Sydney", "Jakarta", "Manila", "Los Angeles"])
        nx.add_star(self.pandemic, ["Tokyo", "Seoul", "Shanghai", "Osaka", "San Francisco"])
        nx.add_star(self.pandemic, ["Osaka", "Taipei", "Tokyo"])

        #Freezes the board, so no more nodes or edges can be added to the graph
        nx.freeze(self.pandemic)

        self.outbreakCounter = 0

    def infect(self,city, alreadyInfected=set()):
        if(self.pandemic.node[city]['cubes'] >= 3):
            self.outbreakCounter += 1
            if self.outbreakCounter >= 8:
                print("GAME OVER!")
            else:
                alreadyInfected.add(city)
                neighbors = set(self.pandemic.neighbors(city)) - alreadyInfected
                for n in neighbors:
                    self.infect(n)
        else:
            self.pandemic.node[city]['cubes'] += 1
