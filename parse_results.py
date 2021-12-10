import pickle
import pandas as pd
from scipy.io import savemat
import numpy as np

obj = pd.read_pickle(r'C:\Users\Anirudh Ghantasala\Documents\GitHub\eco-dqn\ER_200spin\eco\data\results_custom_100subgraphs_200node_250master_raw.pkl')
num_nodes = 200
num_graphs = 100
num_trials = 50


min_energies = np.zeros((num_graphs,num_trials))
for i in range(num_graphs):
    min_energies[i,:] = obj['cuts'][i]
mdict =  {'min_energies':min_energies}
prefix = r'C:\Users\Anirudh Ghantasala\Box\Research\Data\MA598\results'
savemat(prefix+'\\rl_'+str(num_graphs)+'subgraphs_'+str(num_nodes)+'nodes_'+str(num_trials) +'runs.mat', mdict)





