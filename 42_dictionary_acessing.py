# 0 ye indexig support nahi karta he or inordered hota he 321 = 123 ye he 
# in it assecing is done by using square bacakte or get [] lets take an example 
s1 = {"name":"sumit",
      "age":23,
      "salary":1000}
print(s1["name"])

print(s1.get("name"))

# 2D dict me se bhi kese karenge 
s = {"name":"sumit",
      "age":18,
      "subject":{"math":80,
                 "english":90,
                 "science":100}}


print(s["subject"]["math"])