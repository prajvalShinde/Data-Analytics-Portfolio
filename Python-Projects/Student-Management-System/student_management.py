students = []

def find_student(student_id):
    return next((s for s in students if s["id"] == student_id), None)

def add_student():
    sid = int(input("Enter ID: "))
    if find_student(sid):
        print("ID already exists!"); return
    student = {"id": sid, "name": input("Enter Name: "), "age": int(input("Enter Age: ")), "course": input("Enter Course: "), "marks": float(input("Enter Marks: "))}
    students.append(student)
    print("Student added successfully!")

def display_students():
    if not students: print("No students found!")
    for s in students: print(s)

def search_student():
    s = find_student(int(input("Enter ID to search: ")))
    print(s if s else "Student not found!")

def update_student():
    s = find_student(int(input("Enter ID to update: ")))
    if s is None: print("Student not found!"); return
    s["name"] = input("New name: ")
    s["age"] = int(input("New age: "))
    s["course"] = input("New course: ")
    s["marks"] = float(input("New marks: "))
    print("Student updated successfully!")

def delete_student():
    s = find_student(int(input("Enter ID to delete: ")))
    if s is None: print("Student not found!"); return
    students.remove(s)
    print("Student deleted successfully!")

def analyze_marks():
    if not students: print("No students found!"); return
    print("Average marks:", round(sum(s["marks"] for s in students) / len(students), 2))
    print("Highest:", max(students, key=lambda s: s["marks"]))
    print("Lowest:", min(students, key=lambda s: s["marks"]))
    for s in students: print(s["name"], "Pass" if s["marks"] >= 40 else "Fail")

def main():
    actions = {1:add_student,2:display_students,3:search_student,4:update_student,5:delete_student,6:analyze_marks}
    while True:
        print("\n1.Add 2.Display 3.Search 4.Update 5.Delete 6.Analyze 7.Exit")
        try:
            choice=int(input("Choice: "))
            if choice == 7: break
            if choice in actions: actions[choice]()
            else: print("Invalid choice")
        except ValueError: print("Please enter valid numbers")

if __name__ == "__main__": main()
