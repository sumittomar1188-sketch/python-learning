# =========================introduction to list ====================================

'''list are refrencial array in which diffrenet type of data type  stored .
difference between list and array 
array me diffrent type ke data types store nahi ho sakte or list me ho sakte he 
array me value binary from me store hoti he or memeori location vahi rehta he array ke andar 
par list ese store hoti he mano ki ye kist he [1,2,3]
to ye pehle memory me kahi store ho jaegi ek address ke sath or fir list me sirf adress ki value store hogi
or adress ki value bhi stored hogi ek memori location ki value me chlo check karte he by using id function
lists are spending extra time or extra space the reson is jab bhi jese 1 ko call karenge to pehle vo 
adrees me jaega fir dursre adres me jaega to timw to lega hi or array fast hota he kyuki uski value vahi stored hotio he 

simple differnce :-
fixed vs dynamic - other language me array fixed or in py dynamic matlab badha sakte he
convenience -> heterogeneus  - array in other lan same data type in python heterogenus
slow of execution - list are slow as compare to array bcz it takes memory location it takes time in execution
memory - list memory use jyada karta he 

'''
l = [1,2,3]
print(id(l)) # isme jo adress stored he value ka uska bhi adress print hoga 
print(id(l[0])) # isme 1 khs store hua vo adress bataega 
print(id(l[1])) # isme 2 kha store hua vo adress bataega 
print(id(l[2])) # isme 3 kha store hua vo adress bataega
print(id(1)) # ye 1 ke store hone ka adress bataega jo ki same hoga list ka data jha store hua uske 
print(id(2)) # same
print(id(3)) # same 
 
'''
characterstics of lists
odered
mutable/changeable
can have duplicate 
heterogenus
are dynamic 
can be nested 
item can be assesed 
can contain any kind of object in python 
'''