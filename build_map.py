import xlrd
import matplotlib.pyplot as plt
import networkx as nx
def build_map():
    G=nx.Graph()
    data = xlrd.open_workbook('router_all.xls')
    table1 = data.sheets()[1]
    table0 = data.sheets()[0]
    nrows0 = table0.nrows
    nrows1 = table1.nrows
    nodedict={}
    for rownum1 in range(1,nrows1):
        cell=table1.cell(rownum1,0).value.strip().upper()
        nodedict[cell]=rownum1+1;
        G.add_node(cell)
        G.node[cell]['x']=table1.cell(rownum1,2).value
        G.node[cell]['y']=table1.cell(rownum1,3).value
    print(len(G.nodes()))
    for rownum0 in range(1,nrows0):
        cell = table0.cell(rownum0,1).value.strip()
        content = cell.split('-')
        #if '2001:DA8:10:301::1' in content:
        #    print('0000000000')
        if content[0] in G.nodes():
            if content[1] in G.nodes():
                
                G.add_edge(content[0],content[1])
        else: 
            continue
        
    pos={}
    nodes=G.nodes()
    for node in nodes:
        list_=[]
        list_.insert(0,G.node[node]['y'])
        list_.insert(1,G.node[node]['x'])
        tup=tuple(list_)
        pos[node]=tup
            
    return G,nodedict,pos

def main():
    #colorlist=
    nodedict1={} 
    pos={}
    g,nodedict1,pos=build_map()
    print(nodedict1)
    
    
    nx.draw_networkx(g,pos,node_size=50,labels=nodedict1,font_size=20)
    print(len(g.nodes()))
    print(g.nodes())
    print(len(g.edges()))
   


if __name__=="__main__":
    main()

