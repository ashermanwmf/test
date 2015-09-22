print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
# changed the input and it works different
print "How much do you weigh?",
weight = raw_input()

# will output with escapes because there is %r to help debug
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# another example of forms
print "What is your initials?",
initials = raw_input()

print "My initiasl are %r." % (initials)
