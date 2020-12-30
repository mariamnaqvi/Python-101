#Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum
def q1(num1,num2):
	if (num1*num2)>1000:
		return (num1+num2)
	return num1*num2

assert q1(2,3) == 6, "Ensure that the function is defined, named properly, and returns the correct value"
assert q1(5000,3) == 5003, "Ensure that the function is defined, named properly, and returns the correct value"
print("q1 is correct.")

#Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number
def q2(max_value):
	for num in range(1,max_value):
		print("previous " + str(num-1) + " current " + str(num) + " sum " + str(num-1 + num))

q2(10)

