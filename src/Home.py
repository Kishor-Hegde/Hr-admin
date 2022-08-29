from tkinter import *
from lib.ScreenShot import takeScreenShot

class Home():
    def __init__(self,parent:Tk):
        self.parent=parent
        parent.title('Home')
        parent.geometry('1000x700+300+200')
        parent.configure(bg="#fff")
        parent.resizable(False,False)
        Label(self.parent,text='Employee App',bg='white',font=('Microsoft YaHei UI Light',23,'bold')).pack()
        
        self.butt=Button(self.parent,text='start work',width=37,pady=7,bg='#57a1f8', fg='white',font=('Microsoft YaHei UI Light',10,'bold'), border=0,command=self.Run)
        Frame(self.parent,height=300,bg="#fff").pack()
        self.butt.pack()
    def Run(self):
        self.butt.destroy()
        Label(self.parent,text='Your work have been started and attendence have be marked',font=('Microsoft YaHei UI Light',12,'bold'),bg='white').pack()
        Label(self.parent,text='Close this application only after you finish the job',font=('Microsoft YaHei UI Light',10),bg='white').pack()
        takeScreenShot(10)



