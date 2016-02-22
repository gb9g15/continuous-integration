def Fibonacci(n):
	"""
	Return the n-th value of the Fibonacci sequence.
	"""

	if n < 2:
		return n
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)
