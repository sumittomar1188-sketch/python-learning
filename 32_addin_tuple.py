# Adding in tuple 
# it is not possible


#  === deletion in tuple ========
# isme ham tuple ko pura delte kar sakte he par sief ek portion nahi lets take examples 
t1 = (1,2,3,4,5,6)
print(t1)
del t1   # ye delete kar dega 
# print (t1) # ye print nahi hoga ab kyuki delte ho chuka he 


# now take example of how a part is not delted from tuple 
t2 = (4,45,565,64)
# del t2 [0]
# print(t2) # showing an error tuples doews no suppo deletion 



# ================== function =====================
# len/sort/sum/min/max 
t3 = (2,3,6,5)
print(len(t3))
print(max(t3))
print(min(t3))
print(sorted(t3)) # ascending order 
print(sorted(t3),reversed = True)