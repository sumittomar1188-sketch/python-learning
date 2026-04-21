class Securityerror (Exception) :
    def __init__(self,message):
        print(message)
    def logout (self):
        print("logout 🚫 ")    
class google :
    def __init__(self,name,password,device):
        self.name = name
        self.password = password
        self.device = device

    def login(self,password,device):
        if device != self.device :
            raise Securityerror ("☠️  bhai koi hack karne ki koshish kar rha he") 
        if password == self.password and device == self.device:
            print("welcome to the virtual world")
        else :
            print("kuchh to gadbad he syd pass galat he ") 


obj = google("sumit","222","windows")
try :
    obj.login("222","mac")
except Securityerror as e :  
    e.logout()

else :
    print(obj.name) 

finally :
    print("maja aagya data base me store ho gya hu ")    


