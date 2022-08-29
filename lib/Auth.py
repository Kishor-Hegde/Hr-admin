from genericpath import exists
import urllib.request,json,threading
# from cryptography.fernet import Fernet

# def encrypt(message: bytes, key: bytes):
#     return Fernet(key).encrypt(message)

# def decrypt(token: bytes, key: bytes):
#     return Fernet(key).decrypt(token)

def fetch(link):
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        return data

def setNewToken(token):
    with open('.techtok4u','w') as file:
        file.write(token)
def getToken()->str:
    if(exists('.techtok4u')):
        with open('.techtok4u','r') as file:
            return file.read()

def AuthenticateUser(username,password,callback=None):
    def get():
        try:
            data=fetch(f"https://cakehouse.co.in/hr-management/apis/main.php?username={username}&password={password}")
            sucess='status' in data.keys() and data['status']
            if(sucess):
                setNewToken(data['token'])
                if(callback):callback(sucess)
        except:
            print('--implement the new thread access to tlc widndow')
    threading.Thread(target=get).start()
    