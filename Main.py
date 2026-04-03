import sys,time,os




class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def __str__(self):
        return f"{self.name}, {self.age}, {self.course}"
    def Info(self):
        return str(self)

class StudentSystem:

    def __init__(self):
        self.students=[]
        self.load_file()

    def addS(self):#For adding students to the array
        name = input("Enter student's name: ")
        age = input("Enter student's age: ")
        course = input("Enter the course of the student: ")
        student = Student(name, age, course)
        self.students.append(student)
        self.SaveF()
        print("\nStudent Successfully Added")

    def ViewS(self):
        if not self.students:
            print("No students found")
            return

        print("List of Students")
        for i, student in enumerate(self.students,start=1):
            print(f"{i}.{student.Info()}")
        print()

    def SaveF(self):
        with open("Student Records.txt","w") as file:
            for student in self.students:
                file.write(f"{student.name}, {student.age}, {student.course}\n")

    def DeleteS(self):
        self.ViewS()
        self.SaveF()
        if not self.students:
             return
        try:
            print("\nStudent Records")
            for i, student in enumerate(self.students, start=1):
                print(f"{i}.{student.Info()}")

            option = int(input("Choose student record to delete: "))
            if 1 <= option <= len(self.students):
                delete = self.students.pop(option - 1)
                print(f"Deleted: {delete.name}")
        except ValueError as VErr:
            print(VErr)

    def load_file(self):
        try:
            with open(f"Student Records.txt", "r") as file:
                for line in file:
                    name, age, course = line.strip().split(",")
                    self.students.append(Student(name, int(age), course))
        except FileNotFoundError:
            pass




system = StudentSystem()
while(True):
        print("\n----Student Info System----")
        print("1)Add Student")
        print("2)View Students")
        print("3)Delete Student")
        print("4)Exit")
        choice=input("Pick A Number: ").lower()

        if choice=="1":
            system.addS()
        elif choice=="2":
            system.ViewS()
        elif choice=="3":
            system.DeleteS()
        elif choice=="4":
            print("EXITING PROGRAM...")
            break
        else:
            print("INCORRECT INPUT... TRY AGAIN")
