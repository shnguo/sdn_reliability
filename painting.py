import build_map_mat as bmm
import networkx as nx
import itertools
import numpy as np
import random
import calculate_pro as cp
import calculate_free as cf
import calculate_approximation as ca
import calculate_greed as cg
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
    dict_pro_p={}
    dict_pro_f={}
    dict_pro_g={}
    dict_pro_a={}
    dict_list_p={}
    dict_list_f={}
    dict_list_g={}
    dict_list_a={}
    dict_dict_p={}
    dict_dict_f={}
    dict_dict_g={}
    dict_dict_a={}
    dict_runtime_p={}
    dict_runtime_f={}
    dict_runtime_g={}
    dict_runtime_a={}
    data={}
    
    
    for times in range(m):
        k=times+1
        
        final_pos_p,assigment_p,assigment_nodetocontroller_p,runtime_p=cp.calculate_pro(g,pos,k)
        plt.figure()
        for node in final_pos_p:
            nx.draw_networkx(g,pos,nodelist=assigment_p[node],node_size= 300,node_color=bmm.color[final_pos_p.index(node)%len(bmm.color)])
            nx.draw_networkx(g,pos,nodelist=[node],node_size= 300,node_color=bmm.color[final_pos_p.index(node)%len(bmm.color)],node_shape=nodeshape[0])
        plt.axis('off')
        plt.savefig('./pic/topo/cp_k='+str(k)+".eps",format="eps")
        
        final_pos_f,assigment_f,assigment_nodetocontroller_f,runtime_f=cf.calculate_free(g,pos,k)
        plt.figure()
        for node in final_pos_f:
            nx.draw_networkx(g,pos,nodelist=assigment_f[node],node_size= 300,node_color=bmm.color[final_pos_f.index(node)%len(bmm.color)])
            nx.draw_networkx(g,pos,nodelist=[node],node_size= 300,node_color=bmm.color[final_pos_f.index(node)%len(bmm.color)],node_shape=nodeshape[0])    
        plt.axis('off')
        plt.savefig('./pic/topo/cf_k='+str(k)+".eps",format="eps")
        
        final_pos_g,assigment_g,assigment_nodetocontroller_g,runtime_g=cg.calculate_greed(g,pos,k)
        plt.figure()
        for node in final_pos_g:
            nx.draw_networkx(g,pos,nodelist=assigment_g[node],node_size= 300,node_color=bmm.color[final_pos_g.index(node)%len(bmm.color)])
            nx.draw_networkx(g,pos,nodelist=[node],node_size= 300,node_color=bmm.color[final_pos_g.index(node)%len(bmm.color)],node_shape=nodeshape[0])    
        plt.axis('off')
        plt.savefig('./pic/topo/cg_k='+str(k)+".eps",format="eps")
        
        final_pos_a,assigment_a,assigment_nodetocontroller_a,runtime_a=ca.calculate_approximation(g,pos,k)
        plt.figure()
        for node in final_pos_a:
            nx.draw_networkx(g,pos,nodelist=assigment_a[node],node_size= 300,node_color=bmm.color[final_pos_a.index(node)%len(bmm.color)])
            nx.draw_networkx(g,pos,nodelist=[node],node_size= 300,node_color=bmm.color[final_pos_a.index(node)%len(bmm.color)],node_shape=nodeshape[0])  
        plt.axis('off')
        plt.savefig('./pic/topo/ca_k='+str(k)+".eps",format="eps")
#        plt.show()
        pro_p,list_p,dict_p=nv.verification(g,pos,final_pos_p,assigment_p,assigment_nodetocontroller_p)
        pro_f,list_f,dict_f=nv.verification(g,pos,final_pos_f,assigment_f,assigment_nodetocontroller_f)
        pro_g,list_g,dict_g=nv.verification(g,pos,final_pos_g,assigment_g,assigment_nodetocontroller_g)
        pro_a,list_a,dict_a=nv.verification(g,pos,final_pos_a,assigment_a,assigment_nodetocontroller_a)
        dict_pro_p[k]=pro_p
        dict_pro_f[k]=pro_f
        dict_pro_g[k]=pro_g
        dict_pro_a[k]=pro_a
        dict_list_p[k]=list_p
        dict_list_f[k]=list_f
        dict_list_g[k]=list_g
        dict_list_a[k]=list_a
        dict_dict_p[k]=dict_p
        dict_dict_f[k]=dict_f
        dict_dict_g[k]=dict_g
        dict_dict_a[k]=dict_a
        dict_runtime_p[k]=runtime_p
        dict_runtime_f[k]=runtime_f
        dict_runtime_g[k]=runtime_g
        dict_runtime_a[k]=runtime_a
    data['dict_pro_p']= dict_pro_p
    data['dict_pro_f']= dict_pro_f
    data['dict_pro_g']= dict_pro_g
    data['dict_pro_a']= dict_pro_a
    data['dict_list_p']=dict_list_p
    data['dict_list_f']=dict_list_f
    data['dict_list_g']=dict_list_g
    data['dict_list_a']=dict_list_a
    data['dict_dict_p']=dict_dict_p
    data['dict_dict_f']=dict_dict_f
    data['dict_dict_g']=dict_dict_g
    data['dict_dict_a']=dict_dict_a
    data['dict_runtime_p']=dict_runtime_p
    data['dict_runtime_f']=dict_runtime_f
    data['dict_runtime_g']=dict_runtime_g
    data['dict_runtime_a']=dict_runtime_a
    
    pickle.dump(data, open("aaa.txt", "wb"))
    
        
        

if __name__=="__main__":
    main()