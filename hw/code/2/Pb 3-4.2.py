print "Coding Homework 3.4.2"
print "--------------------------------------------------------------"

def do_twice(f,value):
    f(value)
    f(value)
    
def print_spam(value):
    print value

do_twice(print_spam,'spam')