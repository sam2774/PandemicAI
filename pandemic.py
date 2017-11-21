import networkx as nx

pandemic = nx.Graph()
pandemic.add_nodes_from(["San Fransisco", "Chicago", "Montreal", "New York", "Atlanta", "Washington", "London", "Madrid", "Essen", "Paris", "Milan", "St. Petersburg"], color="blue")
pandemic.add_nodes_from(["Los Angeles", "Mexico City", "Miami", "Bogota", "Lima", "Santiago", "Buenos Aires", "Sao Paulo", "Lagos", "Kinshasa", "Johanesburg", "Khartoum"], color="yellow")
pandemic.add_nodes_from(["Algiers", "Istanbul", "Cairo", "Moscow", "Baghdad", "Riyadh", "Tehran", "Karachi", "Mumbai", "Delhi", "Chennai", "Kolkata"], color="black")
pandemic.add_nodes_from(["Bangkok", "Jakarta", "Beijing", "Shanghai", "Hong Kong", "Ho Chi Minh City", "Seoul", "Taipei", "Manila", "Sydney", "Tokyo", "Osaka"], color="red")

pandemic.add_edges_from([("San Fransisco", "Tokyo"), ("San Fransisco", "Manila"), ("San Fransisco", "Los Angeles"), ("San Fransisco", "Chicago")])
pandemic.add_edges_from([("Chicago", "San Fransisco"), ("Chicago", "Los Angeles"), ("Chicago", "Mexico City"), ("Chicago", "Atlanta"), ("Chicago", "Montreal")])
pandemic.add_edges_from([("Montreal", "Chicago"), ("Montreal", "Washington"), ("Montreal", "New York")])
pandemic.add_edges_from([("New York", "Montreal"), ("New York", "Washington"), ("New York", "London"), ("New York", "Madrid")])
pandemic.add_edges_from([("Atlanta", "Chicago"), ("Atlanta", "Washington"), ("Atlanta", "Miami")])
pandemic.add_edges_from([("Washington", "Miami"), ("Washington", "Atlanta"), ("Washington", "Montreal"), ("Washington", "New York")])
pandemic.add_edges_from([("London", "New York"), ("London", "Madrid"), ("London", "Paris"), ("London", "Essen")])
pandemic.add_edges_from([("Madrid", "Washington"), ("Madrid", "London"), ("Madrid", "Paris"), ("Madrid", "Algiers"), ("Madrid", "Sao Paulo")])
pandemic.add_edges_from([("Essen", "London"), ("Essen", "Paris"), ("Essen", "Milan"), ("Essen", "St. Petersburg")])
pandemic.add_edges_from([("Paris", "London"), ("Paris", "Madrid"), ("Paris", "Algiers"), ("Paris", "Milan"), ("Paris", "Essen")])
pandemic.add_edges_from([("Milan", "Essen"), ("Milan", "Paris"), ("Milan", "Instanbul")])
pandemic.add_edges_from([("St. Petersburg", "Essen"), ("St. Petersburg", "Istanbul"), ("St. Petersburg", "Moscow")])

pandemic.add_edges_from([("Los Angeles", "Sydney"), ("Los Angeles", "San Fransisco"), ("Los Angeles", "Chicago"), ("Los Angeles", "Mexico City")])
pandemic.add_edges_from([("Mexico City", "Los Angeles"), ("Mexico City", "Chicago"), ("Mexico City", "Miami"), ("Mexico City", "Bogota"), ("Mexico City", "Lima")])
pandemic.add_edges_from([("Miami", "Atlanta"), ("Miami", "Washington"), ("Miami", "Bogota"), ("Miami", "Mexico City")])
pandemic.add_edges_from([("Bogota", "Mexico City"), ("Bogota", "Miami"), ("Bogota", "Sao Paolo"), ("Bogota", "Buenos Aires"), ("Bogota", "Lima")])
pandemic.add_edges_from([("Lima", "Mexico City"), ("Lima", "Bogota"), ("Lima", "Santiago")])
pandemic.add_edges_from([("Santiago", "Lima"), ("Santiago", "Buenos Aires")])
pandemic.add_edges_from([("Buenos Aires", "Santiago"), ("Buenos Aires", "Bogota"), ("Buenos Aires", "Sao Paulo")])
pandemic.add_edges_from([("Sao Paulo", "Bogota"), ("Sao Paulo", "Buenos Aires"), ("Sao Paulo", "Madrid"), ("Sao Paulo", "Lagos")])
pandemic.add_edges_from([("Lagos", "Sao Paulo"), ("Lagos", "Kinshasa"), ("Lagos", "Khartoum")])
pandemic.add_edges_from([("Kinshasa", "Lagos"), ("Kinshasa", "Johanesburg"), ("Kinshasa", "Khartoum")])
pandemic.add_edges_from([("Johanesburg", "Kinshasa"), ("Johanesburg", "Khartoum")])
pandemic.add_edges_from([("Khartoum", "Lagos"), ("Khartoum", "Kinshasa"), ("Khartoum", "Johanesburg"), ("Khartoum", "Cairo")])

