# empty dictionary 
s = {}

# 1D dictionary or homogenus
s1 = {"name":"sumit","gender":"male"}
print(s1)


# mixed  type dictonary 
s2 = {(1,2,3):1,"sumit": "badshah"}
print(s2)


# 2D - Dictionary - dictionary ke andar dictionary 
s3 = {"name":"sumit",
      "age":18,
      "subject":{"math":80,
                 "english":90,
                 "science":100}}


# using dict function bhi dictionary ban jati he usme list of tuple ko vo dictionary ke form me assume kar leta he eg -:
s4 = dict([(1,2),(3,4),(5,6)])
print(s4)

# duplicte - isme ye hota he ki vo duplicateme next wali ko print karta he change ho jati he pehli value 
s5 = {"name":"vivek"
      ,"name":"sumit"}
print(s5) # isme ye apan ko sumit dega name me kyuki change ho jati he value jab same key hoti he to 


# does not support mutable item as a key 
s6 = {[1,2,3]:5} # ye support nahi karega
print(s6)

