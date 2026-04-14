# just like other languages 
# try -> try 
# exeption -> catch
# raise -> throw
# raise - raise ka kam hota he kahi par error raise karke exception ki trf fek dena jisse error asani se haldle ho jata he 
# lets take an example of bank 
class bank :
    def __init__(self,balance):
        self.balance = balance

    def withdraw (self,amount) :
        if amount <0 :
            raise Exception ("bhai ye to -ive nahi ho sakta")
        if self.balance <amount :
            raise Exception ("bhai itte paise nahi he mere pass")
        self.balance = self.balance- amount
obj = bank(10000)
try:
    obj.withdraw(-5000)

except Exception as e : # ye catch kar lega jo ki raise ne vha se throw kiya he 
    print(e) 

else:
    print(obj.balance)