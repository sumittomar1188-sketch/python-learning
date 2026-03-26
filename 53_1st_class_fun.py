# function are first-class citizens in python 
# just likhe a list tuple int float all the data types we can use function as a data type 
def square (n):
    x = n **2
    return x
print(square(5))

a = square # isko ham as a data type value me store kara sakte he 
print(type(a))

l = [1,2,3,square]
# using idexing 
print(l[-1](4)) # isko 4 value de di to uska square bata dega ye 



# it is a imutable datatype - because isko ham set me put kar sakte he or set me ham mutable datatype nahi rakh sakte
s = {1,2,3,square}


# function as arrguments 

def fun_1 ():
    print("do you call func_1")

def func_2(z): 
    print("do you call func_2") 
    return z()

print(func_2(fun_1))     