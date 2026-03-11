# in a tuple we can assign each value for each variable 
# ==== tuple unpacking =============
a,b,c = (1,2,3)
print(a,b,c)

# 3 agar ham iski jgh ye likhe ki 
# print(a,b)  isme to ye error aaega 

# =========== operationn in tuple ============= 
# +, - * 

t = (1,2,3,4,5)
a = t
print(t*2)
t = t+(3,) # ye ek tuple ban chuka he isliye ye add hua 
print(t)
# but a me changes nahi honge yahi iski khasiyat he  par list me ho jate he 
print(a)

# python me swap ka option bhi hota hge eadily 
a = 2 
b = 3 
a,b = b,a
print(a,b)


# now ab ham kisi ko agar axis karna he to jese tuple me se sird do elemnt ko hi
a,b,*others = (2,3,4,5)
print(a,b) # it is alow but in simple way without * it is not allow 
print (others)


#zip funition ek value deta he usko kisi me change karna padta he either list or tuple 
t1 = (1,2,3,4,5)
t2 = (3,6,8,7,9)
print (zip(t1,t2)) # ye sirf ek value dega baki fir uski list tuple me change karenge 
print (tuple(zip(t1,t2)))#or isko list me bhi de sakte he 
print(t1)