students =["dipak", "kartik", "rohit","satyarth","shivam"]
print(students)
print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[4])
for student in students:

  marks_list =[95, 85, 76, 88, 92]

for marks in marks_list:
        if marks >=90:
            print(f"{students[0]}: Grade: A")
        elif marks >=80:
            print(f"{students[1]}: Grade: B")
        else :
            print(f"{students[2]}: good ")
             
for i in range(5):
    print(f"line number {i}")

for i in range(1,6):
    print(f"line number {i}")

    # define function
def greet(names):
    print(f"Hello, {names}! Welcome to the programming world.")

    greet("Dipak")
    greet("Kartik")
    greet("Rohit")
    greet("Satyarth")
    
for student in students:
    greet(student)