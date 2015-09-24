i = 0
numbers = []
end_of_list = 6

# made a variable to pass a new value into the steps the list goes in
addition_to_list = raw_input("> ")

# converted to funciton

def first_loop(number):
    while number < end_of_list:
        print "At the top i is %d" % number
        numbers.append(number)

        number = number + int(addition_to_list)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % number

# the for loop they told me to write
#for num in range(0, int(addition_to_list)):
    #print "At the top i is %d" %  num
    #numbers.append(num)
    #print "Numbers now: ", numbers
    #print "At the bottom i is %d" % num

# first_loop(i)
        
print "The numbers: "

for num in numbers:
    print num




    