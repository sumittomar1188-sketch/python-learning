#here the function which is  only applicable in string 

# capitalize / upper / title / lower /swapcase
s = "sumit tomar"
print(s.capitalize()) # ye pehle word ko capital kare dega 
print(s.title()) # ye title ke form me print kar dega
print("sumit tomar".upper()) # ye sare letter ko upper case me change kar dega
print("SUMIT TOMAR".lower()) # ye sabko lower case me change karega
print("SumIT tOMar".swapcase()) # ye upper ko lower or lower ko upper me 


# cout / find / index 
print('my name is sumit'.count("i")) # ye count karke bata dega ki vo letter kitti bar he 
print("my name is sumit".find("is")) # ye apan ko index bata dega ki ye kha he or alag exist nahi karta hoga to -1 dega matlab nahi he 
print("my name is sumit tomar".index("is")) # ye bhi as same as find ki trh he but ek diff he 
# print("my name is sumit tomar".index("x")) # ye -1 ki jgh isme eeror show kaega 

# endswith / startswith
print("my name is sumit tomar".endswith("ar")) # it prints ture because ar se end hora he 
print("my name is sumit tomar".startswith("my"))# isme bhi true 


# =================format==================
# isme variable ki value ko bhar dega balnk space me {isme}
name = "sumit"
gender = "male"
print("my name is {} and i am {}".format(name,gender)) # it will automates fill name in first blank braces and male in second braces 
print("my name is {} and i am {}".format(gender,name)) # ye sequentally dega 
print("my name is {1} and i am {0}".format(gender,name)) # isme ham indexing ke isab se jama sakte he 

# isalnum / isalpha / isdigit / isidentifiers
print("sumit2123".isalnum())