import ctypes
import sys
from tkinter import *
from Home import Home
from lib.Auth import getToken
from login import Login
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def GetAdministratorPermission():ctypes.windll.shell32.ShellExecuteW(None,'runas',sys.executable," ".join(sys.argv),None,1)
def isAdmin(): return ctypes.windll.shell32.IsUserAnAdmin()

class App():
    def __init__(self):
        root=Tk()
        if((token:=getToken()) and len(token)==32):Home(root)
        else:Login(root)
        root.mainloop()


if __name__=='__main__':
        App()
  
