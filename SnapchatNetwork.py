# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:22:20 2018

@author: Pranav
"""

import networkx as nx
import matplotlib.pyplot as plt


snapchat_graph = nx.Graph()

#ADDING NODES

snapchat_graph.add_node('Manoj',sec='A',gen='M')
#snapchat_graph.add_node('Johanna',sec='A',gen='F')
#snapchat_graph.add_node('Ramya',sec='A',gen='F')
#snapchat_graph.add_node('Shalini',sec='A',gen='F')
snapchat_graph.add_node('Balasubramaniyan',sec='A',gen='M')
#snapchat_graph.add_node('Pooja',sec='A',gen='F')
snapchat_graph.add_node('Harish',sec='A',gen='M')
snapchat_graph.add_node('Keerthan',sec='A',gen='M')
snapchat_graph.add_node('Abdul',sec='A',gen='M')
#snapchat_graph.add_node('Abhishek',sec='A',gen='M')
snapchat_graph.add_node('Aditya',sec='A',gen='M')
snapchat_graph.add_node('Ajith',sec='A',gen='M')
snapchat_graph.add_node('Akash',sec='A',gen='M')
#snapchat_graph.add_node('Amit',sec='A',gen='M')
snapchat_graph.add_node('Amritha',sec='A',gen='F')
snapchat_graph.add_node('Amrutha',sec='A',gen='F')
#snapchat_graph.add_node('Arun',sec='A',gen='M')
snapchat_graph.add_node('Beenu',sec='A',gen='F')
snapchat_graph.add_node('Bhargava',sec='A',gen='M')
#snapchat_graph.add_node('Bishal',sec='A',gen='M')
#snapchat_graph.add_node('Bhavya',sec='A',gen='F')
#snapchat_graph.add_node('Chandana',sec='A',gen='F')
snapchat_graph.add_node('Darshan',sec='A',gen='M')
snapchat_graph.add_node('Sravya',sec='A',gen='F')
snapchat_graph.add_node('Gokul',sec='A',gen='M')
snapchat_graph.add_node('Pruthvi',sec='A',gen='F')
#snapchat_graph.add_node('Nidhi',sec='A',gen='F')
#snapchat_graph.add_node('Devaditya',sec='B',gen='M')
#snapchat_graph.add_node('Ashim',sec='B',gen='M')
#snapchat_graph.add_node('Bimal',sec='B',gen='M')
#snapchat_graph.add_node('Ashish',sec='B',gen='M')
#snapchat_graph.add_node('Nissi',sec='B',gen='F')
snapchat_graph.add_node('Pranav',sec='B',gen='M')
#snapchat_graph.add_node('Prashant',sec='B',gen='M')
#snapchat_graph.add_node('Prathiksha',sec='B',gen='F')
#snapchat_graph.add_node('Raja',sec='B',gen='M')
#snapchat_graph.add_node('Rakshith',sec='B',gen='M')
snapchat_graph.add_node('Rashmi',sec='B',gen='F')
#snapchat_graph.add_node('Sanjana',sec='B',gen='F')
snapchat_graph.add_node('Apeksha',sec='C',gen='F')
#snapchat_graph.add_node('Vignesh',sec='C',gen='M')
snapchat_graph.add_node('Gaurav',sec='C',gen='M')
snapchat_graph.add_node('Akansha',sec='C',gen='F')
#snapchat_graph.add_node('Santosh',sec='C',gen='M')
#snapchat_graph.add_node('Nitish',sec='C',gen='M')
snapchat_graph.add_node('Badri',sec='C',gen='M')
snapchat_graph.add_node('Tejaswini',sec='C',gen='F')
#snapchat_graph.add_node('Purvaj',sec='C',gen='M')
snapchat_graph.add_node('Rahul',sec='C',gen='M')
snapchat_graph.add_node('Rohit',sec='C',gen='M')
#snapchat_graph.add_node('Sachin',sec='C',gen='M')
#snapchat_graph.add_node('Aroon',sec='C',gen='M')
#snapchat_graph.add_node('Shimna',sec='C',gen='F')
snapchat_graph.add_node('Shreyas',sec='C',gen='M')
#snapchat_graph.add_node('Joshua',sec='C',gen='M')
#snapchat_graph.add_node('Soundarya',sec='C',gen='F')
#snapchat_graph.add_node('Sonal',sec='C',gen='F')
snapchat_graph.add_node('Aishwarya',sec='C',gen='F')

#-------------------------------------------------------------------------------
snapchat_edge_list = [('Rohit','Keerthan'),('Rohit','Gokul'),('Rohit','Apeksha'),('Rohit','Badri'),('Rohit','Rahul'),
('Rashmi','Keerthan'),
('Apeksha','Akansha'),('Apeksha','Tejaswini'),
('Tejaswini','Akansha'),
('Rahul','Beenu'),('Rahul','Gaurav'),('Rahul','Badri'),('Rahul','Shreyas'),
('Aishwarya','Rohit'),
('Keerthan','Abdul'),('Keerthan','Aditya'),('Keerthan','Ajith'),('Keerthan','Amrutha'),('Keerthan','Bhargava'),('Keerthan','Pruthvi'),
('Abdul','Akash'),('Abdul','Bhargava'),('Abdul','Darshan'),('Abdul','Gokul'),
('Aditya','Harish'),('Aditya','Ajith'),('Aditya','Amritha'),('Aditya','Amrutha'),('Aditya','Darshan'),('Aditya','Gokul'),('Aditya','Pruthvi'),
('Ajith','Abdul'),('Ajith','Bhargava'),('Ajith','Darshan'),('Ajith','Gokul'),('Ajith','Pruthvi'),('Ajith','Gaurav'),('Ajith','Shreyas'),
('Darshan','Keerthan'),('Darshan','Bhargava'),('Darshan','Gokul'),
('Sravya','Harish'),('Sravya','Pruthvi'),('Sravya','Tejaswini'),
('Gokul','Harish'),('Gokul','Akash'),('Gokul','Bhargava'),('Gokul','Pruthvi'),
('Pruthvi','Amritha'),('Pruthvi','Bhargava'),
('Amritha','Keerthan'),('Amritha','Amrutha'),
('Bhargava','Manoj'),('Bhargava','Balasubramaniyan'),('Bhargava','Akash'),('Bhargava','Sravya'),('Bhargava','Shreyas'),('Bhargava','Rahul'),
('Pranav','Abdul')]
#------------------------------------------------------------------------------------
snapchat_graph.add_edges_from(snapchat_edge_list)
#-------------------------------------------------------------------------------------
nodesizelist = [150*snapchat_graph.degree(node) for node in snapchat_graph]
nodecolorlist = []
nodecolorlist2 = [snapchat_graph.degree(student) for student in snapchat_graph]
for person in snapchat_graph:
    if snapchat_graph.node[person]['sec'] == 'A':
        nodecolorlist.append('#36688D')
    elif snapchat_graph.node[person]['sec'] == 'B':
        nodecolorlist.append('#66CC00');
    else:
        nodecolorlist.append('#F3CD05')
                
#pos = nx.circular_layout(snapchat_graph)
#plt.figure(figsize=(15,15))
#nx.draw_networkx(snapchat_graph,pos,node_color = nodecolorlist2, node_size = nodesizelist,cmap = plt.cm.Reds)
#nx.draw_networkx(snapchat_graph,pos,node_color = nodecolorlist, node_size = nodesizelist,alpha=0.9,edge_color='0.5')
#plt.savefig('snapchat_graph0.1_circular.pdf',format='pdf')

pos=nx.spring_layout(snapchat_graph)
plt.figure(figsize=(19.2,10.8))
nx.draw_networkx(snapchat_graph,pos,node_color = nodecolorlist, node_size = nodesizelist,alpha=0.9,edge_color='0.7')
plt.savefig('snapchat_graph0.1spring.pdf',format='pdf')
#--------------------------------------------------------------------------------------------------
'''
#for male-female bipartite:
from networkx.algorithms import bipartite
B = nx.Graph()
nodecolorlistb = []
for (u,v) in snapchat_edge_list:
    if snapchat_graph.node[u]['gen'] == 'M' and snapchat_graph.node[u]['gen'] != snapchat_graph.node[v]['gen']:
        B.add_node(u,gen = 'M')
        

for (u,v) in snapchat_edge_list:
    if snapchat_graph.node[v]['gen'] == 'M' and snapchat_graph.node[u]['gen'] != snapchat_graph.node[v]['gen']:
        B.add_node(v,gen = 'M')

for (u,v) in snapchat_edge_list:
    if snapchat_graph.node[u]['gen'] == 'F' and snapchat_graph.node[u]['gen'] != snapchat_graph.node[v]['gen']:
        B.add_node(u,gen = 'F')
    
for (u,v) in snapchat_edge_list:
    if snapchat_graph.node[v]['gen'] == 'F' and snapchat_graph.node[u]['gen'] != snapchat_graph.node[v]['gen']:
        B.add_node(v,gen = 'F')

for (u,v) in snapchat_edge_list:
    if snapchat_graph.node[u]['gen'] != snapchat_graph.node[v]['gen']:
        B.add_edge(u,v)
for person in B:
    if snapchat_graph.node[person]['gen'] == 'M':
        nodecolorlistb.append('#36688D')
    else:
        nodecolorlistb.append('#F3CD05')
nodesizelistbip = [100*B.degree(node) for node in B]
plt.figure(figsize=(15,15))  
pos = nx.circular_layout(B)     
nx.draw_networkx(B,pos,node_color = nodecolorlistb,edge_color = '0.75',node_size = nodesizelistbip)

X, Y = bipartite.sets(B)
pos = dict()
pos.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
plt.figure(figsize=(10,25)) 
plt.title('Bipartite Boys-Girls Graph')
nx.draw_networkx(B, pos=pos,node_color = nodecolorlistb,edge_color = '0.75', node_size = nodesizelistbip)

nx.degree(B)
#---------------------------------------------------------------------------
#Projected Graph for BOYS (common female friends)

x = set([node for node in B if B.node[node]['gen'] == 'M'])
#y = set([node for node in B if B.node[node]['gen'] == 'F']) - if you want to ddo it for girls - common male friends

Pboys = bipartite.weighted_projected_graph(B,x)
edge_width =[1*Pboys[u][v]['weight'] for u,v in Pboys.edges()]
labels_greater_than_5 = {edge:weight for edge,weight in nx.get_edge_attributes(Pboys,'weight').items() if weight >5}
plt.figure(figsize=(15,15))
plt.title('Common Female Friends')
pos = nx.circular_layout(Pboys)
nx.draw_networkx(Pboys,pos,edge_color = '0.45',width=edge_width)
nx.draw_networkx_edge_labels(Pboys,pos,edge_labels = labels_greater_than_5)

edgelist_grt_than_5 = [x for x in Pboys.edges(data=True) if x[2]['weight'] > 5]

plt.figure(figsize=(15,15))
plt.title('Common Female Friends - >5')
nx.draw_networkx(Pboys,pos,edge_color = '0.8',width=edge_width)
nx.draw_networkx_edges(Pboys,pos,edgelist = edgelist_grt_than_5,edge_color = 'green',width=edge_width)
nx.draw_networkx_edge_labels(Pboys,pos,edge_labels = labels_greater_than_5)

#Make it better by adding weights to the edges, and changing edge size accordingly. - use weighted_projected_graph(B,x) and print P.edges(data = True)
#------------------------------------------------------------------------------------------
#Projected Graph for GIRLS (common male friends)
y = set([node for node in B if B.node[node]['gen'] == 'F'])

Pgirls = bipartite.weighted_projected_graph(B,y)
edge_width =[1*Pgirls[u][v]['weight'] for u,v in Pgirls.edges()]
labels_greater_than_5 = {edge:weight for edge,weight in nx.get_edge_attributes(Pgirls,'weight').items() if weight >5}
plt.figure(figsize=(15,15))
plt.title('Common Male Friends')
pos = nx.circular_layout(Pgirls)
nx.draw_networkx(Pgirls,pos,edge_color = '0.45',width=edge_width)
nx.draw_networkx_edge_labels(Pgirls,pos,edge_labels = labels_greater_than_5)

edgelist_grt_than_5 = [x for x in Pgirls.edges(data=True) if x[2]['weight'] > 5]

plt.figure(figsize=(15,15))
plt.title('Common Male Friends - >5')
nx.draw_networkx(Pgirls,pos,edge_color = '0.8',width=edge_width)
nx.draw_networkx_edges(Pgirls,pos,edgelist = edgelist_grt_than_5,edge_color = 'green',width=edge_width)
nx.draw_networkx_edge_labels(Pgirls,pos,edge_labels = labels_greater_than_5) '''
#-------------------------------------------------------------------------------------------
#snapchat_graph coloured according to gender
'''nodesizelist = [100*snapchat_graph.degree(node) for node in snapchat_graph]
nodecolorlistg = []
#nodecolorlist2 = [snapchat_graph.degree(student) for student in snapchat_graph]

for person in snapchat_graph:
    if snapchat_graph.node[person]['gen'] == 'M':
        nodecolorlistg.append('#36688D')
    elif snapchat_graph.node[person]['gen'] == 'F':
        nodecolorlistg.append('#BDA589');
    else:
        nodecolorlistg.append('c')
                
#pos = nx.spring_layout(snapchat_graph,k=1,iterations=150)
pos = nx.spring_layout(snapchat_graph)
plt.figure(figsize=(20,20))
nx.draw_networkx(snapchat_graph,pos,node_color = nodecolorlistg, node_size = nodesizelist,edge_color='0.5')
'''
#------------------------------------------------------------------------------------------
#Boy-Boy Friendship graph
b2b = nx.Graph()

for (u,v) in snapchat_edge_list:
    if snapchat_graph.node[u]['gen'] == 'M' and snapchat_graph.node[v]['gen'] == 'M':
        b2b.add_edge(u,v)

b2bnodeclrlist = []
for person in b2b:
    if snapchat_graph.node[person]['sec'] == 'A':
        b2bnodeclrlist.append('#36688D')
    elif snapchat_graph.node[person]['sec'] == 'B':
        b2bnodeclrlist.append('#BDA589')
    elif snapchat_graph.node[person]['sec'] == 'C':
        b2bnodeclrlist.append('#F3CD05')
    else:
        b2bnodeclrlist.append('c')

pos = nx.spring_layout(b2b)
plt.figure(figsize=(12,12))
plt.title('Male- Male Friendships')
nx.draw_networkx(b2b,pos,edge_color='0.5',node_color = b2bnodeclrlist)
#--------------------------------------------------------------------------------------------
#Girl-Girl Friendship

'''for (u,v) in snapchat_edge_list:
    if snapchat_graph.node[u]['gen'] == 'F' and snapchat_graph.node[u]['sec'] == 'A':
        b2b.add_node(u,gen = 'F',sec='A')
    elif snapchat_graph.node[u]['gen'] == 'F' and snapchat_graph.node[u]['sec'] == 'B':
        b2b.add_node(u,gen = 'F',sec='B')
    elif snapchat_graph.node[u]['gen'] == 'F' and snapchat_graph.node[u]['sec'] == 'C':
        b2b.add_node(u,gen = 'F',sec='C')
    else:
        b2b.add_node(u,gen = 'F', sec = 'All')
        
for (u,v) in snapchat_edge_list:
    if snapchat_graph.node[v]['gen'] == 'F' and snapchat_graph.node[v]['sec'] == 'A':
        b2b.add_node(v,gen = 'F',sec='A')
    elif snapchat_graph.node[u]['gen'] == 'F' and snapchat_graph.node[v]['sec'] == 'B':
        b2b.add_node(v,gen = 'F',sec='B')
    elif snapchat_graph.node[v]['gen'] == 'F' and snapchat_graph.node[v]['sec'] == 'C':
        b2b.add_node(v,gen = 'F',sec='C')
    else:
        b2b.add_node(v,gen = 'F', sec = 'All')'''
        
g2g = nx.Graph()
for (u,v) in snapchat_edge_list:
    if snapchat_graph.node[u]['gen'] == 'F' and snapchat_graph.node[v]['gen'] == 'F':
        g2g.add_edge(u,v)

g2gnodeclrlist = []
for person in g2g:
    if snapchat_graph.node[person]['sec'] == 'A':
        g2gnodeclrlist.append('#36688D')
    elif snapchat_graph.node[person]['sec'] == 'B':
        g2gnodeclrlist.append('#BDA589')
    elif snapchat_graph.node[person]['sec'] == 'C':
        g2gnodeclrlist.append('#F3CD05')
    else:
        g2gnodeclrlist.append('c')
        
pos = nx.spring_layout(g2g)
plt.figure(figsize=(16,9))
plt.title('Female-Female Friendships')
nx.draw_networkx(g2g,pos,edge_color='0.5',node_color = g2gnodeclrlist)
plt.savefig('snapchatg2g.pdf',format='pdf')
#---------------------------------------------------------------------------------------------
bfs_t = nx.bfs_tree(snapchat_graph,'Pranav')
bfsnodecolorlist = []
pos = nx.shell_layout(bfs_t)
#nx.draw(G, pos, with_labels=False, arrows=True)
plt.figure(figsize=(15,15));
for person in bfs_t:
    if snapchat_graph.has_edge(person,'Pranav'):
        bfsnodecolorlist.append('r')
    else:
        bfsnodecolorlist.append('c')
nx.draw_networkx(bfs_t,pos,node_color = bfsnodecolorlist) 
#shows bfs tree with starting node Pranav. Very interesting Tree structure.
#---------------------------------------------------------------------------------
#dfs-tree
#plt.figure(figsize=(18,18)) 
#nx.draw_networkx(nx.dfs_tree(snapchat_graph,'Pranav'))

'''disc = nx.Graph()
disc.add_edges_from(snapchat_edge_list)
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
for u in snapchat_graph.nodes:
    for v in snapchat_graph.nodes:
        if mfg.has_edge(u,v) or u==v:
            continue
        else:
            cn = []
            for i in nx.common_neighbors(snapchat_graph,u,v):
                cn.append(i)
            if len(cn) > 6:
                mfg.add_edge(u,v,MF=len(cn))

nodecolorlist = []
for person in mfg:
    if snapchat_graph.node[person]['sec'] == 'A':
        nodecolorlist.append('#36688D')
    elif snapchat_graph.node[person]['sec'] == 'B':
        nodecolorlist.append('#66CC00');
    elif snapchat_graph.node[person]['sec'] == 'C':
        nodecolorlist.append('#F3CD05')
    else:
        nodecolorlist.append('c')

plt.figure(figsize=(19.2,10.8))
nx.draw_networkx(mfg,node_size=200,node_color = nodecolorlist,cmap='coolwarm',edge_color='0.7')
plt.savefig('snapchatmfg.pdf',format='pdf')
#---------------------------------------------------------------------------------
#MUTUAL FRIENDS, NOT CONNECTED. - POTENTIAL FRIENDS
mfgnc = nx.Graph()
#MORE THAN 8 MF, NOT CONNECTED
for u in snapchat_graph.nodes:
    for v in snapchat_graph.nodes:
        if mfgnc.has_edge(u,v) or u==v:
            continue
        else:
            cn = []
            for i in nx.common_neighbors(snapchat_graph,u,v):
                cn.append(i)
            if len(cn) > 2 and not(snapchat_graph.has_edge(u,v)):
                mfgnc.add_edge(u,v,MF=len(cn))            
#---------------------------------------------------------------------------------
#Degree Centrality
                
degcentgraph = nx.Graph(snapchat_graph)

nodesizelistdeg = [170*snapchat_graph.degree(node) for node in snapchat_graph]
nodecolorlist2 = [snapchat_graph.degree(student) for student in snapchat_graph]
pos = nx.spring_layout(snapchat_graph)
plt.figure(figsize=(16,9))
nx.draw_networkx(degcentgraph,node_size=nodesizelistdeg,node_color = nodecolorlist2,cmap='RdYlBu',edge_color='0.7')
plt.savefig('snapchatdegcent.pdf',format='pdf')


plt.figure(figsize=(15,15))
nx.draw_networkx(degcentgraph,node_size=nodesizelistdeg,node_color = nodecolorlist2,cmap='RdYlBu')


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
nodesizelistclo = [1500*nx.closeness_centrality(snapchat_graph,node) for node in snapchat_graph]
nodecolorlistclo = [nx.closeness_centrality(snapchat_graph,student) for student in snapchat_graph]

#pos = nx.spring_layout(snapchat_graph,k=1,iterations=150)
pos = nx.spring_layout(snapchat_graph)
plt.figure(figsize=(20,12.6))
nx.draw_networkx(snapchat_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='RdYlGn',edge_color='0.7')
plt.savefig('snapchatcc.pdf',format='pdf')
#nx.draw_networkx(snapchat_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='RdYlBu')

import operator
sorted(nx.closeness_centrality(snapchat_graph).items(),key=operator.itemgetter(1),reverse=True)

#----------------------------------------------------------------------------------
#Betweenness Centrality
nodesizelistbet = [25000*nx.betweenness_centrality(snapchat_graph)[node] for node in snapchat_graph]
nodecolorlistbet = [nx.betweenness_centrality(snapchat_graph)[student] for student in snapchat_graph]
pos = nx.spring_layout(snapchat_graph)
plt.figure(figsize=(20,12.6))
nx.draw_networkx(snapchat_graph,node_size=nodesizelistbet,node_color = nodecolorlistbet,cmap='YlOrBr',edge_color='0.7')
plt.savefig('snapchatbtwcent.pdf',format='pdf')
#----------------------------------------------------------------------------------
#Edge-betweenness centrality

edgesizelistbete = [200*nx.edge_betweenness_centrality(snapchat_graph)[(u,v)] for u,v in nx.edge_betweenness_centrality(snapchat_graph).keys()]
#nodecolorlistbete = [nx.betweenness_centrality(snapchat_graph)[node] for node in snapchat_graph]
edgecolorlistbete = [nx.edge_betweenness_centrality(snapchat_graph)[(u,v)] for u,v in nx.edge_betweenness_centrality(snapchat_graph).keys()]
pos = nx.spring_layout(snapchat_graph,k=1,iterations=150)
#pos = nx.spring_layout(snapchat_graph)
plt.figure(figsize=(20,20))
nx.draw_networkx(snapchat_graph,pos,edge_color = edgecolorlistbete,width=edgesizelistbete,node_size=500,node_color = '#BDA589')
#nx.draw_networkx_edges(Pgirls,pos,edgelist = edgelist_grt_than_5,edge_color = 'green',width=edge_width)
#nx.draw_networkx_edge_labels(Pgirls,pos,edge_labels = labels_greater_than_5)
#plt.figure(figsize=(20,20))
#nx.draw_networkx(snapchat_graph,node_size=20,node_color = nodecolorlistbete,cmap='coolwarm')

#nx.draw_networkx(snapchat_graph,node_size=20,node_color = nodecolorlistbete,cmap='YlOrBr',edge)




#------------------------------------------------------------------------------------
#CLIQUES

clqlist = []
clqlist = list(nx.find_cliques(snapchat_graph))
for i in range(len(clqlist)):
    print(len(clqlist[i]), clqlist[i])

#show how a clique looks like- just some random 6 node example, and then show the graph's cliques
c = nx.subgraph(snapchat_graph,['Beenu', 'Nidhi', 'Amrutha', 
                                'Keerthan', 'Chandana', 'Pruthvi',
                                'Bhavya', 'Amritha'])
#highlight those nodes and edges in the graph.    
    
#-------------------------------------------------------------------------------------
#Degree distribution graph
   
#import seaborn as sns
import collections
deg_dict = dict(snapchat_graph.degree)

degree_sequence = sorted([d for n, d in snapchat_graph.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.35, color='#CCCC00')

plt.title("Degree Histogram")
plt.ylabel("Number of People")
plt.xlabel("Number of Friends")
ax.set_xticks([d + 0.5 for d in deg])
ax.set_xticklabels(deg)
# draw graph in inset
plt.axes([0.4, 0.4, 0.5, 0.5])
Gcc = sorted(nx.connected_component_subgraphs(snapchat_graph), key=len, reverse=True)[0]
pos = nx.spring_layout(snapchat_graph)
plt.axis('off')
nx.draw_networkx_nodes(snapchat_graph, pos, node_size=20,node_color='#999900')
nx.draw_networkx_edges(snapchat_graph, pos, alpha=0.4)
#plt.show()
plt.savefig('ddg-sp0.1.pdf',format='pdf')

#----------------------------------------------------------------------------------
#VARYING CENTRALITY GRAPhs - nodesize = DEG CEN, nodecolor = CLO cen

nodesizelistclo = [100*snapchat_graph.degree(node) for node in snapchat_graph]
nodecolorlistclo = [nx.closeness_centrality(snapchat_graph,student) for student in snapchat_graph]

#pos = nx.spring_layout(snapchat_graph,k=1,iterations=150)
pos = nx.spring_layout(snapchat_graph)
#plt.figure(figsize=(20,20))

#plt.figure(figsize=(15,15))
#nx.draw_networkx(snapchat_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm')

plt.figure(figsize=(20,20))
nx.draw_networkx(snapchat_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm',edge_color='0.7')
#---------------------------------------------------------------------------------
#VARYING CENTRALITY GRAPHS - NODESIZE = DEG CEN, COLOR = BTW CEN

nodesizelistclo = [100*snapchat_graph.degree(node) for node in snapchat_graph]
nodecolorlistclo = [nx.betweenness_centrality(snapchat_graph)[student] for student in snapchat_graph]

#pos = nx.spring_layout(snapchat_graph,k=1,iterations=150)
pos = nx.spring_layout(snapchat_graph)
#plt.figure(figsize=(20,20))

#plt.figure(figsize=(15,15))
#nx.draw_networkx(snapchat_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm')

plt.figure(figsize=(20,20))
nx.draw_networkx(snapchat_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm',edge_color = '0.75')

#---------------------------------------------------------------------------------
#VARYING CENTRALITIES - NODESIZE = BETW CEN, COLOR = CLOSE CEN

nodesizelistclo = [30000*nx.betweenness_centrality(snapchat_graph)[student] for student in snapchat_graph]
nodecolorlistclo = [nx.closeness_centrality(snapchat_graph,student) for student in snapchat_graph]

#pos = nx.spring_layout(snapchat_graph,k=1,iterations=150)
pos = nx.spring_layout(snapchat_graph)
#plt.figure(figsize=(20,20))

#plt.figure(figsize=(15,15))
#nx.draw_networkx(snapchat_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm')

plt.figure(figsize=(20,20))
nx.draw_networkx(snapchat_graph,node_size=nodesizelistclo,node_color = nodecolorlistclo,cmap='coolwarm',edge_color = '0.8')

#---------------------------------------------------------------------------------
alist = []
blist = []
clist = []
for node in snapchat_graph:
    if snapchat_graph.node[node]['sec'] == 'A':
        alist.append(node)
    elif snapchat_graph.node[node]['sec'] == 'B':
        blist.append(node)
    elif snapchat_graph.node[node]['sec'] == 'C':
        clist.append(node)
    else:
        pass
#---------------------------------------------------------------------------------
#A-sec graph
'''
asec = nx.subgraph(snapchat_graph,alist)

nodesizelistclo = [2000*nx.closeness_centrality(asec,node) for node in asec]
nodecolorlistclo = [nx.closeness_centrality(asec,student) for student in asec]
plt.figure(figsize=(15,15))
nx.draw_networkx(asec,node_size=nodesizelistclo,node_color =nodecolorlistclo,cmap='coolwarm',edge_color = '0.6')


#B-sec graph

bsec = nx.subgraph(snapchat_graph,blist) 
nodesizelistclo = [2000*nx.closeness_centrality(bsec,node) for node in bsec]
nodecolorlistclo = [nx.closeness_centrality(bsec,student) for student in bsec]
plt.figure(figsize=(15,15))
nx.draw_networkx(bsec,node_size=nodesizelistclo,node_color =nodecolorlistclo,cmap='coolwarm',edge_color = '0.6')


#C-sec graph

csec = nx.subgraph(snapchat_graph,clist)
nodesizelistclo = [2000*nx.closeness_centrality(csec,node) for node in csec]
nodecolorlistclo = [nx.closeness_centrality(csec,student) for student in csec]
plt.figure(figsize=(15,15))
nx.draw_networkx(csec,node_size=nodesizelistclo,node_color =nodecolorlistclo,cmap='coolwarm',edge_color = '0.6')
'''
#-----------------------------------------------------------------------------------------------