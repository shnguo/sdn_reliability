import scipy.io as sio
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import  pickle
import math
color = ['cyan','yellow','r','lightgreen','magenta','b']
def rad(flo):
    return flo * math.pi / 180.0
def distance(lat1,lng1,lat2,lng2):
    radlat1=rad(lat1)
    radlat2=rad(lat2)
    a=radlat1-radlat2
    b=rad(lng1)-rad(lng2)
    s=2*math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))
    earth_radius=6378.137
    s=s*earth_radius
    if s<0:
        return -s
    else:
        return s
        
def build_map_mat():
    matfn='internet2.topo.mat'
    data=sio.loadmat(matfn,mat_dtype=False)
    topology=data['topology']
    nodenames=data['nodenames']
    coordinates=data['coordinates']
    G=nx.from_numpy_matrix(topology)
    prob = pickle.load(open("tmp.txt", "rb"))
    #print(prob)
    
    #prob_matrix=nx.get_edge_attributes(G,'prob')
    #print(prob)
    i=0
    for x,y in coordinates:
        G.node[i]['x']=x
        G.node[i]['y']=y
        i=i+1
    i=0
    for name in nodenames:
        G.node[i]['name']=name[0][0]
        i=i+1 
        
    nodes=G.nodes()
    pos={}
    for node in nodes:
        list_=[]
        list_.insert(0,G.node[node]['x'])
        list_.insert(1,G.node[node]['y'])
        tup=tuple(list_)
        pos[node]=tup
    
    edges=G.edges()
    i=0
    dict1={}
    dict3={}
    for edge in edges:
        if G[edge[0]][edge[1]]['weight']==float('inf'):
            #print(G[edge[0]][edge[1]]['weight'])
            G.remove_edge(edge[0],edge[1])
        else:
           G[edge[0]][edge[1]]['weight']=G[edge[0]][edge[1]]['weight']/(3*10**5)
           list_=[]
           list_.insert(0,edge[0])
           list_.insert(1,edge[1])
           tup=tuple(list_)
           dict1[tup]=prob[i]
           dict3[tup]=G[edge[0]][edge[1]]['weight']/prob[i]
           i=i+1
    edges=G.edges()
    #print(len(edges))
    dict2={}
    for edge in edges:
        distancet=distance(G.node[edge[0]]['y'],G.node[edge[0]]['x'],G.node[edge[1]]['y'],G.node[edge[1]]['x'])
        #print(distancet/G[edge[0]][edge[1]]['weight'])
        list_=[]
        list_.insert(0,edge[0])
        list_.insert(1,edge[1])
        tup=tuple(list_)
        dict2[tup]=distancet        
        #print(edge,'  ',G[edge[0]][edge[1]]['weight'],'   ',distancet)
        
        
    nx.set_edge_attributes(G, 'prob', dict1)
    nx.set_edge_attributes(G, 'distancet', dict2)
    nx.set_edge_attributes(G, 'distance', dict3)
    G[8][32]['prob']=1
    G[17][18]['prob']=1
    
    return G,pos
        
def main():
    
    g,pos=build_map_mat()
    
    f1 = plt.figure()
    g[8][32]['weight']=float('inf')
    print(nx.shortest_path_length(g,source=8,target=19,weight='weight')==float('inf'))
    print(nx.draw_networkx(g,pos,node_color='cadetblue'))
    plt.show()
    
    #print(g.nodes())
    #print(g.edges())

if __name__=="__main__":
    main()
