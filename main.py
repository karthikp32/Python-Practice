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