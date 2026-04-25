class Student: #Prints the name,age and course of students
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def __str__(self):
        return f"{self.name}, {self.age}, {self.course}"
    def Info(self):
        return str(self)
