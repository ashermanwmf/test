from sys import argv

# hello and goodybe are two more arguments I added
script, user_name, hello, goodbye = argv
# I changed the > to a %
prompt = '%'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you ahve a %r computer. Nice.
%s %s
""" % (likes, lives, computer, hello, goodbye)