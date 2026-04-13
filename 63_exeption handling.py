# there are two types of errors in python 
# compile time errors - syntax , value, type error jo ki during compilation hote he 
# execution error also called logical error  jo ki run time par hota he 
# apan exeption handle kyu karte he kyuki user ko daravna error na dikhe vo kuchh galt kar de to or security ke liye 
with open(input("enter file :"),"r") as f :
    a = f.read()
    print(a)

# idhar ab ham agar galt file name dalenge to vo error show karega par usko ham try exept mode me dalenge to jo ham chahe vo batega
# =========== try exept demo ======================
try:
    with open(input("enter file :"),"r") as f1 :
        print(f1.read())

except:  # agar galat file ka name  dala to ye wala block chalega nahi to uper wala hi chlega 
    print("file does not exist")


# isse to ham agar apne program me koi bhi error ho to yahi print karva denge 
# like a sarkari website usme koi bhi error ho ek hi error dikhata he 
# ab ham kha error he usko cathch karenge

# catch the coreect error exept printing same error on all errors

# catch specific expetion - har type ke erroe ke liye ek exeption banana last me ek generic expetion jisse kuchh misiing ho to vo bhi handle ho ja

try:
    with open(input("enter file :"),"r") as f1 :
        print(f1.read())
        print(m) # name error

# errors ka pata karne ke liye 
# except Exception as e :
    # print(e.with_traceback)# isse  konsa error he vo pata chl jaega
except NameError:
    print("invalid variable seen")
except FileNotFoundError :
    print("file does not found enter corect file") 
# last me el generic dal do agar vo dono exeption ki jgh koi or aaya error to ye bata dega konsa erroe he 
except Exception as e :
    print(e)    


# ========= else ===========
# else - agar try wla  block sahi se chala koi error nahi aaya to uske bad expet ko ignore karke else ke pass aa jega 
# jab apan ko pata ho ki ye code error nahi dega to usko hi else block me likhenge 
try:
    f3 = open(input("enter file name"),"r")

except FileNotFoundError :
    print("file not found error") 

else :
    print(f3.read())                  


# =========== finally ============
# finaly - chahe  try block sahi ho ya galt ye to chalega hi else jesa nahi ki jab try sahi ho tabhi chalega
try:
    f3 = open(input("enter file name"),"r")

except FileNotFoundError :
    print("file not found error") 

else :
    print(f3.read())     

finally :
    print("ye block chalega hi chahe try sahi ho ya galat")    