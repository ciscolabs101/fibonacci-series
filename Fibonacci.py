#Fibonacci Series:
	
#def fibonacci(n):
#	if n == 1:
#		return 1
#	elif n == 2:
#		return 1
#	elif n > 2:
#		return fibonacci(n-1) + fibonacci(n-2)
#	
#for n in range(1, 11):
#	print(n, ";", fibonacci(n))

#Implicit Memoization:
#fibonacci_cache = {}

#def fibonacci(n):
#	#if we have cached the value of n, then return it
#	if n in fibonacci_cache:
#		return fibonacci_cache[n]
#	
#	#compute the nth term
#	if n == 1:
#		value = 1
#	elif n == 2:
#		value = 1
#	elif n > 2:
#		value = fibonacci(n-1) + fibonacci(n-2)
#		
#	#cache the value and return it
#	fibonacci_cache[n] = value
#	return value
#	
#for n in range(1, 101):
#	print(n, ";", fibonacci(n))

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
	#Check if input type is a positive integer
	if type(n) != int:
		raise TypeError("n must be a positive int")
	if n < 1:
		raise ValueError("n must be a positive int")
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n-2)
		
for n in range(1, 101):
	print(n, ";", fibonacci(n))
	
	#Ratio between consecutive numbers in the fibonacci series
	#print(fibonacci(n+1) / fibonacci(n))


