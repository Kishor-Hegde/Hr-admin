import datetime,threading,pyautogui


def takeScreenShot(intervel):
    if not threading.main_thread().is_alive() : exit()
    threading.Timer(intervel,takeScreenShot,args=[intervel]).start()
    current = datetime.datetime.now()
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'{current.date()}_{str(current.time()).replace(":","-")}.png')
