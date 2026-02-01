# list comprehension formula 
# newlist = [expression for item in iterable if condition == True]  
# advantages of list comprehension -
# more time efficent and space efficient than loops 
# require fewer line of code 
# transform iterative statement into a formula

# just ek example :- print list first to last 
l = []
for i in range (1,11):
    l.append(i)
print(l)    # ye pure 10 tak number ko list me print karva dega 

# by using list comprehension 
l1 = [i for i in range (1,11)]
print(l)

# scalar multiplication on vector 
# first simple method 
l = [2,3,6]
s = -3
l1 = []
for i in l :
    l1.append(i*s)
print(l1)        

# now by list comprehension same question 
l =  [2,3,6]
s = -3 
l1 = [i*s for i in l ]
print(l1)


# add squares in list by using list comprehension 
l = [2,5,6,8]
l1 = [i**2 for i in l ]
print(l1)


# print all number divisible by 5 in 1 to 50 
l1 = [i for i in range(1,50) if i %5 == 0]
print(l1)

# print language strts with p 
languages = ["python","c++","php","java","c"]
l1 = [language for language in languages if language.startswith("p")]
print(l1)

# nested if with list comprehension 
basket = ["apple","mango","cheery","banana"]
my_furit = ["apple","guava","grapes","banana"]
# add new list from my_fruit and items if the fruit exist in the basket and also starts with "a"
l = [fruit for fruit in my_furit if fruit in basket if fruit.startswith("a")]
print(l) 

# print (3,3) matrix using list comprihenseion  - use of nested loops 
l = [[i*j for i in range (1,4)]for j in range(1,4)]
print(l)

# cartisiean product - list comprehension on 2 list together 
l1 = input()
l2 = [5,6,7,8]
l = [i*j for i in l1 for j in l2]
print(l)