"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: (int) to find the largest digit in it
	:return: the largest digit of n
	"""
	if n < 0:
		n = n - (2*n)

	return helper(n, 0)


def helper(n, largest):
	last_digit = n % 10
	if n == 0:
		return largest
	else:
		if last_digit > largest:
			largest = last_digit
		n //= 10
		return helper(n, largest)

	# if n < 0:							                            # if n is a negative int
	# 	n = n - (2*n)					                             # make n a positive int
	#
	# if n < 10:   												    # base case
	# 	return n
	#
	# else:
	# 	last_digit = n % 10
	# 	last_second = (n - n % 10) // 10 % 10
	# 	if last_second > last_digit:
	# 		n = (n - last_digit) // 10    							# ex: 8 > 1, make 281 to 28
	# 	else:
	# 		n = (n - last_digit) // 10 - last_second + last_digit   # ex: 4 < 5, make 12345 to 1235
	# 	return find_largest_digit(n)


if __name__ == '__main__':
	main()

