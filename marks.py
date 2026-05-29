# Taking input for 5 subjects from the user
sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))
sub4 = int(input("Enter marks for subject 4: "))
sub5 = int(input("Enter marks for subject 5: "))

# Calculating total, average, and percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5
percentage = (total / 500) * 100

# Printing the results
print("Total marks:", total)
print("your Percentage is:", percentage)

# Grading logic based on percentage
if percentage >= 75:{
    print("REsult: Distinction")
}
elif percentage >= 60:
    print("Result: First Class")
elif percentage >= 45:
    print("Result: Pass Class")
else:
    print("Result: Fail")