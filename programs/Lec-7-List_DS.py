# creating a list and accessing its elements
theList=["multan", "lahore","Dera Ghazi Khan",560]
print(theList)
print(theList[0])
theList[0]="Islamabad"
print(theList)
theList[3]="Muzaffargarh"
print(theList)

# list positive indexing
SubjectList=["biology","botany","zoology","computer","mathematics", "Statistics"]
print(SubjectList)
print(SubjectList[0])   # print first element
print(SubjectList[3])   # print fourth element
print(SubjectList[2:5]) # print 3rd, 4th and 5th element

# list negative indexing
SubjectList=["biology","botany","zoology","computer","mathematics", "Statistics"]
print(SubjectList)
print(SubjectList[-1])   # print last element
print(SubjectList[-2])   # print second element
print(SubjectList[-4])   # print fourth element starting from end and comming down to start
print(SubjectList[-5:-2])# print 5th element from right to 2nd element from right

# adding an element in list
SubjectList.append("education")
print(SubjectList)

# removing an element from list
SubjectList.remove("botany")
print(SubjectList)
