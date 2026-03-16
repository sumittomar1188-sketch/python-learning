s1 = {"name":"sumit","gender":"male"}

s1["salary"] = 10000

print(s1)
s1["age"]= 19

print(s1)

# 2D dict me adding ese karenge 

s = {"name":"sumit",
      "age":18,
      "subject":{"math":80,
                 "english":90,
                 "science":100}}

s["subject"]["dsa"] = 76
print(s)


# =========== deletion ================

# ============== pop ============

# pop - jo item apan chae delete kar sakta he ye 


d = {'name': 'sumit', 'gender': 'male', 'salary': 10000, 'age': 19}

d.pop("age")
print(d) # ye apan ko age vali key or value dono ko delete kar dega 


# ========== popitem ==============
# popitem - ye last vali key or value ko dlete kar deta he dictionary me se 

d1 = {'name': 'sumit', 'gender': 'male', 'salary': 10000, 'age': 19}
d1.popitem() # ye ek bar delte kar dega dict me se last item ko 
print(d1)
d1.popitem() # ye ab delted item vali dict me se bhi ek last vale ko dlete kar dega 
print(d1)


# =================== del =================
# del - ye same as the pop he ek sath pura bhi kar sakte he or ek particular iten ko bhi 
d3 = {'name': 'sumit', 'gender': 'male', 'salary': 10000, 'age': 19}
del d3["name"]  # or del d3 karke pure ko bhi dlete kar sakte he 
print(d3)

# ================= clear ================
d4 = {'name': 'sumit', 'gender': 'male', 'salary': 10000, 'age': 19}
d4.clear()
print(d4)  # empty dega 


# 2d ya 3d me remove ese karenge 
s3 = {"name":"sumit",
      "age":18,
      "subject":{"math":80,
                 "english":90,
                 "science":100}}

del s3["subject"]["math"]
print(s3)