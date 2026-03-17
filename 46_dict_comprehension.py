# simple comprhension 
print({i:i**2 for i in range (1,11)})


distance = {"mumbai":1000,
            "delhi":500,
            "kolkata":2000,
            "raeshvaram":3000}
print({key:value for (key,value) in distance.items()}) 


# now using zip functionn - applying comprehension 

days = {"sunday","monday","tuesday","wednesday"}
temp_c = {35.5,56.6,67.7,67.8}
print({i:j for (i,j) in zip(days,temp_c)})

# using if statement 
product = {"iphone": 10,
           "vivo":15,
           "nokia":0,
           "tables":20}
print({i:j for (i,j) in product.items() if j>0})


# neted comprehension 
# imagine we have to print table 
{2:{1:2,2:4,3:5,4:8,5:10,6:12,7:14,8:16,9:18,10:20}}

print({i:{j:i*j for j in range (1,11)} for i in range(2,5)})