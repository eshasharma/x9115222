print "Coding Homework Employee class"
print "--------------------------------------------------------------"


class Employee(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "%s(name='%s',age=%s)" \
                % (self.__class__.__name__,self.name,self.age)
                   
    def __lt__(self,emp2):
        return (self.age < emp2.age)
        
    def __gt__(self,emp2):
        return(self.age > emp2.age)
        
    def __eq__(self,emp2):
        return (self.age == emp2.age)



def sort(emp1,emp2,emp3):
    if(emp1>emp2 and emp1>emp3):
        if(emp2>emp3):
            print "Sorted employee by age is="
            print emp1.name, emp2.name, emp3.name
        else:
            print "Sorted employee by age is="
            print emp1.name, emp3.name, emp2.name
    elif(emp2>emp3):
        if(emp3>emp1):
            print "Sorted employee by age is="
            print emp2.name, emp3.name, emp1.name
        else:
            print "Sorted employee by age is="
            print emp2.name, emp1.name, emp3.name
    else:
        if(emp2>emp1):
            print "Sorted employee by age is="
            print emp3.name, emp2.name, emp1.name
        else:
            print "Sorted employee by age is="
            print emp3.name, emp1.name, emp2.name


emp1 = Employee("Bhanu",25)
emp2 = Employee("Vinay",26)
emp3=Employee("Esha", 24)
print "Before using __repr__"
print emp1
print "***************************"

print "After using __repr__"
tempEmp = eval(repr(emp1))
print tempEmp.name
print tempEmp.age
print "****************************"
sort(emp1,emp2,emp3)