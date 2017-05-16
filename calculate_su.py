import build_map_mat as bmm
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import itertools
longesttime=20*60*1000
import time
nodeshape = 'so^>v<dph8'
def calculate_su(G,pos,k):
    start=time.clock()
    num_nodes=len(G.nodes())
    #print(nx.node_connected_component(G,1))
    
    shortest_path_matrix=np.empty((num_nodes,num_nodes))
    #A = nx.adjacency_matrix(G).to_dict_of_dicts()
    #print(nx.neighbors(G,8))
    shortest_path=nx.shortest_path_length(G,weight='distance')
    
    
    for i in G.nodes():
        for j in G.nodes():
            #初始化最短路径
            shortest_path_matrix[i][j]=shortest_path[i][j]
   
    temp_pos = np.zeros((num_nodes,num_nodes))
    min_max_length=99999999999
    min_average=0

    final_pos=[]
    assigment={}
    #print(G.nodes())
    for cell in G.nodes():
        temp_assigment={}
        temp_assigment_nodetocontroller={}
        temp_pos[:]=float('inf')
        temp_pos[:,cell]=1
        temp_assigment[cell]=[]
        min_max_temp_list=np.nanmin(shortest_path_matrix*temp_pos,axis=1)
        min_max_average_temp=min_max_temp_list.sum()
        min_temp=np.amax(min_max_temp_list)
        for o in range(num_nodes):
                if shortest_path_matrix[o][cell]==min_max_temp_list[o]:
                    temp_assigment[cell].append(o)
                    temp_assigment_nodetocontroller[o]=cell
                    break
        if min_max_length>min_temp:
            min_max_length=min_temp
            final_pos.clear();
            final_pos.append(cell)
        elif min_max_length==min_temp:
            if min_max_average_temp<min_average:
                min_average=min_max_average_temp
                final_pos.clear();
                final_pos.append(cell)           
    assigment_dit={}
    assigment_dit[final_pos[0]]=G.nodes()
    #print(assigment_dit)
    for i in range(k+10):
        temp_max=0
        temp_key=-1
        temp_v=-1
        temp_list=[]
        for key,value in assigment_dit.items():
            #print(value)
            for v in value:
                if shortest_path_matrix[key][v]>temp_max:
                    temp_max=shortest_path_matrix[key][v]
                    temp_key=key
                    temp_v=v
        #print('temp_v=',temp_v)
        temp_list.append(temp_v)
        final_pos.append(temp_v)
        #print(temp_v)
        if i==int(k+9):
            min_max=9999999999
            print("i=",i)
            print("final_pos=",final_pos)
            permutations_list=list(itertools.combinations(final_pos,i-8))
            print(permutations_list)
            for cobin in permutations_list:
                temp_assigment={}
                temp_assigment_nodetocontroller={}
                temp_pos[:]=float('inf')
                for cell in cobin:
                    temp_pos[:,cell]=1
                    temp_assigment[cell]=[]
                temp_matrix=shortest_path_matrix*temp_pos
                min_max_temp_list=np.nanmin(temp_matrix,axis=1)
                temp_min_max=np.amax(min_max_temp_list)
                if temp_min_max<min_max:
                    min_max=temp_min_max
                    for o in range(num_nodes):
                        for cell in cobin:
                            if shortest_path_matrix[o][cell]==min_max_temp_list[o]:
                                temp_assigment[cell].append(o)
                                temp_assigment_nodetocontroller[o]=cell
                                break
                    assigment_dit=temp_assigment.copy()
                    final_pos.clear()
                    final_pos=list(cobin)
                    print("cobin=",final_pos)
            continue
                    
                
        
            
            
        
        assigment_dit[temp_key].remove(temp_v)
        
        #final_pos.append(temp_v)
        for key,value in assigment_dit.items():
            #print(value)
            for v in value:
                #print(v)
                if shortest_path_matrix[key][v]>shortest_path_matrix[temp_v][v]:                   
                    temp_list.append(v)
            for v in temp_list:
                if v in assigment_dit[key]:
                    assigment_dit[key].remove(v)
        assigment_dit[temp_v]=temp_list
        #print('assigment_dit',i,'=',assigment_dit)
    for key,value in assigment_dit.items():
        for v in value:
            assigment[v]=key
    end=time.clock()
    return final_pos,assigment_dit,assigment,end-start


def main():
    g,pos=bmm.build_map_mat()
    timelist=[]
    #for i in range(5):
    i=3    
    final_pos,assigment,assigment_nodetocontroller,times=calculate_su(g,pos,0)
    plt.figure()
    for node in final_pos:
        nx.draw_networkx(g,pos,nodelist=assigment[node],node_size= 300,node_color=bmm.color[final_pos.index(node)%len(bmm.color)])
        nx.draw_networkx(g,pos,nodelist=[node],node_size= 300,node_color=bmm.color[final_pos.index(node)%len(bmm.color)],node_shape=nodeshape[0])
    plt.axis('off')
    #print(final_pos)
    #print(assigment)
        #timelist.append(times)
    #print(timelist)
    plt.show()
    
if __name__=="__main__":
    main()
