# program to find the sum of  three digit number entr by the user
num = int (input("enter numbers :"))
#345%10 -> 5
a= num%10
num = num//10
# 34%10 -> 4
b= num%10
num = num//10
#3
c= num%10

print(a+b+c)

# or
a= num//100
b = (num/10)%10
c = num%10
print(a+b+c)