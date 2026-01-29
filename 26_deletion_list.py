# there are 4 ways of deletion 
# del / remove / pop / clear 

# del
p = [1,2,3,4,5]
print (p) 
del p # issse puri list ko delete kar dega 
# print (p)  isko agar chalegnge to error aaega kyuki list to delete ho chuki he na 



p = [1,2,3,4,5]
# by index number del
del p[0]
# by slicing deletion 
del p[1:4]
print (p)  # isme sirf 2 aaega kyuki pehle 1 delete to 2 ka  index number 0 ho jaega 0 1 se 4 to sare elment cover ho jaenge 

# ================ remove ==================== 
q = [2,3,4,5,6,7]
q.remove(5)
print(q)#, ye particular element ko remove kar degi list me se index number ki koi jarurat nahi 

#============== pop ====================
r = [1,2,3,4,5,6,7]
r.pop() # generally it can be used for remove last elemnt from the list ye -1 let karega 
print(r)

# =============== clear ==================
# ye puri list koe sare element clear kar dega 
s = [1,23,4,5,6,7]
s.clear()
print(s)