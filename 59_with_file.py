# it is a good idea to close a file after usage it will free up the space 
# if we dont close it garbage collector close it 
# with keyword close the file as soon as the use is over 
# lets take an example 
with open("newfile.txt", "w") as f :
    f.write("sumit bhai amar rahe ")
# iske bad agar ise bhar se caal karenge to nahi write hoga kyuki by default ye close kar dega file ko 

with open("sample1.txt","r") as f1 :
    print(f1.read(10)) 
    print(f1.read(10))


l = ["hello world " for i in range(1000)]
with open ("newfile.txt","w") as f2 :
    f2.writelines(l) # `1000 bar file me write kar diya ab isko memeory me bina load diye chuncks me nikalenge`
    
with open("newfile.txt", "r") as f3 :
    chunk_size = 100
    while len(f3.read(chunk_size))>0:
        print(f3.read(chunk_size),end="")
        f3.read(chunk_size)


   
with open("newfile.txt", "r") as f3 :
    chunk_size = 10
    while len(f3.read(chunk_size))>0:
        print(f3.read(chunk_size),end="***")
        f3.read(chunk_size)

