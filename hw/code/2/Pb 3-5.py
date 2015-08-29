print "Coding Homework 3.5"
print "--------------------------------------------------------------"


column=0

def print_pattern_1():
    print "+",

def print_pattern_2():
    print "/",

def print_pattern_3():
    print "-",

def print_pattern_4():
    print " ",
def draw_pattern(row, column):
    for i in range(0,row*5+1):
        if (i%5==0):
            for j in range(0,column*10+1):
                if(j%10==0) :
                    print_pattern_1()
                elif (j%2==0):
                    print_pattern_3()
                else :
                    print_pattern_4()
        else :
            for j in range(0,column*10+1):
                if(j%10==0) :
                    print_pattern_2()
                else :
                    print_pattern_4()
        print ""
        
print "Pattern with 2X2 grid"
draw_pattern(2,2)

print "Pattern with 4x4 grids"
draw_pattern(4,4)
        