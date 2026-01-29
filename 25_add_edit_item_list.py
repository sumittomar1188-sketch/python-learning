# =============== adding ===================
# adding items in list 
# append by the use of it we can add the item at the end of the list but it can only add onle single unit 
s =  ["sumit",2,2.5,2+2j,True]
s.append(2)
print(s)

# example 
s.append([2,3,4]) # to ye puri list ko hi print kar dega 
print(s)

# =============== extend =======================
l = ["sumit",2,2.5,2+2j,True]
l.extend([1,23,4]) # to ye sabko print kar dega sirf ek ko nahi or puri list ko alag alag kar dega fir extend karega 
print(l)

n = ["sumit",2,2.5,2+2j,True]
n.extend("betu") # ye puri string ko alag alg tod dega fir extend karega 
print(n)

# ===================== insert ==============================

t = ["sumit",2,2.5,2+2j,True]
t.insert(1,100) # ye  sumit ko 1 let kar lega isme fir vo 1 ke bad insert ho jaega 
print(t)


# ============= editing ===============
# in editing we can use particular index or slice to change that item here ae example 
l1 = [1,2,3,4,5,6,7]
l1[6] = 200 
print(l1) # here the 7th item are changed to 200 
l1[1:6] = 300,400,500,600
print(l1)