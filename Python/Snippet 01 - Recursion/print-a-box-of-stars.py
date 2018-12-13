# Create a line of character x with length y
def line_of_char(length, char):
	# As long as the length is > 0 call the same function with the same character, but with one length less
	if length > 0:
		return line_of_char(length-1, char) + char
	else:
	# If the length of length is <= 0, return an empty string, if nothing get's returned, an error will occure, 
	# since you can't concat a None with a string
		return ''

# Create a line of stars with length x 
def line_of_stars(length):
	return line_of_char(length, '*') + '\n'
		
# Create a line of spaces with the length - 2 and where the first and last character are a star
def first_last_star_line(length):
	return line_of_char(1, '*') + line_of_char(length - 2, ' ') + line_of_char(1, '*') + '\n'
	
# Create a box of starts, of which the middle is empty
def square_of_stars(size):
	# Return a list of stars with the size of size and
	# return a line of characters with the size of size minus 2 and the char of first_last_star_line with the value of size
	# This will result in calling the function of first_last_star_line the amount of times that size - 2 is. 
	# and lastly return a line of stars to close the square. 
	return line_of_stars(size) + line_of_char(size-2, first_last_star_line(size)) + line_of_stars(size)
		
		
# Print the result of calling the function square_of_stars with a value of 10
print(square_of_stars(10))