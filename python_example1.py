# Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.


def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

print("big">"small")


def format_name(first_name, last_name):
    if first_name == '' and last_name == '':
        string = ""
    elif first_name == '':
        string = "Name: " + last_name
    elif last_name == '':
        string = "Name: " + first_name
    else:
        string = "Name: " + first_name + "," + last_name

    return string


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string



# The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length). Fill in the blank to make this happen.

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2)>=len(word1) and len(word2)>=len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


# check the code below

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

print(((10 >= 5*2) and (10 <= 5*2)))


# The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number.
# Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
	if numerator==0 or denominator==0:
		return 0
	else:
		result=numerator/denominator
		while result>=1:
			result-=1
		return result

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0