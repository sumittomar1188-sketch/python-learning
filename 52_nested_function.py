# function are allowed nested function 
def f():
    def g():
        print("fucntion of g ")
    g()
    print("function of f ")   

# g() - we cannot directly acces nested function directly
f()

# note - :  nested function me se hm directly program me usko use nahi kar sakte usko main function ke andar hi likhna hoga 

def s():
    def h():
        print("fucntion of h")
        s()
    h()
    print("function of s ")  

s()    # isme ek infintte loop aa jaega kyuki vo andar hi bar bar s ko call karega or s h ko call karega 
