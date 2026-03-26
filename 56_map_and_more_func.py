# three imp feature 
# map - by the use of it we can apply any logic on the list 
# eg - ki ek list ka square print karna he 
b = list(map(lambda x : x**2,[1,2,3,5]))
print(b)

# ab ham even odd using the function 
l1 = [1,2,3,4,5,6]
c = list(map(lambda x:'even' if x %2==0 else "odd",l1))

print(c)

d = [{"name":"sumit","age":5},
    {"name":"rahul", "age":6},
    {"name":"moksh","age":7},
    {"name":"prennet","age":6},
    {"name":"rghu","age":4},
    {"name":"pesha","age":5 }]
d = list(map(lambda d :d["name"],d))
print(d)


# ======== filter ========
# ye list me se filtering ka kam karta he 
# filter ko do chije chahiye lamda function or list 
# isme ye vahi item ko rakhega jo true hoga 
# map list ke har items par logic apply karta he 
l2 = [1,2,3,4]
e =list(filter(lambda x : x <3,l2))
print(e) # yem vahi item ko print karega jo condition ko satisfy karenge 

# lets takes one more example 
l3 = ["mango","grapes","apple","anar"]
f = list(filter(lambda x : x.startswith("a"),l3))
print(f)

# ========== reduce ================
# reduce is an interseting function jo ki ek module ke andar he functool uska kam he reduce karna 
# ek sath list ke do item ko uthata he or then perform operation 
import functools
# isko bhi map or filter ki trh d chij chahiye lamda function or list 
g = functools.reduce(lambda x,y:x+y ,[1,2,3,4,5,6])
print(g) # ye pahle 1+2 karega fir 3 +3 fir uske sum ko aage aage le jaega 
# agar teen z bhi le lenge to ye nahi chelga
#  lets do one more example - find min in the list
h = functools.reduce(lambda x,y:x if x<y else y,[3,6,8,9,7] )
print(h)