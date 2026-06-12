from Student import Student

class StudentSystem:
    def __init__(self):
        self.students=[]
        self.load_file()

    #For File Handling

    def load_file(self):
        try:
            with open("Student Records.txt", "r") as file:
                for line in file:
                    name, age, course=line.strip().split(",")
                    self.students.append(Student(name.strip(), int(age), course.strip()))
        except FileNotFoundError:
            pass

    def save_file(self):
        with open("Student Records.txt", "w") as file:
            for student in self.students:
                file.write(f"{student.name}, {student.age}, {student.course}\n")

    def addS(self, name, age, course):
        age=int(age)

        if age < 18 or age > 100:
            raise ValueError()

        student = Student(name, age, course)
        self.students.append(student)
        self.save_file()

    def viewS(self): #able to view students in the box
        return [student.Info() for student in self.students]

    def deleteS(self, index): # for deleting students, it only functions if 0 is less than the number of corresponding student
        #and is less than the length of the list of students
        if 0 <= index < len(self.students):
            remove = self.students.pop(index)
            self.save_file()
            return remove
        return None
