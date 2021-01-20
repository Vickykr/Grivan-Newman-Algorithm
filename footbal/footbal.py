import networkx as nx
import itertools#for combinations of nodes for making two communities
import matplotlib.pyplot as plt
import pandas as pd

def edge_to_remove(G):
  dict1 = nx.edge_betweenness_centrality(G)
  list_of_tuples = dict1.items() #contains edges and the betweeness
  list_of_tuples=sorted(list_of_tuples,key=lambda x:x[1],reverse=True)
  #list_of_tuples.sort(key = lambda x:x[1],reverse = True) #sort in descending order w.r.t second element
  return list_of_tuples[0][0]

def girvan(G):
  c = list(nx.connected_component_subgraphs(G)) # To check if graph is connected
  l = len(c)
  print('The number of connected componenets are ',l)
  
  while(l==1):  
    G.remove_edge(*edge_to_remove(G)) #((a,b))-->(a,b)
    c = list(nx.connected_component_subgraphs(G)) # To check if graph is connected
    l = len(c)
    print('The number of connected componenets are ',l)
    
  return c

dataset = pd.read_csv('football.csv')
data_array = dataset.iloc[:-1,].values
G = nx.Graph()
n = set([])
for i in range (len(data_array)):
  n.add(data_array[i][0])
  n.add(data_array[i][1])
for i in n:
  G.add_node(i)
for i in range(len(data_array)):
    G.add_edge(data_array[i][0],data_array[i][1])

nx.draw(G,with_labels=1)
plt.show()
c = girvan(G)
for i in c:
    print(i.nodes())
    print('----------------')

nx.draw(G,with_labels=1)
plt.show()

