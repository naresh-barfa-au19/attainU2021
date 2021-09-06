# 03. How do you count the occurrence of a given character in a string?
# Python3 code to program to find occurrence
# to each character in given string

# initializing string
inp_str = "GeeksforGeeks"

# frequency dictionary
freq = {}
	
for ele in inp_str:
	if ele in freq:
		freq[ele] += 1
	else:
		freq[ele] = 1
	
# printing result
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(freq))
