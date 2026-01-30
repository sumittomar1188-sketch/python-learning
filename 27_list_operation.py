# Arithmetic 
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
print(l1+l2)
print (l1*3) # print 3 times l1

# membership operators
l3 = [1,2,3,4,5]
l4 = [2,3,4,5,[6,7]]
print (5 in l3) # it comes true 
print (6 in l4) #it comes false because in it the 6 is inside the different list  


# loop
l1 = [1,2,3,4,5]
l2 = [2,3,4,5,[6,7]]
for i in l1 :
    print(i)
for i in l2 :
    print(i)