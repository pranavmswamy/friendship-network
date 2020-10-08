# friendship-network
Social Network Analysis in Python using NetworkX. The networks depict the various properties of a class of 59 students and their connections on social media.

![Image of Friendship Network](https://github.com/pranavmswamy/friendship-network/blob/master/sna_network.png)

## Centrality Measures
In Network Analysis, indicators of Centrality identify the most important vertices within a network. Its applications include:
1. Identifying, for example, the most influential people in a social network,
2. Key infrastructure nodes in urban networks, 
3. Important pages on the web, 
4. Nodes that spread information across the network, 
5. Nodes that can cause/prevent epidemics, and,
6. Nodes that are crucial to keep the network from breaking up.

### Degree Centrality

Degree Centrality assigns an importance score based on the number of ties each actor in the network has:

*“More no. of ties = More important”*

It answers the immediate question – How many people in the network are you directly connected to?

![Image of Degree Centrality](https://github.com/pranavmswamy/friendship-network/blob/master/FacebookNetwork.py)

### Closeness Centrality

Closeness Centrality is a measure of the degree to which an individual is near all other individuals (the number of hops) in a network. It is used for finding the individuals who are best placed to influence the entire network most quickly – good ‘broadcasters’.

*“Close to everyone in the network = More important”*

It answers the immediate question - How close are you to every person in the network?

![Image of Closeness Centrality](https://github.com/pranavmswamy/friendship-network/blob/master/ClosenessCentralityFacebook.png)

### Betweenness Centrality 

Betweenness Centrality is the measure of how many times a particular node comes in between the shortest path between any other two nodes. 

*“People that act as bridges between other people = More important”*

It answers the immediate question - Who is important for the flow of information in a network?

Removal of a node with a high betweenness centrality would result in the disruption of communication across the entire network.

![Image of Betweenness Centrality](https://github.com/pranavmswamy/friendship-network/blob/master/HighBeweennessCentrality.png)



