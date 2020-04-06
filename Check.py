import os
import easygui as gui
import Name as n
Total = 0

Fall = set()
Good = set()
CheckTwoCode = set()
openbox = gui.diropenbox('请选择检查的路径','作业管理系统')
for i in os.listdir(openbox):
    for li in n.Name:
        if(i.find(li) !=-1):
            Total+=1
            Good.add(li)
            break
        else:
            Fall.add(li)


