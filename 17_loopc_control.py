# break 
# contine 
# pass

for i in range (1,5):
    if i== 3:
        break
    print(i)

# example
# isme hamko user se do number lene he or unke bich me ane wale sare number ke prime factors nikalne he 
lower = int(input("enter lower number: "))
upper = int(input("enter upper number:"))
for i in range (lower,upper):
    for j in range (2,i):
        if i%j== 0:
            break
    else:
        print(i)    

 # continue
for i in range (1,10):
    if i == 5:
     continue   # ye jo number ko ham continue karenge uske print nahi karega 
    print(i)


# pass 
for i in range (1,10):
    # here i dont know what to do next so i write pass to pass and not showing error or move formward to next line 
    pass
for i in range (1,6):
    print(i)