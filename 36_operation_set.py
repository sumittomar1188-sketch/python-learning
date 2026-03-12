# ================= sets operation ======================


#==================== uniion (|) =======================
# union - isme dono ka mix ho jaega 
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1|s2) # but repeat value nahi print karega ye 



#================== intersection (&) =====================
# intersection - isme dono ka common print ho jaega 
print(s1&s2)



# ================= differnce (-) ==================
# difference - isme jo diffrent he unko print karega 
print(s1-s2) # par jo aage likhja rahega usi set ka sirf value lega 
print(s2-s1) # isme sirf s2 ko lega or common nahi print karega 



# ================== symmetrical set(^) ====================              
# symmetrical - isme dono sets me se common ko chhod ke sare elements ko print kar dega 
print(s1^s2)
