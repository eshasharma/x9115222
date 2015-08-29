print "Coding Homework 3.4.5"
print "--------------------------------------------------------------"

def do_twice(f,value):
    f(value)
    f(value)

def do_four(f, value):
    do_twice(f,value)
    do_twice(f,value)
    
def print_twice(value):
    print value
    print value
    print "***************"

do_four(print_twice,'spam')