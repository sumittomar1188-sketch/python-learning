s1 = {1,23,4,5}
# print(s1[0])# it is not aloowed in it 
# or editing also not allowed because indexing is also not allowed 

# adding items are allowed according ti hash function 
s1.add(53)# it is used for adding only 1 item 
print(s1) 
 
s1.update([34,56,78])  # remember it is in a list 
print(s1)


# deleting are also allowed but diffrent metods 
#==============del===================
# del - ise pure set ko delete karsakte he 
s = {1,2,3,4,5}
del s # particular item ko dlete nahi kar sakte he 


# ================ discard ==================
# discard - item ko delete kar sakte he 
s = {1,2,3,4,5}
s.discard (5) # ye 5 ko delete kar dega , but agar ham isme jab value nahi hogi to vo error nahi dega eg niche 
s.discard(58) #  not showing error here


# ====================== remove =======================
# remove - it is just like a discard but if value does not exists it gives an error\
s.remove(2) #it will remove 2 from s
# s.remove(34)showing an error here this diffrence of diccard and remove


#============= pop ===============
# pop - ye randomly delete kare dega kisi bjhi item ko 
s.pop() # random delete any element 


# =============== clear ===============
# clear
