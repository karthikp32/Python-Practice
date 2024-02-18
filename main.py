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


#List comprehension
arr5 = ["karthik" * i for i in range(5)]
print(arr5)

#You can use list comprehension to create 2D lists
#for ex. creating a 10x10 2D array with all zeroes
arr6 = [[0] * 10 for i in range(10)]
print(arr6)


#Creating 2D lists this way can create 4 of the same rows instead of 4 unique rows in the larger list
# so if you modify one value in one row, it will modify that same value in all of the other rows
arr7 = [[0] * 4] * 4
arr7[0][3] = 17
print(arr7)

#You can slice, print, etc. strings similar to arrays
s1 = "karthik"
print(s1[2:4])

#A specific character in a string can't be changed since strings are immutable
s2 = "swathi"
# s2[0] = "k"

#You can concatenate a new string to original string since this will create a whole new string
#Considered O(n) time operation since you're creating a whole new string
s2 += "abhi"
print(s2)

#Integers can be converted to strings
print(str(23) + str(23))

#String can be converted to integers
print(int("23") + int("23"))
        
#You can get ASCII value using ord() function
print(ord("A"))       
print(ord("a"))       

#You can combine strings using join() function and a delimiter
strings = ["karthik", "swathi", "abhi", "akhil"]
print("/".join(strings))

#Queues are doubled ended queues by default
#you can use deques if you want to use a data structure to work like a stack
#you can append to the right, pop from the right, append to the left ,pop from the left
#O(1) time for these enqueuing and dequeuing operations I think

from collections import deque 

queue = deque()
queue.append(3)
queue.append(1)
queue.append(4)
print(queue)

queue.popleft()
print(queue)


queue.pop()
print(queue)

queue.appendleft(2)
print(queue)


#You can use hashset to store unique values and search and insert a value in O(1) time
tempSet = set()

tempSet.add(1)
tempSet.add(2)
tempSet.add(3)


print(tempSet)
print(len(tempSet))

#You can use "in" operator to check if an element exists in the set
print(1 in tempSet)
print(3 in tempSet)
print("Karthik" in tempSet)


#You can remove values in O(1) time
tempSet.remove(3)
print(3 in tempSet)


#You can create a set from a list in python
print(set([3,1,4]))

# You can use set comprehension to initialize a set and insert values 
# similar to how you would for a certain range values 0...n with a for loop

# HashMap AKA Dictionaries in Python, Maps in Java, Objects in Javascript
# can't have duplicate keys
myMap = {}
myMap["karthik"] = 32
myMap["karthik"] = 23
myMap["swathi"] = 17
print(myMap)

#Use len to get number of key value pairs
print(len(myMap))

#you can remove key value pair by using pop() of hashmap
myMap.pop("karthik")
print(len(myMap))


#You can use "in" operator to check if an element exists as key in the map
print("swathi" in myMap)


#you can initialize maps with concrete values 
myMap2 = {"color1": "blue", "color2": "red"}
print(myMap2)


# You can use dictionary comprehension to initalize a dictionary/map with 
# with concrete key values pair for a range of values 0,1..n just like
# you would with a for loop
myMap3 = {i: i*i for i in range(10)}
print(myMap3)


#Looping through maps

#You can loop through the keys
for key in myMap3:
    print(key)

#You can loop through the values
for val in myMap3.values():
    print(val)

#You can loop through keys and values using items() and unpacking
for key, val in myMap3.items():
    print(key, val)    


#Tuples are like immutable arrays that you use () to initialize
#you can't change the values in a tuple after you initialize it
# with certain values

pi = (3, 1, 4)
print(pi)
print(pi[2])

#You can use as key in hashmap or element in hashset
myMap4 = {("karthik", "pillalamarri"): "984 N. High St."}
print(myMap4)

mySet2 = set()
mySet2.add(("karthik", "pillalamarri"))
mySet2.add(("akhil", "pillalamari"))
print(mySet2)
print(("akhil", "pillalamari") in mySet2)

#Lists can't be keys for hashmap since they can have duplicate values so you can't generate unique
# hash values which makes them not hashable I think 
# myMap5 = {[3,1,4]: "pi" }
# print(myMap5)

# Heaps
import heapq

# heaps are min heaps by default
# can use heap to find the min/max values of a set of values in O(1) time

# implemented using arrays under the hood
# you can initialize using [] just like arrays
minHeap = []
heapq.heappush(minHeap, 8)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 10)

#min will always be at index 0
# print(minHeap[0])

#you can keep pop values from minHeap while length is non-zero
while len(minHeap):
    print(heapq.heappop(minHeap))

# to create max heap, create min heap and multiply each value by -1
# when you push and pop
# for ex. 1,2, 1000 will be added as -1,-2,-1000
# pop the min from this heap will return -1000 and multiplying it by -1
# will give you the max
maxHeap = []
heapq.heappush(maxHeap, -8)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -10)

#max will also be at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

#you can build heap from initial set of concrete values using heapify()

arr = [3,1,4, 8]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))


# to create functions, use def keyword and define the functionName and parameters and colon (:)
# just like conditional statements and loop and body is indented
def functionName(parameter1, parameter2):        
    return parameter1 * parameter1 * parameter2 * parameter2

print(functionName(2, 5))

# Nested functions that are inner functions inside of outer functions
# have access to outer variables in outer function scope by default

def outerFunc(address, phoneNumber):
    name = "karthik"

    def innerFunc():
        return name + address + phoneNumber
    
    return innerFunc()
    
print(outerFunc("N. High St.", "312450"))


# You can modify the data within data structures
# but you can't reassign in nested functions
#for ex. you can modify colors = ["blue", "red", "green"]
# but you can't assign colors = ["purple", "orange", "brown"]

def square(arr1, arr2):
    def helper():

        # this is OK
        arr1[1] = "yellow"

        # this is NOT OK
        # arr2 = ["black", "gray", "white"]

        # using nonLocal allow you to reassign and have it be updated
        # outside of helper() scope

        nonlocal arr2
        arr2 = ["black", "gray", "white"]
    helper()
    print(arr1, arr2)

square(["blue", "red", "green"], ["purple", "orange", "brown"])


#Class
class ColorClass:
    #Constructor initialized with __init__
    #self is similar to "this" keyword in other programming languages
    #and passed onto every function in Python
    def __init__(self, paint_brush):
        #You can use self keyword and dot notation to create member variables
        self.paint_brush = paint_brush
        self.length_paint_brush = len(paint_brush)


    #Pass in self keyword as a parameter to function
    # to get access to self's member variables
    def getPaintBrushType(self):
        if self.paint_brush == "filbert":
            return "fan"
        return "wash"     

    #You can use self keyword to call other functions that belong to self
    def getPaintBrushBrand(self):
        if self.getPaintBrushType() == "fan":
            return "Transon"
        return "Mont Marte"

colors = ColorClass("filbert")
print(colors.getPaintBrushBrand())




