# 1
# 22
# 333
# 4444
# 55555
# 4444
# 333
# 22
# 1
n = int(input("enter a number :"))
for i in range (1,n+1):
    for j in range (i):
        print(i,end = "")
    print()     
        

for i in range(n-1,0,-1):
    for j in range (i):
        print(i,end= "")
    print()