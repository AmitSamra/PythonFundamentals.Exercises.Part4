def fibonacci(n):
	if n in [0,1]:
		return n
	elif n >= 2 and n <= 30:
		return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))
