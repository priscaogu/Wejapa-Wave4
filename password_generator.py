#Write a function called generate_password that selects three\
#  random words from the list of words word_list and concatenates\
#  them into a single string. Your function should not accept any \
# arguments and should reference the global variable word_list to\
#  build the password.
import string
# Use an import statement at the top
import random
word_list = []

#fill up the word_list
with open("word.txt","r") as words:
	for line in words:
		 #remove white space and make everything lowercase
		 word = line.translate({ord(c):None for c in string.whitespace}).lower()

		 if 3 < len(word) < 8:
			 word_list.append(word)
			 print(word_list)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
	sup = random.choice(word_list)+random.choice(word_list)+random.choice(word_list)
	return sup
# test your function
print(generate_password())