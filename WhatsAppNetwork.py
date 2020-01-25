# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 12:47:41 2018

@author: Pranav
"""

import networkx as nx
import matplotlib.pyplot as plt


whatsapp_graph = nx.Graph(name = 'whatsapp')

#-----------------------------------------------------------------------------------------------------
#ADDING NODES

whatsapp_graph.add_node('Manoj',sec='A',gen='M')
whatsapp_graph.add_node('Johanna',sec='A',gen='F')
whatsapp_graph.add_node('Ramya',sec='A',gen='F')
whatsapp_graph.add_node('Shalini',sec='A',gen='F')
whatsapp_graph.add_node('Balasubramaniyan',sec='A',gen='M')
whatsapp_graph.add_node('Pooja',sec='A',gen='F')
whatsapp_graph.add_node('Harish',sec='A',gen='M')
whatsapp_graph.add_node('Keerthan',sec='A',gen='M')
whatsapp_graph.add_node('Abdul',sec='A',gen='M')
whatsapp_graph.add_node('Abhishek',sec='A',gen='M')
whatsapp_graph.add_node('Aditya',sec='A',gen='M')
whatsapp_graph.add_node('Ajith',sec='A',gen='M')
whatsapp_graph.add_node('Akash',sec='A',gen='M')
whatsapp_graph.add_node('Amit',sec='A',gen='M')
whatsapp_graph.add_node('Amritha',sec='A',gen='F')
whatsapp_graph.add_node('Amrutha',sec='A',gen='F')
whatsapp_graph.add_node('Arun',sec='A',gen='M')
whatsapp_graph.add_node('Beenu',sec='A',gen='F')
whatsapp_graph.add_node('Bhargava',sec='A',gen='M')
whatsapp_graph.add_node('Bishal',sec='A',gen='M')
whatsapp_graph.add_node('Bhavya',sec='A',gen='F')
whatsapp_graph.add_node('Chandana',sec='A',gen='F')
whatsapp_graph.add_node('Darshan',sec='A',gen='M')
whatsapp_graph.add_node('Sravya',sec='A',gen='F')
whatsapp_graph.add_node('Gokul',sec='A',gen='M')
whatsapp_graph.add_node('Pruthvi',sec='A',gen='F')
whatsapp_graph.add_node('Nidhi',sec='A',gen='F')
whatsapp_graph.add_node('Devaditya',sec='B',gen='M')
whatsapp_graph.add_node('Ashim',sec='B',gen='M')
whatsapp_graph.add_node('Bimal',sec='B',gen='M')
whatsapp_graph.add_node('Ashish',sec='B',gen='M')
whatsapp_graph.add_node('Nissi',sec='B',gen='F')
whatsapp_graph.add_node('Pranav',sec='B',gen='M')
whatsapp_graph.add_node('Prashant',sec='B',gen='M')
whatsapp_graph.add_node('Prathiksha',sec='B',gen='F')
whatsapp_graph.add_node('Raja',sec='B',gen='M')
whatsapp_graph.add_node('Rakshith',sec='B',gen='M')
whatsapp_graph.add_node('Rashmi',sec='B',gen='F')
whatsapp_graph.add_node('Sanjana',sec='B',gen='F')
whatsapp_graph.add_node('Apeksha',sec='C',gen='F')
whatsapp_graph.add_node('Vignesh',sec='C',gen='M')
whatsapp_graph.add_node('Gaurav',sec='C',gen='M')
whatsapp_graph.add_node('Akansha',sec='C',gen='F')
whatsapp_graph.add_node('Santosh',sec='C',gen='M')
whatsapp_graph.add_node('Nitish',sec='C',gen='M')
whatsapp_graph.add_node('Badri',sec='C',gen='M')
whatsapp_graph.add_node('Tejaswini',sec='C',gen='F')
whatsapp_graph.add_node('Purvaj',sec='C',gen='M')
whatsapp_graph.add_node('Rahul',sec='C',gen='M')
whatsapp_graph.add_node('Rohit',sec='C',gen='M')
whatsapp_graph.add_node('Sachin',sec='C',gen='M')
whatsapp_graph.add_node('Aroon',sec='C',gen='M')
whatsapp_graph.add_node('Shimna',sec='C',gen='F')
whatsapp_graph.add_node('Shreyas',sec='C',gen='M')
whatsapp_graph.add_node('Joshua',sec='C',gen='M')
whatsapp_graph.add_node('Soundarya',sec='C',gen='F')
whatsapp_graph.add_node('Sonal',sec='C',gen='F')
whatsapp_graph.add_node('Aishwarya',sec='C',gen='F')
whatsapp_graph.add_node('NGP',sec='All',gen='M')
#------------------------------------------------------------------------------------------------
whatsapp_edge_list = [('Manoj','Ramya'),('Manoj','Shalini'),('Manoj','Harish'),('Manoj','Keerthan'),('Manoj','Bishal'),('Manoj','Gokul'),('Manoj','Nidhi'),('Manoj','Gaurav'),
                      ('Johanna','Ramya'),('Johanna','Ramya'),('Johanna','Shalini'),('Johanna','Pooja'),('Johanna','Beenu'),
                      ('Ramya','Shalini'),('Ramya','Balasubramaniyan'),('Ramya','Pooja'),('Ramya','Beenu'),
                      ('Shalini','Pooja'),('Shalini','Beenu'),
                      ('Pooja','Akash'),('Pooja','Amit'),('Pooja','Beenu'),('Pooja','Nitish'),
                      ('Harish','Keerthan'),('Harish','Abdul'),('Harish','Aditya'),('Harish','Amrutha'),('Harish','Chandana'),('Harish','Sravya'),('Harish','Gokul'),('Harish','Nidhi'),('Harish','Rashmi'),
                      ('Keerthan','Balasubramaniyan'),('Keerthan','Abdul'),('Keerthan','Abhishek'),('Keerthan','Aditya'),('Keerthan','Ajith'),('Keerthan','Akash'),('Keerthan','Amit'),('Keerthan','Amritha'),('Keerthan','Amrutha'),('Keerthan','Arun'),('Keerthan','Beenu'),('Keerthan','Bhargava'),('Keerthan','Bishal'),('Keerthan','Bhavya'),('Keerthan','Chandana'),('Keerthan','Darshan'),('Keerthan','Gokul'),('Keerthan','Pruthvi'),('Keerthan','Nidhi'),('Keerthan','Ashish'),('Keerthan','Prathiksha'),('Keerthan','Rashmi'),
                      ('Abdul','Akash'),('Abdul','Arun'),('Abdul','Gokul'),
                      ('Abhishek','Manoj'),('Abhishek','Balasubramaniyan'),('Abhishek','Abdul'),('Abhishek','Ajith'),('Abhishek','Akash'),('Abhishek','Amit'),('Abhishek','Bhargava'),('Abhishek','Bishal'),('Abhishek','Gokul'),
                      ('Aditya','Abdul'),('Aditya','Ajith'),('Aditya','Amritha'),('Aditya','Amrutha'),('Aditya','Arun'),('Aditya','Beenu'),('Aditya','Bhargava'),('Aditya','Chandana'),('Aditya','Darshan'),('Aditya','Gokul'),('Aditya','Pruthvi'),('Aditya','Nidhi'),('Aditya','Prathiksha'),('Aditya','Rashmi'),
                      ('Ajith','Arun'),('Ajith','Bhargava'),('Ajith','Darshan'),('Ajith','Gokul'),('Ajith','Pruthvi'),('Ajith','Gaurav'),('Ajith','Shreyas'),
                      ('Amit','Manoj'),('Amit','Bishal'),('Amit','Bhavya'),('Amit','Sravya'),
                      ('Amritha','Amit'),('Amritha','Amrutha'),('Amritha','Beenu'),('Amritha','Bhargava'),('Amritha','Bhavya'),('Amritha','Chandana'),('Amritha','Gokul'),('Amritha','Pruthvi'),('Amritha','Nidhi'),('Amritha','Sanjana'),
                      ('Amrutha','Abdul'),
                      ('Arun','Manoj'),('Arun','Balasubramaniyan'),('Arun','Harish'),('Arun','Akash'),('Arun','Bhargava'),('Arun','Bishal'),('Arun','Darshan'),('Arun','Gokul'),('Arun','Rohit'),('Arun','Sachin'),
                      ('Beenu','Harish'),('Beenu','Amrutha'),('Beenu','Chandana'),('Beenu','Sravya'),('Beenu','Pruthvi'),('Beenu','Nidhi'),('Beenu','Nissi'),('Beenu','Shimna'),
                      ('Bhargava','Manoj'),('Bhargava','Johanna'),('Bhargava','Balasubramaniyan'),('Bhargava','Harish'),('Bhargava','Abdul'),('Bhargava','Akash'),('Bhargava','Amit'),('Bhargava','Amrutha'),('Bhargava','Chandana'),('Bhargava','Darshan'),('Bhargava','Sravya'),('Bhargava','Gokul'),('Bhargava','Pruthvi'),('Bhargava','Badri'),('Bhargava','Purvaj'),('Bhargava','Rahul'),('Bhargava','Rohit'),('Bhargava','Sachin'),('Bhargava','Shreyas'),
                      ('Bishal','Harish'),('Bishal','Darshan'),('Bishal','Gokul'),('Bishal','Ashim'),('Bishal','Bimal'),
                      ('Bhavya','Amrutha'),('Bhavya','Beenu'),('Bhavya','Chandana'),('Bhavya','Sravya'),('Bhavya','Gokul'),('Bhavya','Pruthvi'),('Bhavya','Nidhi'),
                      ('Chandana','Manoj'),('Chandana','Johanna'),('Chandana','Ramya'),('Chandana','Shalini'),('Chandana','Pooja'),('Chandana','Abdul'),('Chandana','Amit'),('Chandana','Amrutha'),('Chandana','Arun'),('Chandana','Bishal'),('Chandana','Darshan'),('Chandana','Sravya'),('Chandana','Gokul'),('Chandana','Pruthvi'),('Chandana','Nidhi'),('Chandana','Pranav'),('Chandana','Sanjana'),('Chandana','Rohit'),('Chandana','NGP'),
                      ('Darshan','Balasubramaniyan'),('Darshan','Gokul'),
                      ('Sravya','Akash'),('Sravya','Amritha'),('Sravya','Arun'),('Sravya','Bishal'),('Sravya','Chandana'),('Sravya','Gokul'),('Sravya','Pruthvi'),('Sravya','Nidhi'),('Sravya','Tejaswini'),('Sravya','Soundarya'),('Sravya','Sonal'),
                      ('Gokul','Johanna'),('Gokul','Balasubramaniyan'),('Gokul','Akash'),('Gokul','Pruthvi'),('Gokul','Nidhi'),('Gokul','Nissi'),('Gokul','Sanjana'),('Gokul','Badri'),('Gokul','Sonal'),('Gokul','NGP'),
                      ('Pruthvi','Harish'),('Pruthvi','Amrutha'),('Pruthvi','Nidhi'),('Pruthvi','Rashmi'),
                      ('Nidhi','Amrutha'),('Nidhi','Nissi'),('Nidhi','Pranav'),('Nidhi','Prathiksha'),('Nidhi','Rashmi'),('Nidhi','NGP'),
                      ('Ashim','Bishal'),('Ashim','Bimal'),('Ashim','Prashant'),
                      ('Devaditya','Ashim'),('Devaditya','Prashant'),
                      ('Bimal','Prashant'),
                      ('Ashish','Harish'),('Ashish','Gokul'),('Ashish','Ashim'),('Ashish','Bimal'),('Ashish','Prashant'),('Ashish','Raja'),('Ashish','Rakshith'),('Ashish','Badri'),('Ashish','Purvaj'),('Ashish','Rahul'),('Ashish','Rohit'),
                      ('Nissi','Pranav'),('Nissi','Prashant'),('Nissi','Prathiksha'),('Nissi','Rashmi'),('Nissi','Sanjana'),('Nissi','Rakshith'),('Nissi','NGP'),
                      ('Pranav','Amrutha'),('Pranav','Chandana'),('Pranav','Prashant'),('Pranav','Prathiksha'),('Pranav','Sanjana'),('Pranav','Rohit'),('Pranav','Sachin'),('Pranav','Soundarya'),('Pranav','NGP'),
                      ('Prashant','Nidhi'),('Prashant','Prathiksha'),('Prashant','Rakshith'),('Prashant','Rashmi'),('Prashant','Rohit'),('Prashant','Sachin'),('Prashant','Sonal'),('Prashant','NGP'),
                      ('Prathiksha','Chandana'),('Prathiksha','Rashmi'),('Prathiksha','Sanjana'),
                      ('Raja','Arun'),('Raja','Aroon'),('Raja','Joshua'),
                      ('Rakshith','Keerthan'),('Rakshith','Arun'),('Rakshith','Ashish'),('Rakshith','Prashant'),('Rakshith','Prathiksha'),('Rakshith','Rashmi'),
                      ('Rashmi','Amrutha'),('Rashmi','Rakshith'),('Rashmi','Sanjana'),
                      ('Apeksha','Vignesh'),('Apeksha','Gaurav'),('Apeksha','Akansha'),('Apeksha','Tejaswini'),('Apeksha','Rohit'),
                      ('Akansha','Santosh'),('Akansha','Nitish'),('Akansha','Tejaswini'),('Akansha','Rohit'),('Akansha','Soundarya'),
                      ('Santosh','Nitish'),('Santosh','Rohit'),('Santosh','Aroon'),('Santosh','Joshua'),
                      ('Nitish','Balasubramaniyan'),
                      ('Tejaswini','Sonal'),
                      ('Rahul','Ajith'),('Rahul','Arun'),('Rahul','Beenu'),('Rahul','Vignesh'),('Rahul','Gaurav'),('Rahul','Badri'),('Rahul','Purvaj'),('Rahul','Rohit'),('Rahul','Shreyas'),('Rahul','NGP'),
                      ('Aishwarya','Amrutha'),('Aishwarya','Apeksha'),('Aishwarya','Gaurav'),('Aishwarya','Rohit'),('Aishwarya','Sachin'),('Aishwarya','Aroon'),('Aishwarya','Shimna'),('Aishwarya','Soundarya'),('Aishwarya','Sonal'),('Aishwarya','NGP'),
                      ('Rohit','Balasubramaniyan'),('Rohit','Keerthan'),('Rohit','Gokul'),('Rohit','Nidhi'),('Rohit','Vignesh'),('Rohit','Gaurav'),('Rohit','Nitish'),('Rohit','Badri'),('Rohit','Tejaswini'),('Rohit','Purvaj'),('Rohit','Sachin'),('Rohit','Aroon'),('Rohit','Shimna'),('Rohit','Shreyas'),('Rohit','Joshua'),('Rohit','Soundarya'),('Rohit','Sonal'),('Rohit','NGP'),
                      ('Sachin','Apeksha'),('Sachin','Vignesh'),('Sachin','Gaurav'),('Sachin','Akansha'),('Sachin','Nitish'),('Sachin','Badri'),('Sachin','Tejaswini'),('Sachin','Purvaj'),('Sachin','Rahul'),('Sachin','Aroon'),('Sachin','Shimna'),('Sachin','Shreyas'),('Sachin','Joshua'),('Sachin','Soundarya'),('Sachin','Sonal'),('Sachin','NGP'),
                      ('Shimna','Akansha'),('Shimna','Tejaswini'),('Shimna','Purvaj'),('Shimna','Rahul'),('Shimna','Aroon'),('Shimna','Shreyas'),('Shimna','Soundarya'),('Shimna','Sonal'),('Shimna','NGP'),
                      ('Sonal','Soundarya'),('Sonal','Apeksha'),('Sonal','Akansha'),('Sonal','Nitish'),
                      ('Soundarya','Apeksha'),('Soundarya','Vignesh'),('Soundarya','Tejaswini'),('Soundarya','Aroon'),('Soundarya','NGP')]


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
whatsapp_graph.add_edges_from(whatsapp_edge_list)
#---------------------------------------------------------------------------------------------------------------------------
nodesizelist = [75*whatsapp_graph.degree(node) for node in whatsapp_graph]
nodecolorlist = []
nodecolorlist2 = [whatsapp_graph.degree(student) for student in whatsapp_graph]
for person in whatsapp_graph:
    if whatsapp_graph.node[person]['sec'] == 'A':
        nodecolorlist.append('#36688D')
    elif whatsapp_graph.node[person]['sec'] == 'B':
        nodecolorlist.append('#66CC00');
    elif whatsapp_graph.node[person]['sec'] == 'C':
        nodecolorlist.append('#F3CD05')
    else:
        nodecolorlist.append('c')
                
#pos = nx.spring_layout(whatsapp_graph,k=1,iterations=150)
pos = nx.spring_layout(whatsapp_graph)
plt.figure(figsize=(20,12.6))
nx.draw_networkx(whatsapp_graph,pos,node_color = nodecolorlist, node_size = nodesizelist,edge_color='0.7')
plt.savefig('whatsapp_graph0.5_spring.pdf',format='pdf')
#nx.draw_networkx(whatsapp_graph,pos,node_color = nodecolorlist2, node_size = nodesizelist,cmap = plt.cm.Reds)

pos=nx.circular_layout(whatsapp_graph)
plt.figure(figsize=(20,20))
nx.draw_networkx(whatsapp_graph,pos,node_color = nodecolorlist, node_size = nodesizelist,edge_color='0.7')
plt.savefig('whatsapp_graph0.4_circular.pdf',format='pdf')
#-------------------------------------------------------------------------------------------------
#for male-female bipartite:
from networkx.algorithms import bipartite
B = nx.Graph()
nodecolorlistb = []
for (u,v) in whatsapp_edge_list:
    if whatsapp_graph.node[u]['gen'] == 'M' and whatsapp_graph.node[u]['gen'] != whatsapp_graph.node[v]['gen']:
        B.add_node(u,gen = 'M')
        

for (u,v) in whatsapp_edge_list:
    if whatsapp_graph.node[v]['gen'] == 'M' and whatsapp_graph.node[u]['gen'] != whatsapp_graph.node[v]['gen']:
        B.add_node(v,gen = 'M')

for (u,v) in whatsapp_edge_list:
    if whatsapp_graph.node[u]['gen'] == 'F' and whatsapp_graph.node[u]['gen'] != whatsapp_graph.node[v]['gen']:
        B.add_node(u,gen = 'F')
    
for (u,v) in whatsapp_edge_list:
    if whatsapp_graph.node[v]['gen'] == 'F' and whatsapp_graph.node[u]['gen'] != whatsapp_graph.node[v]['gen']:
        B.add_node(v,gen = 'F')

for (u,v) in whatsapp_edge_list:
    if whatsapp_graph.node[u]['gen'] != whatsapp_graph.node[v]['gen']:
        B.add_edge(u,v)
for person in B:
    if whatsapp_graph.node[person]['gen'] == 'M':
        nodecolorlistb.append('#6495ED')
    else:
        nodecolorlistb.append('#F3CD05')
nodesizelistbip = [100*B.degree(node) for node in B]
plt.figure(figsize=(12,12))  
pos = nx.circular_layout(B)     
nx.draw_networkx(B,pos,node_color = nodecolorlistb,edge_color = '0.4',node_size = nodesizelistbip)
plt.savefig('whatsappbipcirc.pdf',format='pdf')

X, Y = bipartite.sets(B)
pos = dict()
pos.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
plt.figure(figsize=(15,25)) 
plt.title('Bipartite Boys-Girls Graph')
nx.draw_networkx(B, pos=pos,node_color = nodecolorlistb,edge_color = '0.4', node_size = nodesizelistbip)
plt.savefig('whatsappbipst.pdf',format='pdf')
            
nx.degree(B)
#---------------------------------------------------------------------------
#Projected Graph for BOYS (common female friends)

x = set([node for node in B if B.node[node]['gen'] == 'M'])
#y = set([node for node in B if B.node[node]['gen'] == 'F']) - if you want to ddo it for girls - common male friends

Pboys = bipartite.weighted_projected_graph(B,x)
edge_width =[1*Pboys[u][v]['weight'] for u,v in Pboys.edges()]
labels_greater_than_5 = {edge:weight for edge,weight in nx.get_edge_attributes(Pboys,'weight').items() if weight >5}
plt.figure(figsize=(8,8))
plt.title('Common Female Friends')
pos = nx.circular_layout(Pboys)
nx.draw_networkx(Pboys,pos,edge_color = '0.4',width=edge_width,node_color='#6495ED',node_size=400)
nx.draw_networkx_edge_labels(Pboys,pos,edge_labels = labels_greater_than_5)
plt.savefig('whatsappcommonfemfrds.pdf',format='pdf')

edgelist_grt_than_5 = [x for x in Pboys.edges(data=True) if x[2]['weight'] > 5]
edge_widthblue =[3*x[2]['weight'] for x in Pboys.edges(data=True)]
edge_width =[x[2]['weight'] for x in Pboys.edges(data=True)]
plt.figure(figsize=(8,8))
plt.title('Common Female Friends - >5')
pos=nx.circular_layout(Pboys)
nx.draw_networkx(Pboys,pos,edge_color = '0.7',width=edge_width,node_color='#6495ED',node_size=400)
nx.draw_networkx_edges(Pboys,pos,edgelist = edgelist_grt_than_5,edge_color = 'blue',width=edge_widthblue)
nx.draw_networkx_edge_labels(Pboys,pos,edge_labels = labels_greater_than_5)
plt.savefig('whatsappcommonfemfrdsg5.pdf',format='pdf')

#Make it better by adding weights to the edges, and changing edge size accordingly. - use weighted_projected_graph(B,x) and print P.edges(data = True)
#------------------------------------------------------------------------------------------
#Projected Graph for GIRLS (common male friends)
y = set([node for node in B if B.node[node]['gen'] == 'F'])

Pgirls = bipartite.weighted_projected_graph(B,y)
edge_width =[1*Pgirls[u][v]['weight'] for u,v in Pgirls.edges()]
labels_greater_than_5 = {edge:weight for edge,weight in nx.get_edge_attributes(Pgirls,'weight').items() if weight >5}
plt.figure(figsize=(9,9))
plt.title('Common Male Friends')
pos = nx.circular_layout(Pgirls)
nx.draw_networkx(Pgirls,pos,edge_color = '0.4',width=edge_width,node_color='#D2691E',node_size=300)
nx.draw_networkx_edge_labels(Pgirls,pos,edge_labels = labels_greater_than_5)
plt.savefig('whatsappcommonmalfrds.pdf',format='pdf')

edgelist_grt_than_5 = [x for x in Pgirls.edges(data=True) if x[2]['weight'] > 5]

plt.figure(figsize=(9,9))
plt.title('Common Male Friends - >5')
edge_width =[x[2]['weight'] for x in Pgirls.edges(data=True)]
edge_widthyellow = [1.5*x[2]['weight'] for x in Pgirls.edges(data=True) if x[2]['weight'] > 5]
nx.draw_networkx(Pgirls,pos,edge_color = '0.7',width=edge_width,node_color='#D2691E',node_size=300)
nx.draw_networkx_edges(Pgirls,pos,edgelist = edgelist_grt_than_5,edge_color = '#FFA500',width=edge_widthyellow)
nx.draw_networkx_edge_labels(Pgirls,pos,edge_labels = labels_greater_than_5)
plt.savefig('whatsappcommonmalfrdsg5.pdf',format='pdf')

#-------------------------------------------------------------------------------------------
#whatsapp_graph coloured according to gender
'''nodesizelist = [100*whatsapp_graph.degree(node) for node in whatsapp_graph]
nodecolorlistg = []
#nodecolorlist2 = [whatsapp_graph.degree(student) for student in whatsapp_graph]

for person in whatsapp_graph:
    if whatsapp_graph.node[person]['gen'] == 'M':
        nodecolorlistg.append('#36688D')
    elif whatsapp_graph.node[person]['gen'] == 'F':
        nodecolorlistg.append('#BDA589');
    else:
        nodecolorlistg.append('c')
                
#pos = nx.spring_layout(whatsapp_graph,k=1,iterations=150)
pos = nx.spring_layout(whatsapp_graph)
plt.figure(figsize=(20,20))
nx.draw_networkx(whatsapp_graph,pos,node_color = nodecolorlistg, node_size = nodesizelist,edge_color='0.5')
'''
#------------------------------------------------------------------------------------------
#Boy-Boy Friendship graph
b2b = nx.Graph()
for (u,v) in whatsapp_edge_list:
    if whatsapp_graph.node[u]['gen'] == 'M' and whatsapp_graph.node[v]['gen'] == 'M':
        b2b.add_edge(u,v)

b2bnodeclrlist = []
b2bnodesizelist = [2000*nx.degree_centrality(whatsapp_graph)[node] for node in b2b]
b2bnodecolorlist2 = [1000*nx.closeness_centrality(whatsapp_graph)[node] for node in b2b]
for person in b2b:
    if whatsapp_graph.node[person]['sec'] == 'A':
        b2bnodeclrlist.append('#36688D')
    elif whatsapp_graph.node[person]['sec'] == 'B':
        b2bnodeclrlist.append('#BDA589')
    elif whatsapp_graph.node[person]['sec'] == 'C':
        b2bnodeclrlist.append('#F3CD05')
    else:
        b2bnodeclrlist.append('c')

pos = nx.spring_layout(b2b)
plt.figure(figsize=(19.8,10.2))
plt.title('Male- Male Friendships')
nx.draw_networkx(b2b,pos,edge_color='0.7',node_size=b2bnodesizelist,node_color = b2bnodeclrlist)
plt.savefig('whatsappb2b.pdf',format='pdf')
plt.figure(figsize=(16,9))
nx.draw_networkx(b2b,pos,edge_color='0.5',node_size=b2bnodesizelist,node_color = b2bnodecolorlist2,cmap='YlOrBr')


#--------------------------------------------------------------------------------------------
#Girl-Girl Friendship

'''for (u,v) in whatsapp_edge_list:
    if whatsapp_graph.node[u]['gen'] == 'F' and whatsapp_graph.node[u]['sec'] == 'A':
        b2b.add_node(u,gen = 'F',sec='A')
    elif whatsapp_graph.node[u]['gen'] == 'F' and whatsapp_graph.node[u]['sec'] == 'B':
        b2b.add_node(u,gen = 'F',sec='B')
    elif whatsapp_graph.node[u]['gen'] == 'F' and whatsapp_graph.node[u]['sec'] == 'C':
        b2b.add_node(u,gen = 'F',sec='C')
    else:
        b2b.add_node(u,gen = 'F', sec = 'All')
        
for (u,v) in whatsapp_edge_list:
    if whatsapp_graph.node[v]['gen'] == 'F' and whatsapp_graph.node[v]['sec'] == 'A':
        b2b.add_node(v,gen = 'F',sec='A')
    elif whatsapp_graph.node[u]['gen'] == 'F' and whatsapp_graph.node[v]['sec'] == 'B':
        b2b.add_node(v,gen = 'F',sec='B')
    elif whatsapp_graph.node[v]['gen'] == 'F' and whatsapp_graph.node[v]['sec'] == 'C':
        b2b.add_node(v,gen = 'F',sec='C')
    else:
        b2b.add_node(v,gen = 'F', sec = 'All')'''
        
g2g = nx.Graph()
for (u,v) in whatsapp_edge_list:
    if whatsapp_graph.node[u]['gen'] == 'F' and whatsapp_graph.node[v]['gen'] == 'F':
        g2g.add_edge(u,v)

g2gnodeclrlist = []
for person in g2g:
    if whatsapp_graph.node[person]['sec'] == 'A':
        g2gnodeclrlist.append('#36688D')
    elif whatsapp_graph.node[person]['sec'] == 'B':
        g2gnodeclrlist.append('#BDA589')
    elif whatsapp_graph.node[person]['sec'] == 'C':
        g2gnodeclrlist.append('#F3CD05')
    else:
        g2gnodeclrlist.append('c')
        
pos = nx.spring_layout(g2g)
plt.figure(figsize=(16,12))
plt.title('Female-Female Friendships')
nx.draw_networkx(g2g,pos,edge_color='0.5',node_color = g2gnodeclrlist)
plt.savefig('whatsappg2g.pdf',format='pdf')
#---------------------------------------------------------------------------------------------
bfs_t = nx.bfs_tree(whatsapp_graph,'Rohit')
bfsnodecolorlist = []
pos = nx.shell_layout(bfs_t)
#nx.draw(G, pos, with_labels=False, arrows=True)
plt.figure(figsize=(15,15));

for person in bfs_t:
    if nx.shortest_path_length(bfs_t,'Rohit',person) == 1:
        bfsnodecolorlist.append('#00FF7F')
    elif nx.shortest_path_length(bfs_t,'Rohit',person) == 2:
        bfsnodecolorlist.append('#FFA500')
    elif nx.shortest_path_length(bfs_t,'Rohit',person) == 3:
        bfsnodecolorlist.append('#00CED1')
    else:
        bfsnodecolorlist.append('r')
    
    

'''for person in bfs_t:
    if fb_graph.has_edge(person,'Keerthan'):
        bfsnodecolorlist.append('r')
    else:
        bfsnodecolorlist.append('c')'''
nx.draw_networkx(bfs_t,pos,node_color = bfsnodecolorlist,with_labels=False)
plt.savefig('shrtestpathmore.pdf',format='pdf')
#shows bfs tree with starting node Pranav. Very interesting Tree structure.
#---------------------------------------------------------------------------------
#dfs-tree
#plt.figure(figsize=(18,18)) 
#nx.draw_networkx(nx.dfs_tree(whatsapp_graph,'Pranav'))

'''disc = nx.Graph()
disc.add_edges_from(whatsapp_edge_list)
disc.remove_edges_from([('Pranav', 'Amrutha'),
 ('Pranav', 'Chandana'),
 ('Pranav', 'NGP'),
 ('Pranav', 'Nidhi'),
 ('Pranav', 'Nissi'),
 ('Pranav', 'Prashant'),
 ('Pranav', 'Prathiksha'),
 ('Pranav', 'Rohit'),
 ('Pranav', 'Sachin'),
 ('Pranav', 'Sanjana'),
 ('Pranav', 'Soundarya')])
plt.figure(figsize=(15,15));
pos = nx.spring_layout(disc)
nx.draw_networkx(disc,pos,node_conlor = nodecolorlist) '''
#---------------------------------------------------------------------------------
#Given 2 friends, connect them by seeing how many mutual friends they have
mfg = nx.Graph()
#MORE THAN 8 MUTUAL FRIENDS.
for u in whatsapp_graph.nodes:
    for v in whatsapp_graph.nodes:
        if mfg.has_edge(u,v) or u==v:
            continue
        else:
            cn = []
            for i in nx.common_neighbors(whatsapp_graph,u,v):
                cn.append(i)
            if len(cn) > 9:
                mfg.add_edge(u,v,MF=len(cn))

nodecolorlist = []
for person in mfg:
    if whatsapp_graph.node[person]['sec'] == 'A':
        nodecolorlist.append('#36688D')
    elif whatsapp_graph.node[person]['sec'] == 'B':
        nodecolorlist.append('#66CC00');
    elif whatsapp_graph.node[person]['sec'] == 'C':
        nodecolorlist.append('#F3CD05')
    else:
        nodecolorlist.append('c')

plt.figure(figsize=(19.2,10.8))
nx.draw_networkx(mfg,node_size=200,node_color = nodecolorlist,cmap='coolwarm',edge_color='0.5')
plt.savefig('whatsappmfg.pdf',format='pdf')
#---------------------------------------------------------------------------------
#MUTUAL FRIENDS, NOT CONNECTED. - POTENTIAL FRIENDS
mfgnc = nx.Graph()
#MORE THAN 8 MF, NOT CONNECTED
for u in whatsapp_graph.nodes:
    for v in whatsapp_graph.nodes:
        if mfgnc.has_edge(u,v) or u==v:
            continue
        else:
            cn = []
            for i in nx.common_neighbors(whatsapp_graph,u,v):
                cn.append(i)
            if len(cn) > 8 and not(whatsapp_graph.has_edge(u,v)):
                mfgnc.add_edge(u,v,MF=len(cn))    
                
nodecolorlist = []
for person in mfgnc:
    if whatsapp_graph.node[person]['sec'] == 'A':
        nodecolorlist.append('#36688D')
    elif whatsapp_graph.node[person]['sec'] == 'B':
        nodecolorlist.append('#66CC00');
    elif whatsapp_graph.node[person]['sec'] == 'C':
        nodecolorlist.append('#F3CD05')
    else:
        nodecolorlist.append('c')

plt.figure(figsize=(19.2,10.8))
nx.draw_networkx(mfgnc,node_size=200,node_color = nodecolorlist,cmap='coolwarm',edge_color='0.5')
plt.savefig('whatsappmfgnc.pdf',format='pdf')

#---------------------------------------------------------------------------------
#Degree Centrality
                
degcentgraph = nx.Graph(whatsapp_graph)

nodesizelistdeg = [100*whatsapp_graph.degree(node) for node in whatsapp_graph]
nodecolorlist2 = [whatsapp_graph.degree(student) for student in whatsapp_graph]
pos = nx.spring_layout(whatsapp_graph)
plt.figure(figsize=(19.2,10.8))
nx.draw_networkx(degcentgraph,node_size=nodesizelistdeg,node_color = nodecolorlist2,cmap='coolwarm',edge_color='0.7')
plt.figure(figsize=(20,12.6))
nx.draw_networkx(degcentgraph,node_size=nodesizelistdeg,node_color = nodecolorlist2,cmap='RdYlBu',edge_color = '0.7',with_labels=False)
plt.savefig('degcentgraphnolbls.pdf',format='pdf')

'''Colormap values:
    Possible values are: Accent, Accent_r, Blues, Blues_r, 
    BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2,
    Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, 
    OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1,
    Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r,
    PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r,
    RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, 
    Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, 
    Vega10, Vega10_r, Vega20, Vega20_r, Vega20b, Vega20b_r, Vega20c, Vega20c_r,
    Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd,
    YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r,
    brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, 
    cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r,
    gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, 
    gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, 
    gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, 
    magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma,
    plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, spectral_r, 
    spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, 
    tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r
    
    https://matplotlib.org/tutorials/colors/colormaps.html
    
    '''
#-------------------------------------------------------------------------------------------------
#Closeness Centrality
nodesizelistclo = [1500*nx.closeness_centrality(whatsapp_graph,node) for node in whatsapp_graph]
nodecolorlistclo = [nx.closeness_centrality(whatsapp_graph,student) for student in whatsapp_graph]

#pos = nx.spring_layout(whatsapp_graph,k=1,iterations=150)
pos = nx.spring_layout(whatsapp_graph)
plt.figure(figsize=(20,12.6))
nx.draw_networkx(whatsapp_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='RdYlGn',edge_color='0.7',with_labels=False)
plt.savefig('whatsappcc.pdf',format='pdf')
#nx.draw_networkx(whatsapp_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='RdYlBu')

import operator
sorted(nx.closeness_centrality(whatsapp_graph).items(),key=operator.itemgetter(1),reverse=True)

#----------------------------------------------------------------------------------
#Betweenness Centrality

nodesizelistbet = [25000*nx.betweenness_centrality(whatsapp_graph)[node] for node in whatsapp_graph]
nodecolorlistbet = [nx.betweenness_centrality(whatsapp_graph)[student] for student in whatsapp_graph]
pos = nx.spring_layout(whatsapp_graph)
#plt.figure(figsize=(20,20))
#nx.draw_networkx(whatsapp_graph,node_size=nodesizelistbet,node_color = nodecolorlistbet,cmap='coolwarm')
plt.figure(figsize=(20,12.6))
nx.draw_networkx(whatsapp_graph,node_size=nodesizelistbet,node_color = nodecolorlistbet,cmap='YlOrBr',edge_color='0.68',with_labels=False )
plt.savefig('whatsappbtwcent.pdf',format='pdf')
#----------------------------------------------------------------------------------
#Edge-betweenness centrality

edgesizelistbete = [200*nx.edge_betweenness_centrality(whatsapp_graph)[(u,v)] for u,v in nx.edge_betweenness_centrality(whatsapp_graph).keys()]
#nodecolorlistbete = [nx.betweenness_centrality(whatsapp_graph)[node] for node in whatsapp_graph]
edgecolorlistbete = [nx.edge_betweenness_centrality(whatsapp_graph)[(u,v)] for u,v in nx.edge_betweenness_centrality(whatsapp_graph).keys()]
pos = nx.spring_layout(whatsapp_graph,k=1,iterations=150)
#pos = nx.spring_layout(whatsapp_graph)
plt.figure(figsize=(20,20))
nx.draw_networkx(whatsapp_graph,pos,edge_color = edgecolorlistbete,width=edgesizelistbete,node_size=500,node_color = '#BDA589')
#nx.draw_networkx_edges(Pgirls,pos,edgelist = edgelist_grt_than_5,edge_color = 'green',width=edge_width)
#nx.draw_networkx_edge_labels(Pgirls,pos,edge_labels = labels_greater_than_5)
#plt.figure(figsize=(20,20))
#nx.draw_networkx(whatsapp_graph,node_size=20,node_color = nodecolorlistbete,cmap='coolwarm')

#nx.draw_networkx(whatsapp_graph,node_size=20,node_color = nodecolorlistbete,cmap='YlOrBr',edge)




#------------------------------------------------------------------------------------
#CLIQUES


clqlist = []
clqlist = list(nx.find_cliques(whatsapp_graph))
for i in range(len(clqlist)):
    if len(clqlist[i]) > 7:
        print(clqlist[i])
#show how a clique looks like- just some random 6 node example, and then show the graph's cliques
c = nx.subgraph(whatsapp_graph,['Beenu', 'Nidhi', 'Amrutha', 
                                'Keerthan', 'Chandana', 'Pruthvi',
                                'Bhavya', 'Amritha'])
#highlight those nodes and edges in the graph.    

clqgraph = nx.Graph(whatsapp_graph)
'''clqgraph.node['Amrutha']['clq1'] = 1
clqgraph.node['Chandana']['clq1'] = 1
clqgraph.node['Keerthan']['clq1'] = 1
clqgraph.node['Aditya']['clq1'] = 1
clqgraph.node['Amritha']['clq1'] = 1
clqgraph.node['Pruthvi']['clq1'] = 1
clqgraph.node['Nidhi']['clq1'] = 1
clqgraph.node['Beenu']['clq1'] = 1

clqgraph.node['Harish']['clq2'] = 1
clqgraph.node['Amrutha']['clq2'] = 1
clqgraph.node['Chandana']['clq2'] = 1
clqgraph.node['Keerthan']['clq2'] = 1
clqgraph.node['Aditya']['clq2'] = 1
clqgraph.node['Pruthvi']['clq2'] = 1
clqgraph.node['Nidhi']['clq2'] = 1
clqgraph.node['Beenu']['clq2'] = 1

clqgraph.node['Amrutha']['clq3'] = 1
clqgraph.node['Chandana']['clq3'] = 1
clqgraph.node['Keerthan']['clq3'] = 1
clqgraph.node['Amritha']['clq3'] = 1
clqgraph.node['Pruthvi']['clq3'] = 1
clqgraph.node['Nidhi']['clq3'] = 1
clqgraph.node['Beenu']['clq3'] = 1
clqgraph.node['Bhavya']['clq3'] = 1

clqgraph.node['Chandana']['clq4'] = 1
clqgraph.node['Keerthan']['clq4'] = 1
clqgraph.node['Aditya']['clq4'] = 1
clqgraph.node['Harish']['clq4'] = 1
clqgraph.node['Abdul']['clq4'] = 1
clqgraph.node['Bhargava']['clq4'] = 1
clqgraph.node['Gokul']['clq4'] = 1
clqgraph.node['Arun']['clq4'] = 1'''

edgeclrlist = []
clq1colorlist = []
clq2colorlist = []
for node in clqgraph:
    if node in ['Amrutha', 'Chandana', 'Keerthan', 'Aditya', 'Amritha', 'Pruthvi', 'Nidhi', 'Beenu']:
        clq1colorlist.append('r')
    else:
        clq1colorlist.append('#DCDCDC')
        
for u,v in clqgraph.edges():
    if u in ['Amrutha', 'Chandana', 'Keerthan', 'Aditya', 'Amritha', 'Pruthvi', 'Nidhi', 'Beenu'] and v in['Amrutha', 'Chandana', 'Keerthan', 'Aditya', 'Amritha', 'Pruthvi', 'Nidhi', 'Beenu']:
        edgeclrlist.append('#800000')
    else:
        edgeclrlist.append('0.85')
'''elif node in ['Amrutha', 'Chandana', 'Keerthan', 'Aditya', 'Harish', 'Pruthvi', 'Nidhi', 'Beenu']:
        clqcolorlist.append('c')
    elif node in ['Amrutha', 'Chandana', 'Keerthan', 'Bhavya', 'Pruthvi', 'Nidhi', 'Beenu', 'Amritha']:
        clqcolorlist.append('g')
    elif node in ['Abdul', 'Bhargava', 'Gokul', 'Keerthan', 'Arun', 'Aditya', 'Chandana', 'Harish']:
        clqcolorlist.append('y')''' 

plt.figure(figsize=(20,15))        
pos=nx.spring_layout(clqgraph)
nx.draw_networkx_edges(clqgraph,pos, edge_color = edgeclrlist)      
nx.draw_networkx_nodes(clqgraph,pos,node_size = 300,node_color = clq1colorlist)
nx.draw_networkx_labels(clqgraph,pos)
plt.savefig('whatsappclq1.pdf',format='pdf')

for node in clqgraph:
    if node in ['Abdul', 'Bhargava', 'Gokul', 'Keerthan', 'Arun', 'Aditya', 'Chandana', 'Harish']:
        clq2colorlist.append('c')
    else:
        clq2colorlist.append('#DCDCDC')

edgeclrlist = []
for u,v in clqgraph.edges():
    if u in ['Abdul', 'Bhargava', 'Gokul', 'Keerthan', 'Arun', 'Aditya', 'Chandana', 'Harish'] and v in ['Abdul', 'Bhargava', 'Gokul', 'Keerthan', 'Arun', 'Aditya', 'Chandana', 'Harish']:
        edgeclrlist.append('red')
    else:
        edgeclrlist.append('0.85')

plt.figure(figsize=(20,15))
pos=nx.spring_layout(clqgraph)
nx.draw_networkx_edges(clqgraph,pos, edge_color = edgeclrlist)      
nx.draw_networkx_nodes(clqgraph,pos,node_size = 300,node_color = clq2colorlist)
nx.draw_networkx_labels(clqgraph,pos)
plt.savefig('whatsappclq2.pdf',format='pdf')
#-------------------------------------------------------------------------------------


#PERIPHERAL NODES
peric = nx.Graph(whatsapp_graph)
edgeclrlist = []
clq1colorlist = []
clq2colorlist = []
for node in peric:
    if node in nx.periphery(peric):
        clq1colorlist.append('#7FFF00')
    elif node in nx.center(peric):
        clq1colorlist.append('#CD5C5C')
    else:
        clq1colorlist.append('#DCDCDC')

plt.figure(figsize=(20,12.6))        
pos=nx.spring_layout(peric,k=0.5)
nx.draw_networkx_edges(peric,pos, edge_color = '0.8')      
nx.draw_networkx_nodes(peric,pos,node_size = 1000,node_color = clq1colorlist)
nx.draw_networkx_labels(peric,pos)
plt.savefig('pericenter.pdf',format='pdf')




#------------------------------------------
#Degree distribution graph
   
#import seaborn as sns
import collections
deg_dict = dict(whatsapp_graph.degree)

degree_sequence = sorted([d for n, d in whatsapp_graph.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.35, color='Green')

plt.title("Degree Histogram")
plt.ylabel("Number of People")
plt.xlabel("Number of Friends")
ax.set_xticks([d + 0.5 for d in deg])
ax.set_xticklabels(deg)
# draw graph in inset
plt.axes([0.4, 0.4, 0.5, 0.5])
Gcc = sorted(nx.connected_component_subgraphs(whatsapp_graph), key=len, reverse=True)[0]
pos = nx.spring_layout(whatsapp_graph)
plt.axis('off')
nx.draw_networkx_nodes(whatsapp_graph, pos, node_size=20,node_color='#808000')
nx.draw_networkx_edges(whatsapp_graph, pos, alpha=0.4,edge_color='0.5')
#plt.show()
plt.savefig('ddg-whatsapp0.1.pdf',format='pdf')

#----------------------------------------------------------------------------------
#VARYING CENTRALITY GRAPhs - nodesize = DEG CEN, nodecolor = CLO cen

nodesizelistclo = [80*whatsapp_graph.degree(node) for node in whatsapp_graph]
nodecolorlistclo = [nx.closeness_centrality(whatsapp_graph,student) for student in whatsapp_graph]

#pos = nx.spring_layout(whatsapp_graph,k=1,iterations=150)
pos = nx.spring_layout(whatsapp_graph)
#plt.figure(figsize=(20,20))

#plt.figure(figsize=(15,15))
#nx.draw_networkx(whatsapp_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm')

plt.figure(figsize=(20,12.6))
nx.draw_networkx(whatsapp_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm',edge_color='0.7')
plt.savefig('degclovarying.pdf',format='pdf')

#---------------------------------------------------------------------------------
#VARYING CENTRALITY GRAPHS - NODESIZE = DEG CEN, COLOR = BTW CEN

nodesizelistclo = [80*whatsapp_graph.degree(node) for node in whatsapp_graph]
nodecolorlistclo = []
edgeclrlist = []
for node in whatsapp_graph:
    if node in ['Bhargava','Prashant']:
        nodecolorlistclo.append('#FFD700')
    elif whatsapp_graph.node[node]['sec'] == 'B':
        nodecolorlistclo.append('#32CD32')
    else:
        nodecolorlistclo.append('#DCDCDC')
                                
for u,v in whatsapp_graph.edges():
        if whatsapp_graph.node[u]['sec'] == 'B' and whatsapp_graph.node[v]['sec'] == 'C':
            edgeclrlist.append('#FF4500')
        else:
            edgeclrlist.append('0.85')
#pos = nx.spring_layout(whatsapp_graph,k=1,iterations=150)
pos = nx.spring_layout(whatsapp_graph)
#plt.figure(figsize=(20,20))

#plt.figure(figsize=(15,15))
#nx.draw_networkx(whatsapp_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm')

plt.figure(figsize=(20,12.6))
nx.draw_networkx(whatsapp_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm',edge_color = edgeclrlist)
plt.savefig('degbtwvaryinghighlighted.pdf',format='pdf')
#---------------------------------------------------------------------------------
#VARYING CENTRALITIES - NODESIZE = BETW CEN, COLOR = CLOSE CEN

nodesizelistclo = [30000*nx.betweenness_centrality(whatsapp_graph)[student] for student in whatsapp_graph]
nodecolorlistclo = [nx.closeness_centrality(whatsapp_graph,student) for student in whatsapp_graph]

#pos = nx.spring_layout(whatsapp_graph,k=1,iterations=150)
pos = nx.spring_layout(whatsapp_graph)
#plt.figure(figsize=(20,20))

#plt.figure(figsize=(15,15))
#nx.draw_networkx(whatsapp_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm')

plt.figure(figsize=(20,20))
nx.draw_networkx(whatsapp_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm',edge_color = '0.8')

#---------------------------------------------------------------------------------
alist = []
blist = []
clist = []
for node in whatsapp_graph:
    if whatsapp_graph.node[node]['sec'] == 'A':
        alist.append(node)
    elif whatsapp_graph.node[node]['sec'] == 'B':
        blist.append(node)
    elif whatsapp_graph.node[node]['sec'] == 'C':
        clist.append(node)
    else:
        pass

#---------------------------------------------------------------------------------
#A-sec graph
'''
asec = nx.subgraph(whatsapp_graph,alist)

nodesizelistclo = [2000*nx.closeness_centrality(asec,node) for node in asec]
nodecolorlistclo = [nx.closeness_centrality(asec,student) for student in asec]
plt.figure(figsize=(15,15))
nx.draw_networkx(asec,node_size=nodesizelistclo,node_color =nodecolorlistclo,cmap='coolwarm',edge_color = '0.6')


#B-sec graph

bsec = nx.subgraph(whatsapp_graph,blist) 
nodesizelistclo = [2000*nx.closeness_centrality(bsec,node) for node in bsec]
nodecolorlistclo = [nx.closeness_centrality(bsec,student) for student in bsec]
plt.figure(figsize=(15,15))
nx.draw_networkx(bsec,node_size=nodesizelistclo,node_color =nodecolorlistclo,cmap='coolwarm',edge_color = '0.6')


#C-sec graph

csec = nx.subgraph(whatsapp_graph,clist)
nodesizelistclo = [2000*nx.closeness_centrality(csec,node) for node in csec]
nodecolorlistclo = [nx.closeness_centrality(csec,student) for student in csec]
plt.figure(figsize=(15,15))
nx.draw_networkx(csec,node_size=nodesizelistclo,node_color =nodecolorlistclo,cmap='coolwarm',edge_color = '0.6')
'''
#-------------------------------------------------------------------------------------------------