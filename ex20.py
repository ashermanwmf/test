# import argv to allow argv to be passed in terminal
from sys import argv

# create the variable to take the info you type
script, input_file = argv

# create a function called print_all and pass one argument. 
def print_all(f):
    # print the argument and add the read function to it
    print f.read()

# create the function rewind and pas one argument.
def rewind(f):
    # find the first line in the arugument
    f.seek(0)

# create the function that passes two arguments
def print_a_line(line_count, f):
    # print the two arguments passed 
    print line_count, f.readline()

# create a variable that opens the file that was passed into the file
current_file = open(input_file)

# print the following message and start a new line
print "First let's print the whole file:\n"

# read the variable current file 
print_all(current_file)

# print line 
print "Now lets rewind, kind of like a tape."

# return to the zero line in the current file
rewind(current_file)

# print line
print "Let's print three lines:"

# add one to the current line variable 
current_line = 1
# print the current line and read it
print_a_line(current_line, current_file)

# add one to the variable current line
current_line = current_line + 1
# print the current line number and content
print_a_line(current_line, current_file)

# add one to the variable
current_line = current_line + 1
# print the current line and line content
print_a_line(current_line, current_file)

# add one to the current line
current_line = current_line + 1
# print the current line and line content
print_a_line(current_line, current_file)