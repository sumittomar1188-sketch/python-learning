# serialization - means to convert python data type in JSON format JSON - java script on notaion
import json
l = [1,2,3,4]
with open("demo.txt","w") as f :
    json.dump(l,f)
    



d = {"name": "sumit",
     "age":18,
     "salary":10000000}

with open ("jason.demo","w") as f1 :
      json.dump(d,f1)


# tuple serializtion and deserialization 
t = (1,2,3,4)
with open ("demo.txt","w") as f2:
    json.dump(t,f2) # ab isme ye tuple ko list ke form  me hi serilize karega demo .txt me

