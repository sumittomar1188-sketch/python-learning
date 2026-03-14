# len / sum / min / max / soted 

s = {1,2,9,8,5,6}
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s))
print(sorted(s,reverse=True))





# union/update 
# jese ki apan |iska use karke union nikalte the to vo isse bhi nikal aaega
s1 = {2,3,5,4,6}
s2 = {3,9,8,7,0,1}
print(s1.union(s2))
s1.update(s2)# ye union ko utha ke s1 me la deta he or change kar deta he 
print(s1) # ye union jesa result deha 
print(s2) # or ye vahi ka vahi rahega 


#intrsection / intersection_update
s3 = {2,3,5,4,6}
s4 = {3,9,8,7,0,1}
print(s3.intersection(s4))
s3.intersection_update(s4) # ye bhi vesa hi he ki 1 jisme dot use kiya he usko interction me badal dega
print(s3)
print(s4)



# deffernce/difference_update
s5 = {2,3,5,4,6}
s6 = {3,9,8,7,0,1}
print(s5.difference(s6)) # isme to pata hi pehle wale ka hi leta he or same value durse me se print nahi karta 

s5.difference_update(s6) # isme vahi pichhe vahi process change kar deta he s5 ko or s6 vesa ka vesa
print(s5)
print(s6)

#symmetrical_difference/symmetrical_dufference_update
s7 = {2,3,5,4,6}
s8 = {3,9,8,7,0,1}
print(s7.symmetric_difference(s8))
# update
s7.symmetric_difference_update(s8)
print(s7) #ye symmetrical oyput ko isme store kar dega means update 
print(s8)# ye jesa tha vesa hi rahega


