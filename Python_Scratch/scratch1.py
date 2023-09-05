# We want to be able to write parts independently and understand them
def get_letter_grade(num_grade):

	if 90 <= num_grade <= 100:
		return "A"
	if 80 <= num_grade < 90:
		return "B"
	if 70 <= num_grade < 80:
		return "C"
	if 60 <= num_grade < 70:
		return "D"
	if 0 <= num_grade < 60:
		return "F"

	raise  ValueError("num_grade must be between 0 and 100 (inclusive)")

print(get_letter_grade(100) == "A")
print(get_letter_grade(73) == "C")
print(get_letter_grade(3) == "F")
print(get_letter_grade(-567))