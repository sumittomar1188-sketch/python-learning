# tuples are just like a list as we can say it brother of list 
# but tuples are immutable means - we cannot able to change elememnts from tuples




# creating empty tuple 
t1 =()
print(t1)
# only 1 elemnt tuple is tricky bcz if we do thi t2 = (2) it will print () 2 so insted of this use comma then it become tuple
t2 = (2,)
print(t2)
#homogenus tuple========== same data type
t3 = (1,2,3,4,5,6)
print(t3)
# heterogenus 
t4 = (1,2.3,True,[1,2])
print(t4)
# using type conversion
t5 = tuple('helo') # eye is pure elemnt ko tuple bana dega 
print(t5)




#==================== indexing and slicing ========================
print(t3)
print(t3[0]) # positive 
print(t3[-1])# negative 
print(t3[0:3])
print(t3[::-1])
print(t3[-3:-1])