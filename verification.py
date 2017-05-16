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
longesttime=20*60*1000
def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'
def main():
    g,pos=bmm.build_map_mat()
    final_pos_p,assigment_p,assigment_nodetocontroller_p=cp.calculate_pro(g,pos,3)
    g,pos=bmm.build_map_mat()
    final_pos_f,assigment_f,assigment_nodetocontroller_f=cf.calculate_free(g,pos,3)
    g,pos=bmm.build_map_mat()
    num_nodes=len(g.nodes())
    shortest_path_matrix=np.empty((num_nodes,num_nodes))
    shortest_path=nx.shortest_path_length(g,weight='weight')
    path=nx.shortest_path(g,weight='weight')
    prob_edge=nx.get_edge_attributes(g,'prob')
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
            
            #初始化相对概率
            fail_matrix[i][j]=(1-network_complity_pro)*(fail_matrix[i][j]/sum_pro)
        path_matrix[i]=temp_dict
    min_max_f=0
    min_max_p=0
    min_max_f_pro=0
    min_max_p_pro=0
    min_max_f_list=[]
    min_max_p_list=[]
    min_max_f_dict={}
    min_max_p_dict={}
    for node in g.nodes():
        if shortest_path_matrix[node][assigment_nodetocontroller_p[node]]>min_max_p:
            min_max_p=shortest_path_matrix[node][assigment_nodetocontroller_p[node]]
        if shortest_path_matrix[node][assigment_nodetocontroller_f[node]]>min_max_f:
            min_max_f=shortest_path_matrix[node][assigment_nodetocontroller_f[node]]
    #print('network_complity_pro=',network_complity_pro)
    min_max_f_pro=min_max_f_pro+min_max_f*network_complity_pro
    min_max_p_pro=min_max_p_pro+min_max_p*network_complity_pro
    #for i in range(int(network_complity_pro*n)):
     #   min_max_f_list.append(min_max_f)
      #  min_max_p_list.append(min_max_p)
    #print('min_max_p=',min_max_p)
    min_max_f_list.append(min_max_f)
    min_max_p_list.append(min_max_p)
    min_max_f_list.append(longesttime)
    min_max_p_list.append(longesttime)
    min_max_f_dict[min_max_f]=network_complity_pro
    min_max_p_dict[min_max_p]=network_complity_pro
    min_max_f_dict[longesttime]=0
    min_max_p_dict[longesttime]=0
    for edge in g.edges():
            temp_weight=g[edge[0]][edge[1]]['weight']
            
            #print(nx.shortest_path(G, source=edge[0],target=edge[1], weight='weight'))
            edge1=str(edge[0])+'+'+str(edge[1])
            edge2=str(edge[1])+'+'+str(edge[0])
            fail_max_length_f=min_max_f
            fail_max_length_p=min_max_p
            for i in g.nodes():
                if edge1 in path_matrix[i][assigment_nodetocontroller_p[i]] or edge2 in path_matrix[i][assigment_nodetocontroller_p[i]]:
                    g[edge[0]][edge[1]]['weight']=float('inf')
                    temp_length_p=nx.shortest_path_length(g,source=i,target=assigment_nodetocontroller_p[i],weight='weight')
                    if temp_length_p>fail_max_length_p:
                        fail_max_length_p=temp_length_p    
                    if(fail_max_length_p==float('inf')):                        
                        break
            if fail_max_length_p==float('inf'):
                #print('NO')
                min_max_p_pro=min_max_p_pro+(longesttime)*fail_matrix[edge[0]][edge[1]]
                min_max_p_dict[longesttime]=min_max_p_dict[longesttime]+fail_matrix[edge[0]][edge[1]]
                
            else:
                min_max_p_pro=min_max_p_pro+fail_max_length_p*fail_matrix[edge[0]][edge[1]]
                if fail_max_length_p in min_max_p_list:
                     min_max_p_dict[fail_max_length_p]=min_max_p_dict[fail_max_length_p]+fail_matrix[edge[0]][edge[1]]
                else:
                     min_max_p_list.append(fail_max_length_p)
                     min_max_p_dict[fail_max_length_p]=fail_matrix[edge[0]][edge[1]]
            g[edge[0]][edge[1]]['weight']=temp_weight
            for i in range(num_nodes):
                if edge1 in path_matrix[i][assigment_nodetocontroller_f[i]] or edge2 in path_matrix[i][assigment_nodetocontroller_f[i]]:
                    g[edge[0]][edge[1]]['weight']=temp_weight
                    orign_length=nx.shortest_path_length(g,source=i,target=assigment_nodetocontroller_f[i],weight='weight')
                    g[edge[0]][edge[1]]['weight']=float('inf')
                    temp_length_f=nx.shortest_path_length(g,source=i,target=assigment_nodetocontroller_f[i],weight='weight')
                    if temp_length_f>fail_max_length_f:
                        fail_max_length_f=temp_length_f    
                    if(fail_max_length_f==float('inf')):
                        break
            if(fail_max_length_f==float('inf')):
                min_max_f_pro=min_max_f_pro+(longesttime)*fail_matrix[edge[0]][edge[1]]
                min_max_f_dict[longesttime]=min_max_f_dict[longesttime]+fail_matrix[edge[0]][edge[1]]
                
            else:
                min_max_f_pro=min_max_f_pro+fail_max_length_f*fail_matrix[edge[0]][edge[1]]
                if fail_max_length_f in min_max_f_list:
                     min_max_f_dict[fail_max_length_f]=min_max_f_dict[fail_max_length_f]+fail_matrix[edge[0]][edge[1]]
                else:
                     min_max_f_list.append(fail_max_length_f)
                     min_max_f_dict[fail_max_length_f]=fail_matrix[edge[0]][edge[1]]
            g[edge[0]][edge[1]]['weight']=temp_weight
    print('min_max_f_pro=',min_max_f_pro)
    print('min_max_p_pro=',min_max_p_pro)
    plt.figure()
    for node in final_pos_p:
        nx.draw_networkx(g,pos,nodelist=assigment_p[node],node_size= 150,node_color=bmm.color[final_pos_p.index(node)%len(bmm.color)])
        nx.draw_networkx(g,pos,nodelist=[node],node_size= 600,node_color=bmm.color[final_pos_p.index(node)%len(bmm.color)])    
    plt.figure()    
    for node in final_pos_f:
        nx.draw_networkx(g,pos,nodelist=assigment_f[node],node_size= 150,node_color=bmm.color[final_pos_f.index(node)%len(bmm.color)])
        nx.draw_networkx(g,pos,nodelist=[node],node_size= 600,node_color=bmm.color[final_pos_f.index(node)%len(bmm.color)])
    
    plt.figure()
    print('min_max_f_list=',min_max_f_list)
    print('min_max_f_dict=',min_max_f_dict)
    print('min_max_p_list=',min_max_p_list)
    print('min_max_p_dict=',min_max_p_dict)
    min_max_f_list.sort()
    min_max_p_list.sort()
    y=[]
    y2=[]
    for num in min_max_f_list:
        #print(min_max_f_dict[num])
        y.append(min_max_f_dict[num])
    for num in min_max_p_list:
        y2.append(min_max_p_dict[num])
    
    
    plt.plot(min_max_f_list,y)
    plt.plot(min_max_p_list,y2)
    #nn1, bins1, patches1=plt.hist(min_max_f_list, normed=True,histtype='step', cumulative=True)
    #print('nn1=',nn)
    #print('bins1=',bins)
    #print('patches1=',patches)
    #plt.ylim(0, 1.1)
    plt.show()
        
if __name__=="__main__":
    main()