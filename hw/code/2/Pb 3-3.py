print "Coding Homework 3.3"
print "--------------------------------------------------------------"

def right_justify(s):
    length_s=len(s)
    space_count=70-length_s
    str=""
    for num in range(1,space_count):
        str=str+ " "
    print str+s
    
right_justify("-----")
right_justify("Bhanu")
right_justify("vinay")
right_justify("Esha")
right_justify("-----")