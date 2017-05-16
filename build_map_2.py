
import matplotlib.pyplot as plt
import networkx as nx
import  pickle
def build_map():
    G=nx.Graph()
    prob = pickle.load(open("tmp.txt", "rb"))
    G.add_node(0,x=312,y=117)
    G.add_node(1,x=315,y=185)
    G.add_node(2,x=265,y=229)
    G.add_node(3,x=121,y=283)
    G.add_node(4,x=214,y=281)
    G.add_node(5,x=121,y=352)
    G.add_node(6,x=217,y=351)
    G.add_node(7,x=312,y=349)
    G.add_node(8,x=378,y=385)
    G.add_node(9,x=313,y=528)
    G.add_node(10,x=640,y=526)
    G.add_node(11,x=640,y=425)
    G.add_node(12,x=640,y=353)
    G.add_node(13,x=556,y=350)
    G.add_node(14,x=464,y=300)
    G.add_node(15,x=400,y=228)
    G.add_node(16,x=359,y=187)
    G.add_node(17,x=538,y=117)
    G.add_node(18,x=619,y=117)
    G.add_node(19,x=702,y=114)
    G.add_node(20,x=595,y=192)
    
    G.add_edge(0,1,weight=124.7)
    G.add_edge(1,2,weight=626.2)
    G.add_edge(2,4,weight=433.4)
    G.add_edge(3,4,weight=491.4)
    G.add_edge(4,5,weight=616.6)
    G.add_edge(5,6,weight=253.3)
    G.add_edge(6,7,weight=736.7)
    G.add_edge(7,8,weight=289.5)
    G.add_edge(1,7,weight=1040.6)
    G.add_edge(7,9,weight=840.4)
    G.add_edge(9,10,weight=500.6)
    G.add_edge(10,11,weight=669)
    G.add_edge(11,12,weight=154.7)
    G.add_edge(12,13,weight=266.6)
    G.add_edge(13,14,weight=150.6)
    G.add_edge(13,7,weight=462.1)
    G.add_edge(14,15,weight=542.8)
    G.add_edge(15,16,weight=275.6)
    G.add_edge(16,1,weight=117.1)
    G.add_edge(1,17,weight=592.1)
    G.add_edge(17,18,weight=267.8)
    G.add_edge(18,19,weight=241)
    G.add_edge(17,20,weight=356.3)
    
    edges=G.edges()
    dict1={}
    dict3={}
    i=0
    for edge in edges:
           G[edge[0]][edge[1]]['weight']=G[edge[0]][edge[1]]['weight']/(3*10**2)
           list_=[]
           list_.insert(0,edge[0])
           list_.insert(1,edge[1])
           tup=tuple(list_)
           dict1[tup]=prob[i]
           dict3[tup]=G[edge[0]][edge[1]]['weight']/prob[i]
           i=i+1
    
    nx.set_edge_attributes(G, 'prob', dict1)
    nx.set_edge_attributes(G, 'distance', dict3)
    
        
    pos={}
    nodes=G.nodes()
    for node in nodes:
        list_=[]
        list_.insert(0,G.node[node]['x'])
        list_.insert(1,600-G.node[node]['y'])
        tup=tuple(list_)
        pos[node]=tup
    G[0][1]['prob']=1
    G[17][1]['prob']=1
    G[17][18]['prob']=1
    G[18][19]['prob']=1
    G[17][20]['prob']=1
    G[3][4]['prob']=1
    G[7][8]['prob']=1
            
    return G,pos

def main():
    #colorlist=
    nodedict1={} 
    pos={}
    g,pos=build_map()
    print(nodedict1)
    
    
    nx.draw_networkx(g,pos,node_size=50,font_size=20)
    plt.show()
    print(len(g.nodes()))
    print(g.nodes())
    print(len(g.edges()))
   


if __name__=="__main__":
    main()

