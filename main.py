# variables are dynamically typed
n = 0
print('n=', n)

n = "karthik"
print('n=', n)

# you can do multiple assignments at the same time
weight, name = 165, "karthik"
print('weight=', weight)
print('name=', name)

# incrementing by 1
weight = weight + 1 #OK
print('weight=', weight)
weight += 1 #OK
print('weight=', weight)
# NOT OK weight++


#None keyword represents null
n = "karthik"
n = None
print('n=', n)

# If statements don't need parenthesis
# or curly braces. They use : after if, elif, else, etc.
# keywords and use indentation to show that
# a body of code belongs to a certain if condition
if name == "karthik":
    print('blue')
elif name == "swathi":
    print('green')

#Parenthesis are required for an if condition, etc.
# the condition is multiple lines long
if (name == "karthik"
    and weight == 167):
    print('purple')

#While loops also have : and their body of code
# is indented starting from the next line    
i = 0
while i < 5:
    print(i)
    i += 1

#for loops can use range(n) function to iterate from 0 to n-1
# or [0, n)
# i is increment
for i in range(5):
    print(i)    
    
# you can use for loops and range(m, n) to iterate from m to n - 1
# [m, n)
for i in range(5, 10):    
    print(i) 

#you can use a for loop to iterate in decreasing order
    
#for. start at i=50, decrement i by 5 while i > 10
# the range [50, 5)
for i in range(50, 10, -5):    
    print(i)

#Decimal division by default
#the result of integer/integer isn't rounded down to the nearest integer
# / --> decimal division
# // --> integer division

print(6/5)

print(6//5)

# integer division with negative numbers truncates towards negative infinity instead of truncating towards 0

print(-6//5)


# workaround for rounding towards 0 in python with negative numbers
# is using decimal division and then converting to int
# because converting a decimal to int rounds towards 0

print(int(-6/5))


# Modulo operator works similar to other C-based languages
# like C, Java, Javascript for positive numbers

print(9%4)

# Modulo operator for negative numbers in Python
# remainder = numerator - (math.floor(numerator/denominator) towards negative infinity) * denominator
print(-7%2)

# to be consistent other C-based languages
import math 
print(math.fmod(-7, 2))


#Python has floor, ceiling, sqrt, and power math functions
print(math.floor(7/2))
print(math.ceil(7 / 2))
print(math.sqrt(49))
print(math.pow(7, 2))

# You can use python inf and -int for positive and negative infinity
float("inf")
float("-inf")


import math
print(math.pow(2, 200))

# dynamic arrays (called lists in python) 
arr = [4,5,6]
print(arr)

# Can be used as a stack 
# add to the end of the stack
arr.append(7)
print(arr)

# pop from the end of the stack
arr.pop()
print(arr)


#O(n) time to add a new value to an index
arr.insert(1, 10)
print(arr)

#O(1) time to set an existing index to a new value
arr[2] = 3
print(arr)


# to initialize an array in python where each element has a particular value like 13
# arr = [value] * size

arr = [13] * 5
print(arr)

# You can use negative indices with arrays to get the 1st value from the end, 2nd value from the end, etc.
arr[-1] = 17
arr[-3] = 73
print(arr)

# You can get sublists in python by slicing arr[n:m] where [n, m)
# just like for-loop ranges, m in non-inclusive
print(arr[1:3])
print(arr[-3:-1])

#You can use unpacking to assign the concrete values within an array to variables in one line
us, china, india, russia, japan = arr
print(us)
print(india)
print(japan)


# Number of variables has to match the number of values in array while unpacking
# us, china = arr


# You iterate through each element of lists in python using index
print("using index")
for i in range(len(arr)):
    print("")
    print(arr[i])

# You iterate through each element of lists in python without index
print("without using index")
for i in arr:
    print("")
    print(i)


# You can use enumerate to possibly get a list of tuples that have (index, value) and iterate through these    
for index, value in enumerate(arr):
    print(index, value)


# You can unpacking and zip() to combine two lists into pairs of values connected at the same index
arr2 = [10,22,33]
arr3 = [40,52,63]

for b, c in zip(arr2, arr3):
    print(b, c)

#You can reverse or flip the elements of a list by calling the reverse() function
arr3.reverse()
print(arr3)

#You can sort an array in ascending order by calling sort() function
arr3.sort()
print(arr3)


#Sort an array in descending order
arr3.sort(reverse=True)
print(arr3)

#String are sorted alphabetically by default
arr4 = ["karthik", "abhi", "akhil", "swathi"]
arr4.sort()
print(arr4)


#To sort by custom algorithm such as length of string
#passing in lambda function to key property
arr4.sort(key=lambda name: len(name), reverse=True)
print(arr4)




        