from src.Home import Home
from lib.Auth import AuthenticateUser
from lib.ImageAsset import resource
from lib.ScreenShot import takeScreenShot
from tkinter import *



class Login():
    def __init__(self,parent:Tk ):
            
        self.root=Frame(parent,width=1000,height=700,bg='white')
        self.root.grid(row=0,column=0)
        self.parent=parent
        parent.title('Login')
        parent.geometry('1000x700+300+200')
        parent.configure(bg="#fff")
        parent.resizable(False,False)

        logo=Frame(self.root,bg='blue',width=350,height=500)
        logo.place(x=100,y=150)
        global logoimg
        logoimg=PhotoImage(file=resource("./assets/logo.png"))
        
        Label(logo,image=logoimg,bg='white').grid(column=0,row=0)

        frame=Frame(self.root,width=350,height=500,bg='white')
        frame.place(x=580,y=100)
        heading=Label(frame,text='Sign in',fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=20)

        def on_enter(e):
            self.user.delete(0,'end')    

        def on_leave(e):
            name=self.user.get()
            if name=='':
                self.user.insert(0,'username')
                
        self.user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
        self.user.place(x=30,y=150)
        self.user.insert(0,'username')
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)
        Frame(frame,width=295,height=2,bg='black').place(x=25,y=180)



        def on_enter(e):
            self.code.delete(0,'end')

        def on_leave(e):
            name=self.code.get()
            if name=='':
                self.code.insert(0,'Password')
        self.code= Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',12))
        self.code.place(x=30,y=250)
        self.code.insert(0,'Password')
        self.code.bind('<FocusIn>', on_enter)
        self.code.bind('<FocusOut>', on_leave)
        Frame(frame,width=295,height=2,bg='black').place(x=25,y=284)
        Button(frame,width=37,pady=7,text='Sign in',bg='#57a1f8', fg='white', border=0,command=self.signin).place (x=24,y=400) 

    def forget(self):
        self.root.destroy()
    def signin(self):
        username=self.user.get()
        password=self.code.get()
        #implement basic email and password validation here
        def Show(status):
            self.root.destroy()
            if(status):Home(self.parent)

        AuthenticateUser(username,password,Show)

