# while loop jisme value ki condition jab tak true nahi ho jati tab tak chlta hi rahega
num = int(input("enter a number :"))
i = 1 
while i<11:

    print(num ,"x" ,i, "=", num*i)
    i +=1

# while loop with else 
x= 1
while x<3:
    print(x)
    x += 1

else :
    print("limit crossed")    

# short game 
import random

n = random.randint(1, 50)
attempt = 0

while True:
    num = int(input("Guess a number: "))
    attempt += 1

    if num > n:
        print("Enter a smaller number")
    elif num < n:
        print("Enter a greater number")
    else:
        print("You guessed the right number 🎉")
        print("Total attempts:", attempt)
        break


# for loop -in it the raneg function is doing participation of ranging
for i in range (1,11):
    print(i) # here it prints 1 to 10 

# step size in for loop jisme ki jump karta 
for i in range (1,11,2):
    print(i) # ye 2 2 ko chhod chood ke jump karke statement dega 

# for loop one demo
for i in range (10,0,-1):
    print(i) # ye reverse print karega 

# for loop demo ye sabke liye applicable he , ecample list string tupple sabme one b one insiate karega
for i in "delhi":
    print(i)

#for withn tuple
for i in ([1,2,3,4,5]):
    print(i)