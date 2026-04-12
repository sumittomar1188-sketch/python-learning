# text files cant work with screensots 
# not suitable for data types int,float,dict,list
# with open ("C:\Users\hp\Desktop\complete python]\WhatsApp Image 2026-03-22 at 9.45.28 AM (1).jpeg","r") as f :
    # print(f.read())
# isse apan binary files ko read nahi kar sakte he 
with open("screenshot1.jpeg","rb") as f:
    with open("screenshot_copy.jpeg","wb") as wf:
        wf.write(f.read())

# always accept string data type no other data type is allowed lets take an example 
d = {"name": "sumit",
     "age":18,
     "salary":10000000}
with open("seek.txt","w") as f1 :
    f1.write(str(d))  
