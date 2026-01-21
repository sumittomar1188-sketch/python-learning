email = input("enter your email :")
password = input("enter password :")

if email == "sumit" and password == "1234":
    print("welcome")
elif email == "sumit" and password != "1234":
    print ("incorrect password \n try again...")
    if password != "1234":
        input("enter again password: ")
        if password == "1234":
            print("welcome")
        else :
            print("again wromg password")     


else :
    print("sahi email or pass dalo bhai")   