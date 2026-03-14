# ye to just like set hi rehte he par unme immutability aa jati he or isko "fozenset" key word se denote kiya jata he 
s1 = frozenset([1,2,3]) # or ye sif ek arrgument leta he 
print(s1)
print(type(s1)) # or isme koi changes nahi ho sakte he immutability

# isme uniion intersection difference sab function kam karenge 
# bas imutable to vo function kam nahi karernge jo ki lets take an example :
fs1 = frozenset([1,2,3,4])
fs2 = frozenset([5,6,7])
print(fs1|fs2)
print(fs1.union(fs2))


# isme 2d set pposssible he normal set me nahi kyuki usme mutablen iten ko set ke andar nahi rakh sakte he isme rakh skate he 
fs = frozenset([1,2,3,frozenset([4,5,6])])
print(fs)