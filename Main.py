import tkinter as tk
from tkinter import messagebox, Entry
from StudentSystem import StudentSystem

system = StudentSystem()

#Functions, here since I can't find how to put in different file.

root = tk.Tk()
root.title("Student Info System")
root.geometry("500x450")

def addStudent():
    name = input_name.get()
    age = input_age.get()
    course = input_course.get()

    if not name or not age or not course:
        messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED FOR ENTRANCE!!!")
        return
    try:
        system.addS(name, age, course)
        messagebox.showinfo("SUCCESS","STUDENT ADDED TO LIST OF ENROLLS")

        refreshList()
    except ValueError:
        messagebox.showerror("ERROR", "VALUE MUST BE ABOVE OR EQUAL TO 18!")

def refreshList():
    listbox.delete(0, tk.END)

    students=system.viewS()

    if not students:
        listbox.insert(tk.END, "NO STUDENT FOUND")

    for numbers, Student in enumerate(students, start=1):
        listbox.insert(tk.END, f"{numbers}. {Student}")


def deleteStudent():
    selected = listbox.curselection()

    if not selected:
        messagebox.showerror("ERROR", "NO STUDENT SELECTED, CLICK STUDENT TO SELECT!")
        return

    index=selected(0)
    removed=system.deleteS(index)

    if removed:
        messagebox.showinfo(f"Deleted: {removed.name}, {removed.age}, {removed.course}")

#MAIN GUI, like the buttons and things
listbox = tk.Listbox(root, width=60)
listbox.pack(pady=15)

tk.Label(root, text="NAME").pack()
input_name=tk.Entry(root)
input_name.pack()

tk.Label(root, text="AGE").pack()
input_age=tk.Entry(root)
input_age.pack()

tk.Label(root, text="COURSE").pack()
input_course=tk.Entry(root)
input_course.pack()

tk.Button(root, text="Add Student", command=addStudent).pack(pady=5)
tk.Button(root, text="Delete Student", command=deleteStudent).pack(pady=5)

refreshList()

root.mainloop()
