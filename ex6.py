# writing a string with a number in it
x = 'There are %d types of people.' % 10
# creating a string variable
binary = 'binary'
# creating a string variable
do_not = "don't"
# created a string and added two other variable strings
y = 'Those who know %s and those who %s.' % (binary, do_not)

# printed both x and y variable
print x
print y 

# printed a sting and added the string with an integer by converting it with repr()#
print "I said: %r." % x
# printing a string and adding a variable with other variables added
print "I also said: '%s'." % y

# created two variables one can accept an integer or string by passing through repr()#
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# print the string variable and add the boolean experssion variable to the end#
print joke_evaluation % hilarious

# created two variables with strings
w = 'This is the left side of...'
e = 'a string with a right side.'

# added variables with strings together like math
print w + e