import random

def has_duplicates(sample_List):
    i=0
    temp_List=[]
    for i in range(len(sample_List)):
        if(sample_List[i] in temp_List):
            return True
        else:
            temp_List.append(sample_List[i])
    return False
    
    
def randomize_Birthdays(studentNumber):
    bdays_Sample=[]
    i=0
    for i in range(studentNumber):
        bdays_Sample.append(random.randint(1,365))
    return bdays_Sample

def duplicates_Birthdays_Count(studentNumber, sampleCount):
    i=0
    duplicate_Bdays=0
    for i in range (sampleCount):
        bdays_Sample=randomize_Birthdays(studentNumber)
        if(has_duplicates(bdays_Sample)):
            duplicate_Bdays+=1
    return duplicate_Bdays

studentNumber=23
sampleCount=20
duplicate_bdays=duplicates_Birthdays_Count(studentNumber, sampleCount)
print "Random Trial #1"
print 'The overlap in birthdays for {} students is {} ' .format(studentNumber, duplicate_bdays) 


studentNumber=23
sampleCount=200
duplicate_bdays=duplicates_Birthdays_Count(studentNumber, sampleCount)
print "Random Trial #2"
print 'The overlap in birthdays for {} students is {} ' .format(studentNumber, duplicate_bdays) 
    