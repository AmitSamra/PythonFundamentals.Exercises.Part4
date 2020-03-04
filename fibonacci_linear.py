# Exercise 3
'''
Create a program called fibonacci_linear.py

Requirements

Given a term (n), determine the value of x(n).
In the fibonacci_linear.py program, create a function called fibonnaci. The function should take in an integer and return the value of x(n).
This problem must be solved WITHOUT the use of recursion.
Constraints
n >= 0
'''

a = list(range(0,31))
print(a)
b = [0,1]

for i in range(2,31):
	c = b[i-1]+b[i-2]
	b.append(c)
print(b)

def fibonacci(n):
	return b[n]

print(fibonacci(5))


a = list(range(0,31))
print(a)
b = [0,1]

for i in range(2,31):
	c = b[i-1]+b[i-2]
	b.append(c)
print(b)

def fibonacci(n):
	return b[n]

print(fibonacci(5))

#