import build_map_mat as bmm
import networkx as nx
import itertools
import numpy as np
import random
import calculate_pro as cp
import calculate_free as cf
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib.ticker import FuncFormatter
import matplotlib
import time
longesttime=20*60*1000
def verification(G,pos,final_pos,assigment,assigment_nodetocontroller):
    start = time.clock()
    num_nodes=len(G.nodes())
    shortest_path_matrix=np.empty((num_nodes,num_nodes))
    shortest_path=nx.shortest_path_length(G,weight='weight')
    path=nx.shortest_path(G,weight='weight')
    prob_edge=nx.get_edge_attributes(G,'prob')
    path_matrix={}
    #print(prob_edge)
    prob_matrix=np.empty((num_nodes,num_nodes))
    fail_matrix=np.zeros((num_nodes,num_nodes))
    network_complity_pro=1
    sum_pro=0
    for key in  prob_edge.keys():
        #print(key)
        prob_matrix[key[0]][key[1]]=prob_edge[key]
        prob_matrix[key[1]][key[0]]=prob_edge[key]
        fail_matrix[key[0]][key[1]]=1-prob_edge[key]
        fail_matrix[key[1]][key[0]]=1-prob_edge[key]
        network_complity_pro=network_complity_pro*prob_edge[key]
        sum_pro=sum_pro+1-prob_edge[key]
    for i in range(num_nodes):
        temp_dict={}
        for j in range(num_nodes):
            #初始化最短路径
            shortest_path_matrix[i][j]=shortest_path[i][j]
            pas=""
            for node in path[i][j]:
                pas=pas+'+'+str(node)
            temp_dict[j]=pas
            path_matrix[i]=temp_dict
            #初始化相对概率
            fail_matrix[i][j]=(1-network_complity_pro)*(fail_matrix[i][j]/sum_pro)
    min_max=0
    min_max_pro=0
    min_max_list=[]
    min_max_dict={}
    
    for node in G.nodes():
        if shortest_path_matrix[node][assigment_nodetocontroller[node]]>min_max:
            min_max=shortest_path_matrix[node][assigment_nodetocontroller[node]]
        
    #print('network_complity_pro=',network_complity_pro)
    min_max_pro=min_max_pro+min_max*network_complity_pro
    
   
    min_max_list.append(min_max)
    
    #min_max_list.append(longesttime)
    
    min_max_dict[min_max]=network_complity_pro
    
    min_max_dict[longesttime]=0
    
    for edge in G.edges():
            temp_weight=G[edge[0]][edge[1]]['weight']
            G[edge[0]][edge[1]]['weight']=float('inf')
            edge1=str(edge[0])+'+'+str(edge[1])
            edge2=str(edge[1])+'+'+str(edge[0])            
            fail_max_length=min_max
            for i in G.nodes():
                if edge1 in path_matrix[i][assigment_nodetocontroller[i]] or edge2 in path_matrix[i][assigment_nodetocontroller[i]]:
                    temp_length=nx.shortest_path_length(G,source=i,target=assigment_nodetocontroller[i],weight='weight')
                    if temp_length>fail_max_length:
                        fail_max_length=temp_length    
                    if(fail_max_length==float('inf')):                        
                        break
            if fail_max_length==float('inf'):
                min_max_pro=min_max_pro+(longesttime)*fail_matrix[edge[0]][edge[1]]
                min_max_dict[longesttime]=min_max_dict[longesttime]+fail_matrix[edge[0]][edge[1]]
                
            else:
                min_max_pro=min_max_pro+fail_max_length*fail_matrix[edge[0]][edge[1]]
                if fail_max_length in min_max_list:
                     min_max_dict[fail_max_length]=min_max_dict[fail_max_length]+fail_matrix[edge[0]][edge[1]]
                else:
                     min_max_list.append(fail_max_length)
                     min_max_dict[fail_max_length]=fail_matrix[edge[0]][edge[1]]
            G[edge[0]][edge[1]]['weight']=temp_weight
    

    
        
    return min_max_pro,min_max_list,min_max_dict

def main():
    g,pos=bmm.build_map_mat()
    final_pos,assigment,assigment_nodetocontroller,time=cp.calculate_pro(g,pos,2)
    A,B,C=verification(g,pos,final_pos,assigment,assigment_nodetocontroller)
    print(A,B,C)
if __name__=="__main__":
    main()