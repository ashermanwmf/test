print "You enter a dark room with two doors. Do you go thorugh door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input(">")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doping %s is probably better. Bear runs away." % bear
    
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input(">")
    
    if instanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
# expansion pack andrewsherman. One extra door wholly.
elif door == "3":
    print "Its your mom. Shes mad at you about your grades"
    print "1. Study."
    print "2. Run."
    print "3. Tell her the truth by typing 'True' "
    
    decision = raw_input(">")
    
    if decision == 1:
        print "She is not mad you are off the hook. Go study if you want."
    elif decision == 2:
        print "The insanity rots your eyes into a pool of muck. Good job!"
    elif decision == decision:
        print "She hits you with her backhand (her ring hand ouch!) What did you say?"
    else:
        print "You are grounded."
    
else: 
    print "You stumble around and fall on a knife and die. Good job!"