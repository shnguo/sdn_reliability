import build_map_mat as bmm
import networkx as nx
import itertools
import numpy as np
import matplotlib.pyplot as plt
import time
longesttime=20*60*1000
global path_matrix
def calculate_pro(G,pos,k):
    start = time.clock()
    num_nodes=len(G.nodes())
    shortest_path_matrix=np.empty((num_nodes,num_nodes))
    path_matrix={}
    #print (num_nodes) 
    shortest_path=nx.shortest_path_length(G,weight='weight')
    path=nx.shortest_path(G,weight='weight')
    prob_edge=nx.get_edge_attributes(G,'prob')
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
    
    
    #print(network_complity_pro)
    for i in G.nodes():
        temp_dict={}
        for j in G.nodes():
            #初始化最短路径
            shortest_path_matrix[i][j]=shortest_path[i][j]
            pas=""
            for nodel in path[i][j]:
            
                pas=pas+'+'+str(nodel)
                
            
            temp_dict[j]=pas
        
            #print('i=',i,'j=',j,path[i][j],path_matrix[i][j])
            #初始化相对概率
            fail_matrix[i][j]=(1-network_complity_pro)*(fail_matrix[i][j]/sum_pro)
        path_matrix[i]=temp_dict
    #print('path_matrix[19][19]=',path_matrix[8][19])        
    print(shortest_path_matrix)
    #print(fail_matrix)
    
    temp_pos = np.zeros((num_nodes,num_nodes))
    min_max_length=99999999999
    min_average=0

    final_pos=[]
    assigment={}
    assigment_nodetocontroller={}
    solution=0
    permutations_list=list(itertools.combinations(G.nodes(),k))
    #print(permutations_list)
    for cobin in permutations_list:
        #print(cobin)
        temp_assigment={}
        temp_assigment_nodetocontroller={}
        temp_pos[:]=float('inf')
        #print(temp_pos)
        for cell in cobin:
            temp_pos[:,cell]=1
            temp_assigment[cell]=[]
        temp_matrix=shortest_path_matrix*temp_pos
        min_max_temp_list=np.nanmin(temp_matrix,axis=1)
        min_max_average_temp=min_max_temp_list.sum()*network_complity_pro
        min_max=np.amax(min_max_temp_list)
        min_temp=np.amax(min_max_temp_list)*network_complity_pro
        for o in range(num_nodes):
            for cell in cobin:
                if shortest_path_matrix[o][cell]==min_max_temp_list[o]:
                    temp_assigment[cell].append(o)
                    temp_assigment_nodetocontroller[o]=cell
                    break
        for edge in G.edges():
            temp_weight=G[edge[0]][edge[1]]['weight']
            #print(temp_weight)
            
            #print(nx.shortest_path(G, source=edge[0],target=edge[1], weight='weight'))
            edge1=str(edge[0])+'+'+str(edge[1])
            edge2=str(edge[1])+'+'+str(edge[0])
            fail_max_length=min_max
            fail_max_average_length=min_max_temp_list.sum()
            for i in range(num_nodes):
                if edge1 in path_matrix[i][temp_assigment_nodetocontroller[i]] or edge2 in path_matrix[i][temp_assigment_nodetocontroller[i]]:
                    G[edge[0]][edge[1]]['weight']=temp_weight
                    orign_length=nx.shortest_path_length(G,source=i,target=temp_assigment_nodetocontroller[i],weight='weight')
                    G[edge[0]][edge[1]]['weight']=float('inf')
                    temp_length=nx.shortest_path_length(G,source=i,target=temp_assigment_nodetocontroller[i],weight='weight')
                    fail_max_average_length=fail_max_average_length-orign_length+temp_length
                    if temp_length>fail_max_length:
                        fail_max_length=temp_length    
                    if(fail_max_length==float('inf')):
                        
                        break
            if(fail_max_length==float('inf')):
                min_temp=min_temp+(longesttime)*fail_matrix[edge[0]][edge[1]]
                min_max_average_temp=min_max_average_temp+longesttime*fail_matrix[edge[0]][edge[1]]
                        
                           
            else:
                min_temp=min_temp+fail_max_length*fail_matrix[edge[0]][edge[1]]
                min_max_average_temp=min_max_average_temp+fail_max_average_length*fail_matrix[edge[0]][edge[1]]
            G[edge[0]][edge[1]]['weight']=temp_weight
        #if cell ==19 :
         #   print('min_temp19=',min_temp)
        if min_max_length>min_temp:
            min_max_length=min_temp
            
            assigment=temp_assigment.copy()
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
    #print('min_max_length=',min_max_length)
    
    #print('solution=',solution)
    end = time.clock()
    return final_pos,assigment,assigment_nodetocontroller,end-start


def main():
    g,pos=bmm.build_map_mat()
    final_pos,assigment,assigment_nodetocontroller=calculate_pro(g,pos,2)
    

if __name__=="__main__":
    main()
