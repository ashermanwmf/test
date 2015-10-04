## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
	pass

# Dog is-a animal and dog has-a name 
class Dog(Animal):

	def __init__(self, name):
		## the dog has-a name
		self.name = name

# Cat is-a animal and cat has-a name
class Cat(Animal):

	def __init__(self, name):
		## the cat has-a name
		self.name = name

#Person is-a object
class Person(object):

	def __init__(self, name):
		## the person has-a name 
		self.name = name
		
		##  person has a pet of some kind 
		self.pet = None

# Employee is-a person has-a salary and name
class Employee(Person):

	def __init__(self, name, salary):
		## what is this
		super(Employee, self).__init__(name)
		## employee has-a salary and name
		self.salary = salary

# Fish is a object 
class Fish(object):
	pass

# Salomon is a fish
class Salmon(Fish):
	pass

# Salmon is a fish
class Halibut(Fish):
	pass

# rover is a dog
rover = Dog("Rover")

# satan is a cat
satan = Cat("Satan")

# mary is a person 
mary = Person("Mary")

# make the pet attribute of mary equal satan which is the name attribute of Cat
mary.pet = satan


# frank is a employee with a sallary of 
frank = Employee("Frank", 120000)

# frank has-a pet named rover
frank.pet = rover

# a fish has a flipper
flipper = Fish()

# slamon has a crouse
crouse = Salmon()

# halibut has a harry
harry = Halibut()
