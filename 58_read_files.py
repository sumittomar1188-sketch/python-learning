f = open("sample1.txt","r")
a = f.read()
print(a)
f.close()


# apan bata sakte he ki kitne words read karna he 
f = open("sample1.txt","r")
a = f.read(10) # yha suru ke 10 char ko read karega 
print(a)
f.close()

# line by line reading
f = open("sample1.txt","r")
a = f.readline() # isse pehla line print hoga
b = f.readline() # isse dusri line print hogi ese jitni bar read line ka use karenge utni hi print hogi
print(a,end= "") # isse line gap nahi aaega
print(b,end = "")

# kitni bhi line ho apne code ke andar sabko print ka sakte he 
f = open("sample1.txt","r")
while True:
    data = f.readline()
    if data == "":
        break
    else :
        print(data,end="")