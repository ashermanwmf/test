from sys import argv

script, filename = argv

txt = open(filename)

print "The file is : %r \n" % filename
print txt.read()


