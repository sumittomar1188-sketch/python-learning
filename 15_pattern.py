'''
*
**
***
'''
n= int(input("enter a number of pattern :"))
for i in range (1,n+1):
    print("*"*i)


# 1
# 121
# 12321 
# 1234321

n = int (input("eneter a number"))
for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end ='') 
    for j in range(i-1,0,-1):
        print(j,end='')
    print()      