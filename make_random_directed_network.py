import networkx as nx
from networkx.drawing.nx_pydot import read_dot

G = nx.fast_gnp_random_graph(20,2/20.,directed=True)
print(G)
print(list(G.nodes()))
#nx.relabel_nodes(G,{u:int(u)-1 for u in G.nodes()},copy=False)
print(list(G.nodes()))

from networkx.readwrite import json_graph
import simplejson as json

data1 = nx.node_link_data(G)

with open('data.json','w') as f:
    json.dump(data1,f,iterable_as_array=True)

