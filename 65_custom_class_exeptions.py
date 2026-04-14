# python allows us to make own error means exeption jisse ki full control aa ajata he ek example lete he pichhle wale ke jesa
class myExeption(Exception):
    def __init__(self,message):
        print(message)

class bank :
    def __init__(self,balance):
        self.balance = balance

    def withdraw (self,amount) :
        if amount <0 :
            raise myExeption ("bhai ye to -ive nahi ho sakta") # yha hamne exeption use kiya tha ab my exeption karrnge
        if self.balance <amount :
            raise myExeption("bhai itte paise nahi he mere pass")
        self.balance = self.balance- amount
obj = bank(10000)
try:
    obj.withdraw(15000)

except myExeption as e : # ye catch kar lega jo ki raise ne vha se throw kiya he 
    pass

else:
    print(obj.balance)