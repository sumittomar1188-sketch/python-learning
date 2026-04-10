# types of data in i/o
# text - 12345 as a unicode characters 
# binary - 1234 as a sequennce of bytes of its equvalents 
# these 2 types deals with 
# text - all programs files are text files 
# binary files - music, files , images vedios

# new file create ese hoti he
f = open("sumit.txt","w")
f.write("sumit jindabad rahe")

# agar existing file me likhna he to ese likhenge 
f1 = open ("sumit.txt","w")
f1.write("sumit ji ye purane text ko remove kar dega or ye wala text le aega ")
f1.close()


# agar bina replace kiye print karana ho to "a" ka use karenge append 
f2 = open("sumit.txt","a")
f2.write("\nsumit jindabad")
f2.close()

# multiple line print ek sath bu using write lines 
l = [ "hello sumit ji","\nnamste ji","\nhalva puri khaoge"]
f3 = open("sample1.txt","w")
f3.writelines(l)
f3.close()