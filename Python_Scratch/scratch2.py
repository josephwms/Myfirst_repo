def fizz_buzz(n):

	if (n % 3 == 0) and (n % 5 == 0):
		return("FizzBuzz")
	if n % 3 == 0:
		return("Fizz")
	if n % 5 == 0:
		return("Buzz")

	return(n)

print(fizz_buzz(3) == "Fizz")
print(fizz_buzz(15) == "FizzBuzz")
print(fizz_buzz(7) == 7)