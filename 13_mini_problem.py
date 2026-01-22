# the current population of town is 10000 and igt is increase at the rate of 10% per year , you have to write program
# to find out the population at the and of each of the last 10 years 

current_pop = 10000
for i in range (10,0,-1):
    print(i,current_pop)
    current_pop = current_pop/1.1


# sequence and series question 
n = int (input("enter a number "))
fact = 1
result= 0
for i in range (1,n+1):
    fact = fact*i
    result = result+fact
print(result)     
    
      