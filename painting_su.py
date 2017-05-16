import build_map_mat as bmm
import networkx as nx
import itertools
import numpy as np
import random
import calculate_pro as cp
import calculate_free as cf
import calculate_approximation as ca
import calculate_su as cs
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib.ticker import FuncFormatter
import matplotlib
import  pickle
import new_verification as nv
nodeshape = 'so^>v<dph8'
def main():
    g,pos=bmm.build_map_mat()
    m=5
    dict_pro_s={}
    
    dict_list_s={}
    
    dict_dict_s={}
    
    dict_runtime_s={}
    
    data={}
    
    
    for times in range(m):
        k=times
        
        final_pos_s,assigment_s,assigment_nodetocontroller_s,runtime_s=cs.calculate_su(g,pos,k)
        plt.figure()
        for node in final_pos_s:
            nx.draw_networkx(g,pos,nodelist=assigment_s[node],node_size= 300,node_color=bmm.color[final_pos_s.index(node)%len(bmm.color)])
            nx.draw_networkx(g,pos,nodelist=[node],node_size= 300,node_color=bmm.color[final_pos_s.index(node)%len(bmm.color)],node_shape=nodeshape[0])
        plt.axis('off')
        plt.savefig('./pic/topo/cp_s='+str(k)+".eps",format="eps")
        
       
        pro_s,list_s,dict_s=nv.verification(g,pos,final_pos_s,assigment_s,assigment_nodetocontroller_s)
        
        dict_pro_s[k+1]=pro_s
        
        dict_list_s[k+1]=list_s
        
        dict_dict_s[k+1]=dict_s
        
        dict_runtime_s[k+1]=runtime_s
        
    data['dict_pro_s']= dict_pro_s
    
    data['dict_list_s']=dict_list_s
    
    data['dict_dict_s']=dict_dict_s
    
    data['dict_runtime_s']=dict_runtime_s
    plt.show()
    
    pickle.dump(data, open("su.txt", "wb"))
    
        
        

if __name__=="__main__":
    main()