# empty list
print([])
# 1d list
print([1,2,3,4,5]) # it is homogenus list 
# 2d list 
print([[1,2,3],[2,5,4]])
# 3d list 
l = ([[[1,2],[3,4]],[[4,5],[6,7]]])
print(l[0][0][1])


# =========== indexing ============
# it just like a string but int it particular word is takesn as index \
l = ["sumit",2,2.5,2+2j,True]
print(l[3])
print(l[2])
print(l[4])


# ============= slicing ===========
s = ["baba",8,4.5,2+6j,True,False,56,52.2]
print(s[0:3])
print(s[2:7:2]) # jumping like slicing  

# ========== negative slicing =================
print(s[-5:]) # agar -1 ko use karenge to ye last wala elment print nahi karega to neglect -1  
print(s[7:0:-1])
print(s[::-1]) # reverse list ko print karne ka tareeka 
 