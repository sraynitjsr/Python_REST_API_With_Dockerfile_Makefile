def reverse(num):
	rev = 0
	while (num > 0):
		rev = rev * 10 + num % 10
		num = num // 10
	return rev

def isPalindrome(num):
	if (num == reverse(num)):
		return True
	return False

def printPalindromes(d):
	if (d <= 0):
		return
	smallest = pow(10, d - 1)
	largest = pow(10, d) - 1
	for i in range(smallest, largest + 1):
		if (isPalindrome(i)):
			print(i, end = " ")

def start():
	print('Inside Generating N Digit Palindromes, Here N = 3')
	printPalindromes(3)
