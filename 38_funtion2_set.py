# isdisjoint / issubset / issuperset
s1 = {2,3,5,4,6}
s2 = {3,9,8,7,0,1}

# isdisjoint - isme ye he ki true false me bataega ki alag alag he ki nahi ek bhi value same hogi to false dega 
print(s1.isdisjoint(s2)) # ye false dega kyuki value 3 same he dono me 

# issubset - isme ki subset he ya nahi ki ek ki vahi exist karti he dusre me ki nahi 
s3 = {1,2,4,5,6}
s4 = {4,5,6}
print(s3.issubset(s4))  # false dega kyuki s3 ki value s4 me exist nahi karti he 
print(s4.issuperset(s3)) # true dega kyuki vo s3 me s4 ki value present he 


# issuperset - isme check karenge ki vo value uska superset he ya nai 
print(s3.issuperset(s4)) # print true s3 me s4 ki value stored 






# copy - karta to copy he vo bhi difrent memory location
s5 = {1,2,3,4}
s6 = s5.copy()
print(id(s5))
print(id(s6))