# function wiithout arrgument - ISME TO SIMPLE FANDA HOTA HE DIRECT CALL KARO WITHOUT PARAMETER KE 
# jab bhi bhot sara code ho jata he to unko ek ek seperate block de diya jata he usi ko fnctiomn bolte he jese 
'''a = 1
b = 3
c = 6
average = a+b+c/3
print(average)

a = 17
b = 9
c = 6
average = a+b+c/3
print(average)


a = 5
b = 6
c = 8
average = a+b+c/3
print(average)
'''
def avg1() :
    a = int(input("ener a number :"))
    b  = int(input("ener a number :"))
    c = int(input("ener a number :"))
    average = a + b + c /3
    print(average)



def avg2():
    a = int(input("ener a number :"))
    b  = int(input("ener a number :"))
    c = int(input("ener a number :"))
    average = a + b + c /3
    print(average)

print("yha ham pehla vg nakalenge ")
avg1()
print("ab dusra nialenge dusre function se ")
avg2 ()


# fnction with paramerter 
# jab ham function create karte he to bracket ke andar ko parameter kehte he or jab use call karte he tab arrgument kehte he 
# esi condtion me ham un code ko ek sepeate block de denge jisse ki vo jab bulaye o aa jae 

# function are basicslly two types :- 
# 1) built in functions- type , print jo ki pehle se deke rakha he 
# 2) user defined funtion - jo ki user khud banaa he 
# eg of function - jha bhi def dikhe to vo function bana rha he 
def sumit(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"        
# print(sumit(int((input("enter a number ")))))   - isse user input dega 
for i in range (1,11):
    x = sumit(i)
    print(x) # - ye sbko ek ek bar check karega 




# isme two points he  jese ki ek hota he jo program banata he or ek hota he jo use karta he agar use akrne wale ne koi masti
# ki to name to senior program ka aaega na jisne cfunctio banaya he to isko handle karn eke liye function ko relevant banao
# sumit("hello") - junior programmer ne masti ki orr error aaya bada to isko ese handle karenge isme uper 
# uper ek if pass karenge ki agar user koi masti kare to ye aaye 

def intelligent  (num):
    if type(num) == int:
        if num % 2 == 0:
            return "even"
        else :
            "odd"
    else:
        return "pagal he kya "
a =(intelligent("sumit"))
print(a)
y = intelligent(int(input()))
print(y)