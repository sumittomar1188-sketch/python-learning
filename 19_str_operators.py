# operation on strings
# =============arithmetic operation===================
print ("delhi" +" " + "mumbai")
print("delhi "*5)


# ===============relational operaton=================
# all relation operators are applicable
print("mumbai"=="delhi") # it gives us false
print("delhi"!="delhi") # also false
print("mumbai"> "pune")
# lexiiographically - mean ek dictonary me vo mumbai pahle aata hoga
print("Pune">"pune") # isme bhi false kyu ki capital P ki askii value small p se chhoti hoti he 



# ==================logical operator===========================
print("sumit" and "tomar")
print("sumit" or "tomar")
'''isme ek concept he ye ki in a string any char value is given then its is asumed as true and if empty string assume as false'''


# ==================loop operation=========================
for i in  "sumit":
    print(i)
for i in "sumit":
    print("tomar") # it print 5 time tomar because loop is continue 5 times in string and print tomar 
     
#====================membership orpeator======================     
print("i" in "delhi") # true dega
print("i" not in "delhi") # false dega 