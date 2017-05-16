import build_map_mat as bmm
import networkx as nx
import itertools
import numpy as np
import random
import matplotlib.pyplot as plt
import time
nodeshape = 'so^>v<dph8'
def calculate_free(G,pos,k):
    start = time.clock()
    num_nodes=len(G.nodes())
    shortest_path_matrix=np.empty((num_nodes,num_nodes))
    path_matrix=[[0] * num_nodes] * num_nodes
    #print (num_nodes) 
    shortest_path=nx.shortest_path_length(G,weight='distance')
    path=nx.shortest_path(G,weight='distance')
    #print(path)
    for i in range(num_nodes):
        for j in range(num_nodes):
            shortest_path_matrix[i][j]=shortest_path[i][j]
            pas=""
            for node in path[i][j]:
                pas=pas+'+'+str(node)
            path_matrix[i][j]=pas
    #print(path_matrix)
    temp_pos = np.zeros((num_nodes,num_nodes))
    min_max_length=99999999999
    min_average=0

    final_pos=[]
    assigment={}
    solution=0
    assigment_nodetocontroller={}
    permutations_list=list(itertools.combinations(G.nodes(),k))
    #print(permutations_list)
    for cobin in permutations_list:
        #print(cobin)
        temp_assigment={}
        temp_assigment_nodetocontroller={}
        temp_pos[:]=float('inf')
        for cell in cobin:
            temp_pos[:,cell]=1
            temp_assigment[cell]=[]
        min_max_temp_list=np.nanmin(shortest_path_matrix*temp_pos,axis=1)
        min_max_average_temp=min_max_temp_list.sum()
        min_temp=np.amax(min_max_temp_list)
        for o in range(num_nodes):
            for cell in cobin:
                if shortest_path_matrix[o][cell]==min_max_temp_list[o]:
                    temp_assigment[cell].append(o)
                    temp_assigment_nodetocontroller[o]=cell
                    break
        if min_max_length>min_temp:
            min_max_length=min_temp
            
            assigment=temp_assigment.copy();
            assigment_nodetocontroller=temp_assigment_nodetocontroller.copy()
            solution=1
            min_average=min_max_average_temp;
            final_pos.clear();
            for cell in cobin:
                final_pos.append(cell)
        elif min_max_length==min_temp:
            if min_max_average_temp<min_average:
                min_average=min_max_average_temp
                assigment=temp_assigment.copy();
                assigment_nodetocontroller=temp_assigment_nodetocontroller.copy()
                final_pos.clear();
                for cell in cobin:
                    final_pos.append(cell)           
            solution=solution+1
    
    #print('solution=',solution)
    end = time.clock()
    return final_pos,assigment,assigment_nodetocontroller,end-start


def main():
    g,pos=bmm.build_map_mat()
    pos,assigment,assigment_nodetocontroller,time=calculate_free(g,pos,1)
    print('assigment_nodetocontroller=',assigment_nodetocontroller)
    plt.savefig('./lssssss')
    plt.show() 

if __name__=="__main__":
    main()
