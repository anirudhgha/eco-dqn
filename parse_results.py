import pickle
import pandas as pd
from scipy.io import savemat
import numpy as np

obj = pd.read_pickle(r'C:\Users\alasg\Documents\GitHub\eco-dqn\results\results_custom_100graphs_50node_raw.pkl')
num_nodes = 50
num_graphs = 100
num_trials = 15


min_energies = np.zeros((num_graphs,num_trials))
for i in range(num_graphs):
    min_energies[i,:] = obj['cuts'][i]
mdict =  {'min_energies':min_energies}
savemat('rl_'+str(num_graphs)+'graphs_'+str(num_nodes)+'nodes_'+str(num_trials) +'runs.mat', mdict)





