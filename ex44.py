# create a class Parent that isa object
class Other(object):

	# not an overrde 
	def override(self):
		print "OTHER override()"

	# not an override
	def implicit(self):
		print "OTHER implicit()"

	# not an override
	def altered(self):
		print "OTHER altered()"

class Child(object):


	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	# defintely an override
	def override(self):
		print "CHILD override()"

	def altered(self):
		# override
		print "CHILD, BEFORE PARENT altered()"
		# not override
		self.other.altered()
		#not override
		print "Child, AFTER PARENT altered()"

son = Child()

son.implicit()
son.override()
son.altered()
