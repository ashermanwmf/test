# creates three variables with three valuaes assigned respectfully
people = 30
cars = 40
trucks = 15

# choose the care if there are more of them than people or else say you cant
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
    
# evaluate how many trucks there are compared to cars 
if trucks > cars:
    print "That's too many tucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

# evaluate how many trucks there are compared to cars 
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

# making an if statment inside a funciton (It works :DDDD)

def take_the_limo(people):
    if people > 25:
        print "Take the limo."
        
take_the_limo(people)