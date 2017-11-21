import networkx as nx

pandemic = nx.Graph()
pandemic.add_nodes_from(["San Fransisco", "Chicago", "Montreal", "New York", "Atlanta", "Washington", "London", "Madrid", "Essen", "Paris", "Milan", "St. Petersburg"], color="blue")
pandemic.add_nodes_from(["Los Angeles", "Mexico City", "Miami", "Bogota", "Lima", "Santiago", "Buenos Aires", "Sao Paulo", "Lagos", "Kinshasa", "Johanesburg", "Khartoum"], color="yellow")
pandemic.add_nodes_from(["Algiers", "Istanbul", "Cairo", "Moscow", "Baghdad", "Riyadh", "Tehran", "Karachi", "Mumbai", "Delhi", "Chennai", "Kolkata"], color="black")
pandemic.add_nodes_from(["Bangkok", "Jakarta", "Beijing", "Shanghai", "Hong Kong", "Ho Chi Minh City", "Seoul", "Taipei", "Manila", "Sydney", "Tokyo", "Osaka"], color="red")

pandemic.add_edges_from([("San Fransisco", "Tokyo"), ("San Fransisco", "Manila"), ("San Fransisco", "Los Angeles"), ("San Fransisco", "Chicago")])
pandemic.add_edges_from([("Chicago", "Montreal"), ("Chicago", "New York"), ("Chicago", "Washington")])
pandemic.add_edges_from([("Montreal", "Washington"), ("Montreal", "Chicago"), ("Montreal", "New York")])
