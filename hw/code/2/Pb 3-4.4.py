print "Coding Homework 3.4.4"
print "--------------------------------------------------------------"

def do_twice(f,value):
    f(value)
    f(value)
    
def print_twice(value):
    print value
    print value
    print "***************"

do_twice(print_twice,'spam')