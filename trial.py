# Create a system that allows a teacher to enter a student nane, 4 marks for that student, calculate the total 
# a) The average of each students marks 
# b) Total of all marks
# c) Print an output like ΅Tavonga had: 45, 58, 69, 87. His average is 67/100 and the total 289/400΅
# d) Grade each mark eg 45 - D, 78 - A, 55 - C 


# Function to grade each mark
def grade_mark(mark):
    if mark >= 75:
        return "A"
    elif mark >= 65:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "D"
    
student_name = input("Enter student name: ")

# Ask for the 4 marks separated by spaces
marks = input("Enter 4 marks separated by spaces: ").split()

# Convert input strings to integers
mark1, mark2, mark3, mark4 = map(int, marks)

# Calculate total and average
total_marks = mark1 + mark2 + mark3 + mark4
average = total_marks / 4

# Grade each mark
grades = [grade_mark(mark) for mark in [mark1, mark2, mark3, mark4]]

# Output
print(f"\n{student_name} had: {mark1}({grades[0]}), {mark2}({grades[1]}), {mark3}({grades[2]}), {mark4}({grades[3]}).")
print(f"His average is {average}/100 and the total is {total_marks}/400.")
