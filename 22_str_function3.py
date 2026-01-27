# split fincton 
# sabse jyada use hota he
print("my name is sumit tomar".split())# ye sabko ek list me bat deta he
print("my name is sumit tomar".split("i")) # ye i ke basis pe split karega 
# kuchh age nahi denge braket me tab space pe split karega or agar koi chij fill karenge to vhahi se break karega 

# join 
#ye split pe jo list banegi to usko join karke ek sentense bana dega 
print(" ".join(['my', 'name', 'is', 'sumit', 'tomar']))
print("-".join(['my', 'name', 'is', 'sumit', 'tomar']))

# replace 
print("my name is sumit tomar ".replace("sumit","betu"))

# string me ye yad rakhna he ki string ki value change nahi hogi kabhi ye jo bhi function he unse nai value banegi eg
a = "my name is sumit tomar"
print(a.replace("sumit","betu")) # ye nai value bana dega bina variable ki original string ko change kiye 
print(a)

# strip  - ye sare spaces hata deta he 
print("sumit                                    ".strip())
print("        sumit tomar".strip())
