name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height = 74 / 12 # convert to feet
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hari = 'Brown'

print "Let's talk about %r." % name
#testing out repr() and str9)
print "He's %s feet tall." % str(height)
print "He's %r punds heavy." % repr(weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %d hair." % (eyes, height)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)