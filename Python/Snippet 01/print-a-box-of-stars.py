def line_of_char(length, char):
	if length > 0:
		return line_of_char(length-1, char) + char
	else:
		return ''

def line_of_stars(length):
	return line_of_char(length, '*') + '\n'
		
def first_last_star_line(length):
	return line_of_char(1, '*') + line_of_char(length - 2, ' ') + line_of_char(1, '*') + '\n'
	
def square_of_stars(size):
	return line_of_stars(size) + line_of_char(size-2, first_last_star_line(size)) + line_of_stars(size)
		
		
print(square_of_stars(10))