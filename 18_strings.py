# in python, the strings are a sequence of unicode character
# method to implement or print striings
print("sumit") # by using double iverted coma
print('sumit') # by using single inverted coma
# for multi line string we use triple invetrd comma
print('''sumit
      badsha
      he''') # these all are valid in python

# now is an indexing in python positve indexing
a = "sumit tomar" # indexing starts from 0 and go to the number 1,2 3,4 like this
#    012345678910 
print(a[0:11]) # ye suru se leke 10 tak jeaga

b= "namostobhayam"
print(b[2:]) # iska matlab he 2 se leke last tak

c = "vivek"
print(c[0:45])

# -------------------negative indexing --------------------------
f = "sumit tomar"
print(f[-1]) # ye number ko indexing dega 

# ----------------------slicing---------------------
s = "sumit tomar"
print(s[2:6]) # isme ye ek range provided hoti he ki yha se yha tak jana he or ek like loop ki trh ki last elemnt nahi lega 

s = "sumit tomar"
print(s[3]) # ye 3 se leke sare number print karega 
s = "sumit tomar"
print(s[:4]) # ye 0 se start karega or 4 pe break mean i tak 

# like a loop isme jumping bhi hoti he 
s = " sumit tomar"
print (s[3:8:2]) # ye ek ke badjump karega 

# =========== negative slicing ==============
s = "sumit tomar"
print([6,0,0-2]) # ye pichhe se chalega but ek ke bad ek chhod chhod ke 

# string ko reverse  karne ka ye ek code he
s= "sumit tomar"
print(s[::-1])   

# jab hamko negative indexing se tomar print karn aho tab 
s = "sumit tomar"
print(s[-5:])

# whwn ulta tomar print karna ho to 
s = "sumit tomar"
print(s[-1:-6:-1])