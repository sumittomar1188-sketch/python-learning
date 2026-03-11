# sets is a unoderd collection of item every set element is unique 
# key points 
# 1) orderd - means 3,2,1 = 1,2,3
# 2) mutable - means chanfges are allowed like lists unlike tuples 
# 3) no duplicates = no duplicate value contain 
# 4) can't contain mutubale data TYPE matlab ki apan usme koi mutable data type use nahi kar sakta 
# par vo khud hi ek mutable data type he 

# =========== how to create a set =======================
# isme ham use to {} iska karte he par by default to ye dictionary he to ham empty ke liye 
# empty set
s1 = set() # isme ham {ye} lete to ye dic bata ta 
print(type (s1))
# 1D set
s2 = {1,2,3,4}
print(s2)
# 2d set is not possible kyuki set mutable data type ko support nahi kar sakta 
# homogenus sets
s3 = {"sumit","ankit","naresh"}
print(s3) # ye aage pichhe print hogi kyuki isme hashing aka use hota he 
# hashinng means ki vo ye dekhta he konsi jgh kisko di jae
# heterogenus 
s4 = {1,2.3,"sumit", True} 
print(s4) # ye true nahi print karega kyuki do not repeat any value

# type concversion allow apan ek list ko set me change karenge 
s5 = set([1,23,45,66])
print(s5) # it is change in set 

# unoders proof ki ye unoderd hota he 
set1 = {1,2,3}
set2 = {3,2,1}
print(set1 == set2 ) #it prints true kyuki ye unoderd hota he or list or tuple odered hote he 