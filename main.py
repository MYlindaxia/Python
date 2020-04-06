import easygui as gui
import CheckDemo
t = gui.buttonbox(msg="已经有:"+str(CheckDemo.Sum)+"交了作业\n还有:"+str(CheckDemo.Total)+"名同学没有交",title="MADE IN MYlindaxia",choices=('打印未交作业的同学','打印交了作业的同学'))
if(t=='打印未交作业的同学'):
    print("good")
    gui.msgbox(str(CheckDemo.Fall),title='作业管理系统')
else:
    print("bad")
    gui.msgbox(str(CheckDemo.Good),title="作业管理系统")