import tkinter as tk
from tkinter import ttk, simpledialog
from datetime import datetime
from math import pi, sin, cos
import random

class Employee:
    def __init__(self, name, salary, leaves):
        self.name = name
        self.salary = salary
        self.leaves = leaves
        self.net_salary = salary

class Admin(Employee):
    def __init__(self, name, salary, leaves):
        super().__init__(name, salary, leaves)
        self.is_admin = True

    def fire_employee(self, employee):
        employees.remove(employee)

    def promote_employee(self, employee, new_salary):
        employee.salary = new_salary
        employee.net_salary = new_salary

class LoginWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Login")
        self.geometry("800x600")
        self.configure(bg="navy")

        # Create the login form
        self.canvas = tk.Canvas(self, width=800, height=600, bg="navy")
        self.canvas.pack()

        # Draw the company logo
        logo_radius = 100
        logo_x = 400
        logo_y = 300
        self.canvas.create_oval(logo_x - logo_radius, logo_y - logo_radius, logo_x + logo_radius, logo_y + logo_radius, fill="white", outline="")

        # Draw the company name
        company_name = "Acme Corporation"
        self.canvas.create_text(logo_x, logo_y, text=company_name, font=("Arial", 24, "bold"), fill="navy")

        # Draw the login form
        self.username_label = tk.Label(self, text="Username:", font=("Arial", 16), bg="navy", fg="white")
        self.username_label.place(x=300, y=400)
        self.username_entry = tk.Entry(self, font=("Arial", 16), bg="white", fg="navy")
        self.username_entry.place(x=450, y=400)

        self.password_label = tk.Label(self, text="Password:", font=("Arial", 16), bg="navy", fg="white")
        self.password_label.place(x=300, y=450)
        self.password_entry = tk.Entry(self, font=("Arial", 16), bg="white", fg="navy", show="*")
        self.password_entry.place(x=450, y=450)

        self.login_button = tk.Button(self, text="Login", font=("Arial", 16), bg="white", fg="navy", command=self.login)
        self.login_button.place(x=400, y=500)

        # Draw the background stars
        for _ in range(100):
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            size = random.randint(1, 3)
            self.canvas.create_oval(x - size, y - size, x + size, y + size, fill="white", outline="")

    def login(self):
        # Perform login logic here
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Validate the username and password, and then open the AdminWindow
        if username == "admin" and password == "password":
            self.destroy()  # Close the LoginWindow
            AdminWindow(self.master)
        else:
            # Display an error message or ask the user to try again
            pass

class AdminWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Admin Panel")
        self.geometry("800x600")
        self.configure(bg="navy")

        self.canvas = tk.Canvas(self, width=800, height=600, bg="navy")
        self.canvas.pack()

        self.tree = ttk.Treeview(self.canvas, columns=("Name", "Salary", "Leaves", "Net Salary"), show="headings")
        self.tree.place(x=100, y=100, width=600, height=400)

        self.tree.heading("Name", text="Name", anchor="center")
        self.tree.heading("Salary", text="Salary", anchor="center")
        self.tree.heading("Leaves", text="Leaves", anchor="center")
        self.tree.heading("Net Salary", text="Net Salary", anchor="center")

        for emp in employees:
            self.tree.insert("", "end", values=(emp.name, emp.salary, emp.leaves, emp.net_salary))

        self.tree.bind("<Double-1>", self.show_employee_details)

        self.fire_button = tk.Button(self.canvas, text="Fire Employee", font=("Arial", 14), bg="white", fg="navy", command=self.fire_employee)
        self.fire_button.place(x=100, y=520)

        self.promote_button = tk.Button(self.canvas, text="Promote Employee", font=("Arial", 14), bg="white", fg="navy", command=self.promote_employee)
        self.promote_button.place(x=300, y=520)

        self.close_button = tk.Button(self.canvas, text="Close", font=("Arial", 14), bg="white", fg="navy", command=self.destroy)
        self.close_button.place(x=500, y=520)

    def show_employee_details(self, event):
        selected_item = self.tree.selection()[0]
        employee = [emp for emp in employees if emp.name == self.tree.item(selected_item, "values")[0]][0]
        EmployeeDetailsWindow(self, employee)

    def fire_employee(self):
        selected_item = self.tree.selection()[0]
        employee = [emp for emp in employees if emp.name == self.tree.item(selected_item, "values")[0]][0]
        admin.fire_employee(employee)
        self.tree.delete(selected_item)

    def promote_employee(self):
        selected_item = self.tree.selection()[0]
        employee = [emp for emp in employees if emp.name == self.tree.item(selected_item, "values")[0]][0]
        new_salary = int(simpledialog.askstring("Promote Employee", f"Enter new salary for {employee.name}:"))
        admin.promote_employee(employee, new_salary)
        self.tree.item(selected_item, values=(employee.name, employee.salary, employee.leaves, employee.net_salary))

class EmployeeDetailsWindow(tk.Toplevel):
    def __init__(self, master, employee):
        super().__init__(master)
        self.title(f"{employee.name}'s Details")
        self.geometry("400x300")
        self.configure(bg="navy")

        self.canvas = tk.Canvas(self, width=400, height=300, bg="navy")
        self.canvas.pack()

        self.name_label = tk.Label(self.canvas, text=f"Name: {employee.name}", font=("Arial", 16), bg="navy", fg="white")
        self.name_label.place(x=50, y=50)

        self.salary_label = tk.Label(self.canvas, text=f"Salary: {employee.salary}", font=("Arial", 16), bg="navy", fg="white")
        self.salary_label.place(x=50, y=100)

        self.leaves_label = tk.Label(self.canvas, text=f"Leaves: {employee.leaves}", font=("Arial", 16), bg="navy", fg="white")
        self.leaves_label.place(x=50, y=150)

        self.net_salary_label = tk.Label(self.canvas, text=f"Net Salary: {employee.net_salary}", font=("Arial", 16), bg="navy", fg="white")
        self.net_salary_label.place(x=50, y=200)

# Create some sample employees and an admin
employees = [
    Employee("John Doe", 5000, 20),
    Employee("Jane Smith", 6000, 15),
Employee("Bob Johnson", 4500, 25),
]

admin = Admin("Admin", 8000, 30)

root = tk.Tk()
root.title("Login")
LoginWindow(root)
root.mainloop()