import os
import easygui as gui
from HomeWorkSystem import Name as n

Total = 0

Fall = []
Good = []
openbox = gui.diropenbox('请选择检查的路径','作业管理系统')
for i in n.Name:
    Fall.append(i)
    Total+=1
try:
    for z in os.listdir(openbox):
        for p in n.Name:
            if(z.find(p) !=-1):
                Fall.remove(p)
                Total-=1
                Good.append(p)
except:
    print("检查一下是不是有个同学的作业重复了")
print(len(Fall))
Sum = len(n.Name) - Total