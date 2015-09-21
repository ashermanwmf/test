formatter = "%r %r %r %r"
 
# put the following number into the string and change them to a string with rep()
print formatter % (1, 2, 3, 4)
# put strings into the %r spaces
print formatter % ("one", "two", "three", "four")
# put boolean expressions into the %r spaces
print formatter % (True, False, False, True)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
    
