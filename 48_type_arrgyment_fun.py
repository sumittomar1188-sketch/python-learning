# types of arrguments 
# default arrgument
# positional arrgument 
# keyword arrgument


# ============= default arrgument ===============
# default arrgument isme ham parameter ko ek default value assign karte he usko hi degfalut arrgment kehte he lets take an example 
def power (a= 1,b= 1):  # - isme apan ne a or b ko ek default value di he 
    return a*b
x = power()  # yha par hamne koi bhi arrgument nahi diya fir bhi bina error ke chalega agar default use nahi karte to jarur error aata 
print(x)

# ============= positional arrguments ============
# positional arrgument = isme esa he ki agar apan parameter ko jis tarh lenege eg - a,b usi position me hi arrument lega (1,2)
y = power(2,4) # yha par usne apne aap hi le li a me 2 or b me 4 
print(y)

#============= keyword arrgument ================
z = power(b=6,a=3)
# ye ab keyword ke hisab se parameter me se arrgument lega 