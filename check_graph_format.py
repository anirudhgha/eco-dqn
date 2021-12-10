
import pickle
import networkx as nx
import numpy as np

graph_save_loc = r"C:\Users\alasg\Documents\GitHub\eco-dqn\_graphs\validation\ER_200spin_p15_100graphs.pkl"

graphs_test = pickle.load(open(graph_save_loc,'rb'))

graphs_test = [nx.to_numpy_array(g) for g in graphs_test]

print(graphs_test[0].shape)

print(type(graphs_test))
print(np.unique(graphs_test[0]))



# to build a graph set which the neural network can use, we do the following. 

#1. format a set of graphs as a list of nx.Graph objects
#2. pickle the list
