student = input("Please enter the student's Full Name: ")
counter = 0
numOfAssign = int(input("Enter the number of assignments: "))
total = 0
while counter < numOfAssign:
    numOfGrade = float(int(input("Please enter the grade: ")))
    total += numOfGrade
    counter += 1
avg = total / numOfAssign
print(student, "has received a final grade of", avg)
    
