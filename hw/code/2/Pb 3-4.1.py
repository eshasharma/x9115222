print "Coding Homework 3.4.1"
print "--------------------------------------------------------------"

def do_twice(f):
    f()
    f()
    
def print_spam():
    print 'spam'

do_twice(print_spam)