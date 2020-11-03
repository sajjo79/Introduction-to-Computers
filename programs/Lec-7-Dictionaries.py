# creating a dictionary variable
Students_marks={"Ahmad": 40, "waleed": 70, "Sumera":"paper not submitted"}
print(Students_marks)

# accessing dictionary elements
print(Students_marks["Ahmad"])

# updating an element in dictionary
Students_marks["Ahmad"]=80
print(Students_marks)

# adding an element in the dictionary
Students_marks.update({"Amna":88})
print(Students_marks)

# removing an element from the dictionary
Students_marks.pop("waleed")
print(Students_marks)
