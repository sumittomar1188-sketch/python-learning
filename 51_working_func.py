# how function works ?
''' answewr - when we declare function and run the program during execution the function makes jump to outside the function
and ignore inner items ko ignore kar dega fir jab usko call kiya jaega to firse vo function par jaega or 
ineer item ko execute karega ---- kets take an example
 '''
# local and global variable 
# global -  global are those variable which comes under he program scop 
# local- local are those variable which comes under function scope 
# example 
def g(y):  # y is a local variable jo ki sirf function ke andar hi kam karega 
    print(x)
    print(x+1)
    

x = 5 # global variable isko function use kar sakta he apne execution time par 
g(x)    # yha par function g ko call kara usko x variable diya jo ki arrgument of parameter he 
  # function global ko use kar sakta he lekin 
print(y)