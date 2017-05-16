import numpy as np
import matplotlib.pyplot as plt
import  pickle
import numpy as np
from scipy.stats import dweibull


import  pickle
data = pickle.load(open("222.txt", "rb"))
data_su = pickle.load(open("2su.txt", "rb"))

x=[]
y_p=[]
y_f=[]
y_g=[]
y_a=[]
y_s=[]
    #plt.figure()
m=5
x = np.arange(m)
for times in range(m):
    k=times+1
    #x1.append(k)
    y_p.append(data['dict_runtime_p'][k])
    #y_f.append(data['dict_runtime_f'][k])
    y_g.append(data['dict_runtime_g'][k])
    y_a.append(data['dict_runtime_a'][k])
    y_s.append(data_su['dict_runtime_s'][k])
#plt.style.use('ggplot')
print('y_p=',y_p)
print('y_g=',y_g)
print('y_a=',y_a)
print('p/g=',[X/y for X,y in zip(y_p,y_g)])
print('p/a=',[X/y for X,y in zip(y_p,y_a)])
fig, ax = plt.subplots()
width=0.2
#ba1=ax.bar(x, y_a, width,color=plt.rcParams['axes.color_cycle'][1],hatch='\\')
ba2=ax.bar(x, y_g, width, color=plt.rcParams['axes.color_cycle'][2],hatch='//')
ba3=ax.bar(x+width, y_p, width, color=plt.rcParams['axes.color_cycle'][3],hatch='.')
ax.set_xticks(x+width)
ax.set_xticklabels(x+1)
plt.ylabel('runtime(s)', fontsize=18)
plt.xlabel('number of controller(k)', fontsize=18)
#plt.ylim(-0.2)
#plt.xlim(1,m+0.3,1)
ax.legend( (ba3[0],ba2[0]), ('NSFT','CIP'),loc=2 )

plt.savefig('./pic/cernet/runtime1.eps',format="eps")

fig, ax = plt.subplots()
width=0.2
ba1=ax.bar(x+width, y_a, width,color=plt.rcParams['axes.color_cycle'][1],hatch='\\')
ba2=ax.bar(x, y_g, width, color=plt.rcParams['axes.color_cycle'][2],hatch='//')
ba3=ax.bar(x+2*width, y_s, width, color=plt.rcParams['axes.color_cycle'][5],hatch='*')
#ba3=ax.bar(x+2*width, y_p, width, color=plt.rcParams['axes.color_cycle'][3],hatch='.')
ax.set_xticks(x+width)
ax.set_xticklabels(x+1)
plt.ylabel('runtime(s)', fontsize=18)
plt.xlabel('number of controller(k)', fontsize=18)
#plt.ylim(-0.2)
#plt.xlim(1,m+0.3,1)
ax.legend( (ba2[0],ba1[0],ba3[0]), ('CIP','INS','INB'),loc=2 )

plt.savefig('./pic/cernet/runtime2.eps',format="eps")
prob_py=[]
prob_gy=[]
prob_ay=[]
prob_sy=[]
for times in range(m):
   k=times+1
   prob_py.append(data['dict_pro_p'][k])
   prob_gy.append(data['dict_pro_g'][k])
   prob_ay.append(data['dict_pro_a'][k])
   prob_sy.append(data_su['dict_pro_s'][k])
#print('prob_py=',prob_py)
#print('prob_gy=',prob_gy)
#print('prob_ay=',prob_ay)
#print('g-p=',[(g-p)/g for g, p in zip(prob_gy, prob_py)])
#print('a-p=',[(a-p)/a for a, p in zip(prob_ay, prob_py)])
#plt.figure()
fig2,ax2=plt.subplots()

ba4=ax2.bar(x+3*width, prob_sy, width,color=plt.rcParams['axes.color_cycle'][5],hatch='*')
ba1=ax2.bar(x+2*width, prob_ay, width,color=plt.rcParams['axes.color_cycle'][1],hatch='\\')
ba2=ax2.bar(x+width, prob_gy, width, color=plt.rcParams['axes.color_cycle'][2],hatch='//')
ba3=ax2.bar(x, prob_py, width, color=plt.rcParams['axes.color_cycle'][3],hatch='.')
ax2.set_xticks(x+2*width)
ax2.set_xticklabels(x+1)
plt.ylabel('network state latency(ms)', fontsize=18)
plt.xlabel('number of controller(k)', fontsize=18)
#plt.ylim(-0.2)
#plt.xlim(1,m+0.3,1)
ax2.legend( (ba3[0], ba2[0],ba1[0],ba4[0]), ('NSFT','CIP','INS','INB'),loc=1,fontsize=10 )
plt.savefig('./pic/cernet/Worst_case_latency.eps',format="eps")

de_prob_p=[]
de_prob_g=[]
de_prob_a=[]
de_prob_s=[]

for times in range(m):
    k=times+1
    de_prob_p.append((data['dict_pro_p'][1]/data['dict_pro_p'][k])/k)
    de_prob_g.append((data['dict_pro_g'][1]/data['dict_pro_g'][k])/k)
    de_prob_a.append((data['dict_pro_a'][1]/data['dict_pro_a'][k])/k)
    de_prob_s.append((data_su['dict_pro_s'][1]/data_su['dict_pro_s'][k])/k)
print('de_prob_p=',de_prob_p)
print('de_prob_g=',de_prob_g)
print('de_prob_a=',de_prob_a)
fig3,ax3=plt.subplots()
ba1=ax3.bar(x, de_prob_p, width, color=plt.rcParams['axes.color_cycle'][3],hatch='.')
ba2=ax3.bar(x+width, de_prob_g, width, color=plt.rcParams['axes.color_cycle'][2],hatch='//')
ba3=ax3.bar(x+2*width, de_prob_a, width,color=plt.rcParams['axes.color_cycle'][1],hatch='\\')
ba4=ax3.bar(x+3*width, de_prob_s, width,color=plt.rcParams['axes.color_cycle'][5],hatch='*')
ax3.set_xticks(x+2*width)
ax3.set_xticklabels(x+1)
plt.ylabel('cost-benefit ratios',fontsize=18)
plt.xlabel('number of controller(k)',fontsize=18)
ax3.legend( (ba1[0], ba2[0],ba3[0],ba4[0]), ('NSFT','CIP','INS','INB'),loc=1 )   
plt.savefig('./pic/cernet/Cost-benefit-ratios.eps',format="eps")


for times in range(m):
    k=times+1
    list_p=data['dict_list_p'][k]
    list_f=data['dict_list_f'][k]
    list_g=data['dict_list_g'][k]
    list_a=data['dict_list_a'][k]
    list_s=data_su['dict_list_s'][k]
    list_p.sort()
    list_g.sort()
    list_a.sort()
    list_s.sort()
    list_py=[]
    list_gy=[]
    list_ay=[]
    list_sy=[]
    list_x=[]
    list_y=[]
    list_x.extend(list_p)
    list_x.extend(list_g)
    list_x.extend(list_a)
    list_x.extend(list_s)
    
    for node in list_p:
        list_py.append(data['dict_dict_p'][k][node])
    for node in list_g:
        list_gy.append(data['dict_dict_g'][k][node])
    for node in list_a:
        list_ay.append(data['dict_dict_a'][k][node])
    for node in list_s:
        list_sy.append(data_su['dict_dict_s'][k][node])
    list_y.extend(list_py)
    list_y.extend(list_gy)
    list_y.extend(list_ay)
    list_y.extend(list_sy)
    maxx=max(list_x)
    minx=min(list_x)
    miny=min(list_y)
    maxy=max(list_y)
    list_pyy=[]
    list_gyy=[]
    list_ayy=[]
    list_syy=[]
    nun=0
    for numy in list_py:
        nun=nun+numy
        list_pyy.append(nun)
    nun=0
    for numy in list_gy:
        nun=nun+numy
        list_gyy.append(nun)
    nun=0
    for numy in list_ay:
        nun=nun+numy
        list_ayy.append(nun)
    nun=0
    for numy in list_sy:
        nun=nun+numy
        list_syy.append(nun)
        
    #if k==3:
     #   print('list_p=',list_p)
      #  print('list_py=',list_py)
       # print('list_g=',list_g)
        #print('list_gy=',list_gy)
        #print('list_a=',list_a)
        #print('list_ay=',list_ay)
        #sum=0
       # for node in list_p:
        #    if node<10:
         #       sum=sum+data['dict_dict_p'][k][node]
        #print('sum=',sum)
    fig, ax = plt.subplots()
    L1=ax.plot(list_p,list_pyy,'o-',color=plt.rcParams['axes.color_cycle'][3])
#ax.plot(x,y_f,'*-')

    L2=ax.plot(list_g,list_gyy,'s-',color=plt.rcParams['axes.color_cycle'][2])
    L3=ax.plot(list_a,list_ayy,'v-',color=plt.rcParams['axes.color_cycle'][1])
    L4=ax.plot(list_s,list_syy,'*-',color=plt.rcParams['axes.color_cycle'][5])
    ax.legend( (L1[0],L2[0],L3[0],L4[0]), ('NSFT','CIP','INS','INB'),loc=2,fontsize=10 )
    ax.set_ylabel('cumulative distribution', fontsize=18)
    ax.set_xlabel('worst case latency(ms)', fontsize=18)
    
    
    
    plt.savefig('./pic/cernet/latency-distribution-k='+str(k)+".eps",format="eps")
plt.show()

