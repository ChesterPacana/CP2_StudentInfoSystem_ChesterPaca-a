import sys,time,os
from Student import Student
from StudentSystem import StudentSystem

system = StudentSystem()
while(True):
        print("\n----Student Info System----")
        print("1)Add Student")
        print("2)View Students")
        print("3)Delete Student")
        print("4)Exit")
        choice=input("Pick A Number: ")

    
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
