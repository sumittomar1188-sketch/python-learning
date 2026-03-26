# higher order functions are those function jisme return value khud ek function hoti he 
# ya fir esa function jo input me kisi function ko recive kare 
# lets take an example
# 3 idhar ham ek higher order function banaege
def square (n):
    return n**2

# HOF - ye higher order function he 
def transform (f,l):
    output = []
    for i in l :
        output.append(f(i))
    print(output)

l = [1,2,3,4]
transform(square,l)         
# yha par hamne do funtion ka use karke esa kiya ut lamda function me ham direct kar sakte he 
# agr apan ko yah cube print karvana hota to ek or function bana padta to us chij se bachne ke liye apan is lambda function ka use karenge 
a = transform(lambda x :x**3,l) # idHAR EKLINE ME HI SOLVE HO GYA BY THE USE OF LAMDA FUNCTION 
(a)

# three imp feature 
# map - by the use of it we can apply any logic on the list 
# eg - ki ek list ka square print karna he 
b = list(map(lambda x : x**2,[1,2,3,5]))
print(b)

# ab ham even odd using the function 
l1 = [1,2,3,4,5,6]
c = list(map(lambda x:'even' if x %2==0 else "odd",l1))

print(c)