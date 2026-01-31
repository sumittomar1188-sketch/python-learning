# universal function 
# len / min / max / sorerted
l = [1,2,4,5,33,45,54]
print(len(l))
print(min(l)) # ye tabhi show karega minimum jab homogenus items honge 
print(max(l))
print(sorted(l))
print (sorted(l ,reverse = True)) # hidden trick to print in descending order 




# ====================== count =====================
l1 = [1,2,4,5,5,33,45,54]
print(l.count(5)) # ye frequency of count print karke de dega matlab 5 kitni bar he list me


# ================== index ============
l2 = [1,2,4,5,5,33,45,54]
print(l2.index(33))

# =================== reverse ============
# it permanently reverses the list matlab original list me changes honge or sorted me nayi list banke aati purani me changes nahi 
l3 = [22,2,5,55,64,84]
l3.reverse()
print(l3) #it may change the list premanently in reverse order 


# sort (vs sorted ) 
# sorted is temperory sort the list not changes in original list but in sort originnal list affectes and change permanently eg
l4 = [22,2,5,55,64,84]
print(sorted(l4))
print(l4) # here you see clear diffrence of permanment or temperory 
l4.sort()
print(l)

# ================== copy =============
# it created shallow copy of same list in diffrent adress
l = [1,2,3,5,6]
print(l)
print(id(l))
l1 = l.copy()
print(l1)
print(id(l1))



# ============== Zip =======================
# the zip function returns a zip object , which is an iterator of tuple where the first item in each passed
# iterator is paired together and then the second item in each passed iterator are paired together 
# if the passed iterator have different length , the iterator with the least items descieded the length of the new iterator ex

# write a program to add the item of 2 list indexwise 
l1 = [1,2,3,4,5]
l2 = [-1,-2,-3,-4,-5]
print(list(zip(l1,l2)))