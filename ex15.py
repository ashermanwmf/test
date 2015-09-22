# add the argv module to the python script 
from sys import argv

# set up the variable to ask for 
script, filename = argv

# create a variable that performes the open function on a variable name
txt = open(filename)

# print out the name of the variable you sent the argv module
print "Here's your file %r:" % filename
# print out the read variable
print txt.read()

# ask for a variable input again
print "Type the filename again:"
# input a variable with a prompt
file_again = raw_input(">")

# create a varible that opens a variable
txt_again = open(file_again)

# read the variable
print txt_again.read()