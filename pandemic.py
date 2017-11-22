import networkx as nx

pandemic = nx.Graph()
pandemic.add_nodes_from(["San Fransisco", "Chicago", "Montreal", "New York", "Atlanta", "Washington", "London", "Madrid", "Essen", "Paris", "Milan", "St. Petersburg"], color="blue", cubes=0)
pandemic.add_nodes_from(["Los Angeles", "Mexico City", "Miami", "Bogota", "Lima", "Santiago", "Buenos Aires", "Sao Paulo", "Lagos", "Kinshasa", "Johanesburg", "Khartoum"], color="yellow", cubes=0)
pandemic.add_nodes_from(["Algiers", "Istanbul", "Cairo", "Moscow", "Baghdad", "Riyadh", "Tehran", "Karachi", "Mumbai", "Delhi", "Chennai", "Kolkata"], color="black", cubes=0)
pandemic.add_nodes_from(["Bangkok", "Jakarta", "Beijing", "Shanghai", "Hong Kong", "Ho Chi Minh City", "Seoul", "Taipei", "Manila", "Sydney", "Tokyo", "Osaka"], color="red", cubes=0)

nx.add_star(pandemic, ["San Fransisco", "Tokyo", "Manila", "Los Angeles", "Chicago"])
nx.add_star(pandemic, ["Chicago", "San Fransisco", "Los Angeles", "Mexico City", "Atlanta", "Montreal"])
nx.add_star(pandemic, ["Montreal", "Chicago", "Washington", "New York"])
nx.add_star(pandemic, ["New York", "Montreal", "Washington", "London", "Madrid"])
nx.add_star(pandemic, ["Atlanta", "Chicago", "Washington", "Miami"])
nx.add_star(pandemic, ["Washington", "Miami", "Atlanta", "Montreal", "New York"])
nx.add_star(pandemic, ["London", "New York", "Madrid", "Paris", "Essen"])
nx.add_star(pandemic, ["Madrid", "Washington", "London", "Paris", "Algiers", "Sao Paulo"])
nx.add_star(pandemic, ["Essen", "London", "Paris", "Milan", "St. Petersburg"])
nx.add_star(pandemic, ["Paris", "London", "Madrid", "Algiers", "Milan", "Essen"])
nx.add_star(pandemic, ["Milan", "Essen", "Paris", "Istanbul"])
nx.add_star(pandemic, ["St. Petersburg", "Essen", "Istanbul", "Moscow"])

nx.add_star(pandemic, ["Los Angeles", "Sydney", "San Fransisco", "Chicago", "Mexico City"])
nx.add_star(pandemic, ["Mexico City", "Los Angeles", "Chicago", "Miami", "Bogota", "Lima"])
nx.add_star(pandemic, ["Miami", "Atlanta", "Washington", "Bogota", "Mexico City"])
nx.add_star(pandemic, ["Bogota", "Mexico City", "Miami", "Sao Paulo", "Buenos Aires", "Lima"])
nx.add_star(pandemic, ["Lima", "Mexico City", "Bogota", "Santiago"])
nx.add_star(pandemic, ["Santiago", "Lima", "Buenos Aires"])
nx.add_star(pandemic, ["Buenos Aires", "Santiago", "Bogota", "Sao Paulo"])
nx.add_star(pandemic, ["Sao Paulo", "Bogota", "Buenos Aires", "Madrid", "Lagos"])
nx.add_star(pandemic, ["Lagos", "Sao Paulo", "Kinshasa", "Khartoum"])
nx.add_star(pandemic, ["Kinshasa", "Lagos", "Johanesburg", "Khartoum"])
nx.add_star(pandemic, ["Johanesburg", "Kinshasa", "Khartoum"])
nx.add_star(pandemic, ["Khartoum", "Lagos", "Kinshasa", "Johanesburg", "Cairo"])

nx.add_star(pandemic, ["Algiers", "Madrid", "Paris", "Istanbul", "Cairo"])
nx.add_star(pandemic, ["Istanbul", "Milan", "St. Petersburg", "Moscow", "Baghdad", "Cairo", "Algiers"])
nx.add_star(pandemic, ["Cairo", "Algiers", "Istanbul", "Baghdad", "Riyadh"])
nx.add_star(pandemic, ["Moscow", "St. Petersburg", "Tehran", "Istanbul"])
nx.add_star(pandemic, ["Baghdad", "Istanbul", "Cairo", "Riyadh", "Karachi", "Tehran"])
nx.add_star(pandemic, ["Algiers", "Cairo", "Baghdad", "Karachi"])
nx.add_star(pandemic, ["Tehran", "Moscow", "Delhi", "Karachi", "Baghdad"])
nx.add_star(pandemic, ["Karachi", "Tehran", "Delhi", "Mumbai", "Riyadh", "Baghdad"])
nx.add_star(pandemic, ["Mumbai", "Karachi", "Delhi", "Chennai"])
nx.add_star(pandemic, ["Delhi", "Tehran", "Karachi", "Mumbai", "Chennai", "Kolkata"])
nx.add_star(pandemic, ["Chennai", "Mumbai", "Delhi", "Kolkata", "Bangkok", "Jakarta"])
nx.add_star(pandemic, ["Kolkata", "Delhi", "Chennai", "Bangkok", "Hong Kong"])

nx.add_star(pandemic, ["Bangkok", "Chennai", "Kolkata", "Hong Kong", "Ho Chi Minh City", "Jakarta"])
nx.add_star(pandemic, ["Jakarta", "Chennai", "Bangkok", "Ho Chi Minh City", "Sydney"])
nx.add_star(pandemic, ["Beijing", "Seoul", "Shanghai"])
nx.add_star(pandemic, ["Shanghai", "Beijing", "Seoul", "Tokyo", "Taipei", "Hong Kong"])
nx.add_star(pandemic, ["Hong Kong", "Shanghai", "Taipei", "Manila", "Ho Chi Minh City", "Bangkok", "Kolkata"])
nx.add_star(pandemic, ["Ho Chi Minh City", "Bangkok", "Hong Kong", "Manila", "Jakarta"])
nx.add_star(pandemic, ["Seoul", "Beijing", "Shanghai", "Tokyo"])
nx.add_star(pandemic, ["Taipei", "Bangkok", "Hong Kong", "Manila", "Osaka"])
nx.add_star(pandemic, ["Manila", "Taipei", "Hong Kong", "Ho Chi Minh City", "Sydney", "San Fransisco"])
nx.add_star(pandemic, ["Sydney", "Jakarta", "Manila", "Los Angeles"])
nx.add_star(pandemic, ["Tokyo", "Seoul", "Shanghai", "Osaka", "San Fransisco"])
nx.add_star(pandemic, ["Osaka", "Taipei", "Tokyo"])

#Freezes the board, so no more nodes or edges can be added to the graph
nx.freeze(pandemic)

outbreakCounter = 0

def infect(city, alreadyInfected=set()):
    if(pandemic.node[city]['cubes'] >= 3):
        global outbreakCounter
        outbreakCounter += 1
        if outbreakCounter >= 8:
            print("GAME OVER!")
        else:
            alreadyInfected.add(city)
            neighbors = set(pandemic.neighbors(city)) - alreadyInfected
            for n in neighbors:
                infect(n)
    else:
        pandemic.node[city]['cubes'] += 1
