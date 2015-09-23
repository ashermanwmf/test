# creaes a function with two args that have print actions within the function
def chesse_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# adding values to the variables in the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# adding varibles to pass values into function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# do math within args for function
print "We can even do math inside to:"
cheese_and_crackers(10 + 20, 5 + 6)

# work with global variables and math to pass info to args
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
