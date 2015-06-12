"""
Author: Scott C Gramig
Program: Recursively calculates the Nth Fibonacci number
"""

def fibo(n):
	result = []
	if n == 1 or n == 2:
		return 1
	return fibo(n-1) + fibo(n-2)

print "-------- The Nth Fibonacci Number Calculator --------"
n = int(raw_input("Enter the Nth number: "))

print fibo(n)
