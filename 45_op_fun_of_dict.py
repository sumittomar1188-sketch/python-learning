# membership operation  - he ki nahi vo value usme
s = {"name":"sumit",
      "age":18,
      "subject":{"math":80,
                 "english":90,
                 "science":100}}

print("sumit" in s )#- ye false dega kyuki ye haesh key par kam karta he )
print("name" in s) # it give us true


# iteration 
d = {"name":"sumit",
      "age":18,
      "subject":{"math":80,
                 "english":90,
                 "science":100}}

for i in d :
    print(i,d[i])
   

# there are function is just like tuples
#len / min / max / sorted / 

d1 = {'name': 'sumit', 'gender': 'male', 'salary': 10000, 'age': 19}
print(len(d1))
print(max(d1))
print(min(d1))
print(sorted(d1))


# special function - "keys" / "values" / "items"
print(d1.keys()) #- list of tuples mekey ko dega 
print(d1.items()) # ye list of tuple me key value pairs ko dega sare jitne bhi honge usme 
print(d1.values()) # ye sari values dega existing dictionary ki 

# update is just like adding elemnt - or existing ko chnange bhi karva sakte he 
d2 = {"sumit" : "ji"}
d1.update(d2)
print(d1)  # isne dd1 ko change karke usme sumit ji add karva diya means ki usne existing d1 dict ko update kar diya he 
