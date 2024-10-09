# import tkinter as tk
# from tkinter import messagebox, ttk
# import requests
# import re


# def validate_alpha(entry):
#     if not re.match("^[A-Za-z\s]+$", entry.get()):
#         messagebox.showerror("Invalid Input", "This field accepts only alphabetic characters.")
#         entry.focus_set()
#         return False
#     return True

# def validate_numeric(entry):
#     if not entry.get().isdigit():
#         messagebox.showerror("Invalid Input", "This field accepts only numeric characters.")
#         entry.focus_set()
#         return False
#     return True

# def validate_email(entry):
#     if not re.match(r"[^@]+@[^@]+\.[^@]+", entry.get()):
#         messagebox.showerror("Invalid Input", "Please enter a valid email address.")
#         entry.focus_set()
#         return False
#     return True

# def validate_date(entry):
    
#     if not re.match(r"\d{4}-\d{2}-\d{2}", entry.get()):
#         messagebox.showerror("Invalid Input", "Please enter a valid date in YYYY-MM-DD format.")
#         entry.focus_set()
#         return False
#     return True

# def validate_fields():
#     if not validate_alpha(entry_name):
#         return False
#     if not validate_email(entry_email):
#         return False
#     if not validate_numeric(entry_phone):
#         return False
#     if not validate_numeric(entry_salary):
#         return False
#     if not validate_date(entry_dob):
#         return False
#     if not validate_date(entry_doj):
#         return False
#     return True

# # Dropdown creation function
# def create_dropdown(parent, label_text, options, row, column):
#     lbl = tk.Label(parent, text=label_text, bg='#283655', fg='white', font=("Arial", 12, "bold"))
#     lbl.grid(row=row, column=column, padx=10, pady=5, sticky='w')
#     dropdown = ttk.Combobox(parent, values=options, state="readonly", font=("Arial", 10))
#     dropdown.grid(row=row, column=column+1, padx=10, pady=5, sticky='w')
#     dropdown.current(0)  # Set default value
#     return dropdown

# # Add Employee Function
# def add_employee():
#     if not validate_fields():
#         return
    
#     employee_data = {
#         "Department": dropdown_department.get(),
#         "Name": entry_name.get(),
#         "Designation": entry_designation.get(),
#         "Email": entry_email.get(),
#         "Address": entry_address.get(),
#         "location": entry_location.get(),
#         "DOB": entry_dob.get(),
#         "DOJ": entry_doj.get(),
#         "id_proof_type": dropdown_id_proof_type.get(),
#         "id_proof": entry_id_proof.get(),
#         "Gender": dropdown_gender.get(),
#         "Phone": entry_phone.get(),
#         "Country": entry_country.get(),
#         "Salary": entry_salary.get()
#     }

#     response = requests.post("http://127.0.0.1:3031/employee", json=employee_data)

#     if response.status_code == 201:
#         messagebox.showinfo("Success", "User added successfully")
#         clear_fields()
#     else:
#         messagebox.showerror("Error", f"Failed to add user: {response.json().get('message')}")

# # Fetch all employees and display
# def get_all_employees():
#     response = requests.get("http://127.0.0.1:3031/employee")
#     if response.status_code == 200:
#         employees = response.json()
#         display_employees(employees)
#     else:
#         messagebox.showerror("Error", "Failed to retrieve employees")

# def display_employees(employees):
#     display_window = tk.Toplevel(root)
#     display_window.title("Employees")
#     display_window.geometry("600x400")
    
#     canvas = tk.Canvas(display_window, bg='#D0E8F2')
#     scrollbar = tk.Scrollbar(display_window, orient="vertical", command=canvas.yview)
#     scrollable_frame = tk.Frame(canvas, bg='#D0E8F2')

#     scrollable_frame.bind(
#         "<Configure>",
#         lambda e: canvas.configure(
#             scrollregion=canvas.bbox("all")
#         )
#     )

#     canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
#     canvas.configure(yscrollcommand=scrollbar.set)

#     canvas.pack(side="left", fill="both", expand=True)
#     scrollbar.pack(side="right", fill="y")

#     for i, employee in enumerate(employees):
#         emp_text = f"Employee {i + 1}:\n" + "\n".join([f"{key}: {value}" for key, value in employee.items()])
#         lbl = tk.Label(scrollable_frame, text=emp_text, bg='#D0E8F2', font=("Arial", 10), justify='left', anchor='w')
#         lbl.pack(padx=10, pady=5, fill='x')

# # Update Employee Function
# def update_employee():
#     if not validate_fields():
#         return

#     emp_id = entry_id_proof.get()
#     if not emp_id:
#         messagebox.showerror("Input Error", "Please enter the ID Proof to update the employee.")
#         return

#     employee_data = {
#         "Department": dropdown_department.get(),
#         "Name": entry_name.get(),
#         "Designation": entry_designation.get(),
#         "Email": entry_email.get(),
#         "Address": entry_address.get(),
#         "location": entry_location.get(),
#         "DOB": entry_dob.get(),
#         "DOJ": entry_doj.get(),
#         "id_proof_type": dropdown_id_proof_type.get(),
#         "Gender": dropdown_gender.get(),
#         "Phone": entry_phone.get(),
#         "Country": entry_country.get(),
#         "Salary": entry_salary.get()
#     }

#     response = requests.put(f"http://127.0.0.1:3031/employee/{emp_id}", json=employee_data)

#     if response.status_code == 200:
#         messagebox.showinfo("Success", "User updated successfully")
#         clear_fields()
#     else:
#         messagebox.showerror("Error", f"Failed to update user: {response.json().get('message')}")

# # Delete Employee Function
# def delete_employee():
#     emp_id = entry_id_proof.get()
#     if not emp_id:
#         messagebox.showerror("Input Error", "Please enter the ID Proof to delete the employee.")
#         return

#     confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this employee?")
#     if not confirm:
#         return

#     response = requests.delete(f"http://127.0.0.1:3031/employee/{emp_id}")

#     if response.status_code == 200:
#         messagebox.showinfo("Success", "User deleted successfully")
#         clear_fields()
#     else:
#         messagebox.showerror("Error", f"Failed to delete user: {response.json().get('message')}")

# # Clear all input fields
# def clear_fields():
#     department_options.set(dropdown_department['values'][0])
#     entry_name.delete(0, tk.END)
#     entry_designation.delete(0, tk.END)
#     entry_email.delete(0, tk.END)
#     entry_address.delete(0, tk.END)
#     entry_location.delete(0, tk.END)
#     entry_dob.delete(0, tk.END)
#     entry_doj.delete(0, tk.END)
#     entry_id_proof.delete(0, tk.END)
#     dropdown_id_proof_type.set(dropdown_id_proof_type['values'][0])
#     dropdown_gender.set(dropdown_gender['values'][0])
#     entry_phone.delete(0, tk.END)
#     entry_country.delete(0, tk.END)
#     entry_salary.delete(0, tk.END)

# # GUI setup
# root = tk.Tk()
# root.title("Employee Management System")
# root.geometry("700x700")
# root.configure(bg='#283655')

# # Header
# header = tk.Label(root, text="Employee Management", bg='#283655', fg='white', font=("Helvetica", 18, "bold"))
# header.pack(pady=10)

# # Create a frame for the form
# form_frame = tk.Frame(root, bg='#283655')
# form_frame.pack(padx=20, pady=10, fill='both', expand=True)

# # Labels and Entries
# # Using grid for better layout
# labels = [
#     "Department", "Name", "Designation", "Email", "Address", "Location",
#     "DOB (YYYY-MM-DD)", "DOJ (YYYY-MM-DD)", "ID Proof Type", "ID Proof", "Gender", "Phone", "Country", "Salary"
# ]

# row = 0

# # Department Dropdown
# department_options = ["HR", "Software Engineering", "Marketing", "Finance", "Sales", "Operations"]
# lbl_department = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_department.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# dropdown_department = ttk.Combobox(form_frame, values=department_options, state="readonly", font=("Arial", 10))
# dropdown_department.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# dropdown_department.current(0)
# row += 1

# # Name Entry
# lbl_name = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_name.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# entry_name = tk.Entry(form_frame, font=("Arial", 10))
# entry_name.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# entry_name.bind("<FocusOut>", lambda event: validate_alpha(entry_name))
# row += 1

# # Designation Entry
# lbl_designation = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_designation.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# entry_designation = tk.Entry(form_frame, font=("Arial", 10))
# entry_designation.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# row += 1

# # Email Entry
# lbl_email = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_email.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# entry_email = tk.Entry(form_frame, font=("Arial", 10))
# entry_email.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# entry_email.bind("<FocusOut>", lambda event: validate_email(entry_email))
# row += 1

# # Address Entry
# lbl_address = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_address.grid(row=row, column=0, padx=10, pady=5, sticky='nw')
# entry_address = tk.Text(form_frame, height=3, width=30, font=("Arial", 10))
# entry_address.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# row += 1

# # Location Entry
# lbl_location = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_location.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# entry_location = tk.Entry(form_frame, font=("Arial", 10))
# entry_location.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# row += 1

# # DOB Entry
# lbl_dob = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_dob.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# entry_dob = tk.Entry(form_frame, font=("Arial", 10))
# entry_dob.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# entry_dob.bind("<FocusOut>", lambda event: validate_date(entry_dob))
# row += 1

# # DOJ Entry
# lbl_doj = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_doj.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# entry_doj = tk.Entry(form_frame, font=("Arial", 10))
# entry_doj.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# entry_doj.bind("<FocusOut>", lambda event: validate_date(entry_doj))
# row += 1

# # ID Proof Type Dropdown
# id_proof_options = ["Aadhar", "Passport", "Driving License", "Voter ID"]
# lbl_id_proof_type = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_id_proof_type.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# dropdown_id_proof_type = ttk.Combobox(form_frame, values=id_proof_options, state="readonly", font=("Arial", 10))
# dropdown_id_proof_type.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# dropdown_id_proof_type.current(0)
# row += 1

# # ID Proof Entry
# lbl_id_proof = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_id_proof.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# entry_id_proof = tk.Entry(form_frame, font=("Arial", 10))
# entry_id_proof.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# row += 1

# # Gender Dropdown
# gender_options = ["Male", "Female", "Other"]
# lbl_gender = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_gender.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# dropdown_gender = ttk.Combobox(form_frame, values=gender_options, state="readonly", font=("Arial", 10))
# dropdown_gender.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# dropdown_gender.current(0)
# row += 1

# # Phone Entry
# lbl_phone = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_phone.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# entry_phone = tk.Entry(form_frame, font=("Arial", 10))
# entry_phone.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# entry_phone.bind("<FocusOut>", lambda event: validate_numeric(entry_phone))
# row += 1

# # Country Entry
# lbl_country = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_country.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# entry_country = tk.Entry(form_frame, font=("Arial", 10))
# entry_country.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# row += 1

# # Salary Entry
# lbl_salary = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 12, "bold"))
# lbl_salary.grid(row=row, column=0, padx=10, pady=5, sticky='w')
# entry_salary = tk.Entry(form_frame, font=("Arial", 10))
# entry_salary.grid(row=row, column=1, padx=10, pady=5, sticky='w')
# entry_salary.bind("<FocusOut>", lambda event: validate_numeric(entry_salary))
# row += 1

# # Buttons Frame
# buttons_frame = tk.Frame(root, bg='#283655')
# buttons_frame.pack(pady=20)

# # Buttons with styling
# btn_style = {
#     'font': ("Arial", 12, "bold"),
#     'width': 15,
#     'fg': 'white',
#     'bd': 0,
#     'cursor': 'hand2'
# }

# btn_add = tk.Button(buttons_frame, text="Add Employee", command=add_employee, bg='#4CAF50', **btn_style)
# btn_add.grid(row=0, column=0, padx=10, pady=5)

# btn_get_all = tk.Button(buttons_frame, text="Get All Employees", command=get_all_employees, bg='#2196F3', **btn_style)
# btn_get_all.grid(row=0, column=1, padx=10, pady=5)

# btn_update = tk.Button(buttons_frame, text="Update Employee", command=update_employee, bg='#FFC107', **btn_style)
# btn_update.grid(row=1, column=0, padx=10, pady=5)

# btn_delete = tk.Button(buttons_frame, text="Delete Employee", command=delete_employee, bg='#F44336', **btn_style)
# btn_delete.grid(row=1, column=1, padx=10, pady=5)


# root.mainloop()

import tkinter as tk
from tkinter import messagebox, ttk
import requests
import re

def validate_alpha(entry):
    if not re.match("^[A-Za-z\s]+$", entry.get()):
        messagebox.showerror("Invalid Input", "This field accepts only alphabetic characters.")
        entry.focus_set()
        return False
    return True

def validate_numeric(entry):
    if not entry.get().isdigit():
        messagebox.showerror("Invalid Input", "This field accepts only numeric characters.")
        entry.focus_set()
        return False
    return True

def validate_email(entry):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", entry.get()):
        messagebox.showerror("Invalid Input", "Please enter a valid email address.")
        entry.focus_set()
        return False
    return True

def validate_date(entry):
    if not re.match(r"\d{4}-\d{2}-\d{2}", entry.get()):
        messagebox.showerror("Invalid Input", "Please enter a valid date in YYYY-MM-DD format.")
        entry.focus_set()
        return False
    return True

def validate_fields():
    if not validate_alpha(entry_name):
        return False
    if not validate_email(entry_email):
        return False
    if not validate_numeric(entry_phone):
        return False
    if not validate_numeric(entry_salary):
        return False
    if not validate_date(entry_dob):
        return False
    if not validate_date(entry_doj):
        return False
    return True

def create_dropdown(parent, label_text, options, row, column):
    lbl = tk.Label(parent, text=label_text, bg='#283655', fg='white', font=("Arial", 10, "bold"))
    lbl.grid(row=row, column=column, padx=5, pady=3, sticky='w')
    dropdown = ttk.Combobox(parent, values=options, state="readonly", font=("Arial", 8))
    dropdown.grid(row=row, column=column+1, padx=5, pady=3, sticky='w')
    dropdown.current(0)
    return dropdown

def add_employee():
    if not validate_fields():
        return
    
    employee_data = {
        "Department": dropdown_department.get(),
        "Name": entry_name.get(),
        "Designation": entry_designation.get(),
        "Email": entry_email.get(),
        "Address": entry_address.get(),
        "Location": entry_location.get(),
        "DOB": entry_dob.get(),
        "DOJ": entry_doj.get(),
        "ID Proof Type": dropdown_id_proof_type.get(),
        "ID Proof": entry_id_proof.get(),
        "Gender": dropdown_gender.get(),
        "Phone": entry_phone.get(),
        "Country": entry_country.get(),
        "Salary": entry_salary.get()
    }

    response = requests.post("http://127.0.0.1:3301/employee", json=employee_data)

    if response.status_code == 201:
        messagebox.showinfo("Success", "User added successfully")
        clear_fields()
    else:
        messagebox.showerror("Error", f"Failed to add user: {response.json().get('message')}")

def get_all_employees():
    response = requests.get("http://127.0.0.1:3301/employee")
    if response.status_code == 200:
        employees = response.json()
        display_employees(employees)
    else:
        messagebox.showerror("Error", "Failed to retrieve employees")

def display_employees(employees):
    display_window = tk.Toplevel(root)
    display_window.title("Employees")
    display_window.geometry("500x300")
    
    canvas = tk.Canvas(display_window, bg='#D0E8F2')
    scrollbar = tk.Scrollbar(display_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='#D0E8F2')

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for i, employee in enumerate(employees):
        emp_text = f"Employee {i + 1}:\n" + "\n".join([f"{key}: {value}" for key, value in employee.items()])
        lbl = tk.Label(scrollable_frame, text=emp_text, bg='#D0E8F2', font=("Arial", 8), justify='left', anchor='w')
        lbl.pack(padx=5, pady=3, fill='x')

def update_employee():
    if not validate_fields():
        return

    emp_id = entry_id_proof.get()
    if not emp_id:
        messagebox.showerror("Input Error", "Please enter the ID Proof to update the employee.")
        return

    employee_data = {
        "Department": dropdown_department.get(),
        "Name": entry_name.get(),
        "Designation": entry_designation.get(),
        "Email": entry_email.get(),
        "Address": entry_address.get(),
        "Location": entry_location.get(),
        "DOB": entry_dob.get(),
        "DOJ": entry_doj.get(),
        "ID Proof Type": dropdown_id_proof_type.get(),
        "Gender": dropdown_gender.get(),
        "Phone": entry_phone.get(),
        "Country": entry_country.get(),
        "Salary": entry_salary.get()
    }

    response = requests.put(f"http://127.0.0.1:3301/employee/{emp_id}", json=employee_data)

    if response.status_code == 200:
        messagebox.showinfo("Success", "User updated successfully")
        clear_fields()
    else:
        messagebox.showerror("Error", f"Failed to update user: {response.json().get('message')}")

def delete_employee():
    emp_id = entry_id_proof.get()
    if not emp_id:
        messagebox.showerror("Input Error", "Please enter the ID Proof to delete the employee.")
        return

    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this employee?")
    if not confirm:
        return

    response = requests.delete(f"http://127.0.0.1:3301/employee/{emp_id}")

    if response.status_code == 200:
        messagebox.showinfo("Success", "User deleted successfully")
        clear_fields()
    else:
        messagebox.showerror("Error", f"Failed to delete user: {response.json().get('message')}")

def clear_fields():
    dropdown_department.set(department_options[0])
    entry_name.delete(0, tk.END)
    entry_designation.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(1.0, tk.END)
    entry_location.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_doj.delete(0, tk.END)
    entry_id_proof.delete(0, tk.END)
    dropdown_id_proof_type.set(id_proof_options[0])
    dropdown_gender.set(gender_options[0])
    entry_phone.delete(0, tk.END)
    entry_country.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

root = tk.Tk()
root.title("Employee Management System")
root.geometry("600x600")
root.configure(bg='#283655')

header = tk.Label(root, text="Employee Management", bg='#283655', fg='white', font=("Helvetica", 14, "bold"))
header.pack(pady=5)

form_frame = tk.Frame(root, bg='#283655')
form_frame.pack(padx=15, pady=5, fill='both', expand=True)

labels = [
    "Department", "Name", "Designation", "Email", "Address", "Location",
    "DOB (YYYY-MM-DD)", "DOJ (YYYY-MM-DD)", "ID Proof Type", "ID Proof", "Gender", "Phone", "Country", "Salary"
]

row = 0

department_options = ["HR", "Software Engineering", "Marketing", "Finance", "Sales", "Operations"]
dropdown_department = create_dropdown(form_frame, labels[row], department_options, row, 0)
row += 1

lbl_name = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_name.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_name = tk.Entry(form_frame, font=("Arial", 8))
entry_name.grid(row=row, column=1, padx=5, pady=3, sticky='w')
entry_name.bind("<FocusOut>", lambda event: validate_alpha(entry_name))
row += 1

lbl_designation = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_designation.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_designation = tk.Entry(form_frame, font=("Arial", 8))
entry_designation.grid(row=row, column=1, padx=5, pady=3, sticky='w')
row += 1

lbl_email = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_email.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_email = tk.Entry(form_frame, font=("Arial", 8))
entry_email.grid(row=row, column=1, padx=5, pady=3, sticky='w')
entry_email.bind("<FocusOut>", lambda event: validate_email(entry_email))
row += 1

lbl_address = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_address.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_address = tk.Text(form_frame, height=3, font=("Arial", 8))
entry_address.grid(row=row, column=1, padx=5, pady=3, sticky='w')
row += 1

lbl_location = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_location.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_location = tk.Entry(form_frame, font=("Arial", 8))
entry_location.grid(row=row, column=1, padx=5, pady=3, sticky='w')
row += 1

lbl_dob = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_dob.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_dob = tk.Entry(form_frame, font=("Arial", 8))
entry_dob.grid(row=row, column=1, padx=5, pady=3, sticky='w')
entry_dob.bind("<FocusOut>", lambda event: validate_date(entry_dob))
row += 1

lbl_doj = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_doj.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_doj = tk.Entry(form_frame, font=("Arial", 8))
entry_doj.grid(row=row, column=1, padx=5, pady=3, sticky='w')
entry_doj.bind("<FocusOut>", lambda event: validate_date(entry_doj))
row += 1

id_proof_options = ["Aadhaar", "Passport", "Driving License", "Voter ID"]
dropdown_id_proof_type = create_dropdown(form_frame, labels[row], id_proof_options, row, 0)
row += 1

lbl_id_proof = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_id_proof.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_id_proof = tk.Entry(form_frame, font=("Arial", 8))
entry_id_proof.grid(row=row, column=1, padx=5, pady=3, sticky='w')
entry_id_proof.bind("<FocusOut>", lambda event: validate_numeric(entry_id_proof))
row += 1

gender_options = ["Male", "Female", "Other"]
dropdown_gender = create_dropdown(form_frame, labels[row], gender_options, row, 0)
row += 1

lbl_phone = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_phone.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_phone = tk.Entry(form_frame, font=("Arial", 8))
entry_phone.grid(row=row, column=1, padx=5, pady=3, sticky='w')
entry_phone.bind("<FocusOut>", lambda event: validate_numeric(entry_phone))
row += 1

lbl_country = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_country.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_country = tk.Entry(form_frame, font=("Arial", 8))
entry_country.grid(row=row, column=1, padx=5, pady=3, sticky='w')
row += 1

lbl_salary = tk.Label(form_frame, text=labels[row], bg='#283655', fg='white', font=("Arial", 10, "bold"))
lbl_salary.grid(row=row, column=0, padx=5, pady=3, sticky='w')
entry_salary = tk.Entry(form_frame, font=("Arial", 8))
entry_salary.grid(row=row, column=1, padx=5, pady=3, sticky='w')
entry_salary.bind("<FocusOut>", lambda event: validate_numeric(entry_salary))
row += 1

button_frame = tk.Frame(root, bg='#283655')
button_frame.pack(pady=10)

btn_add = tk.Button(button_frame, text="Add Employee", command=add_employee, bg='#4A6A8A', fg='white', font=("Arial", 10, "bold"))
btn_add.grid(row=0, column=0, padx=5)

btn_get = tk.Button(button_frame, text="Get All Employees", command=get_all_employees, bg='#4A6A8A', fg='white', font=("Arial", 10, "bold"))
btn_get.grid(row=0, column=1, padx=5)

btn_update = tk.Button(button_frame, text="Update Employee", command=update_employee, bg='#4A6A8A', fg='white', font=("Arial", 10, "bold"))
btn_update.grid(row=0, column=2, padx=5)

btn_delete = tk.Button(button_frame, text="Delete Employee", command=delete_employee, bg='#4A6A8A', fg='white', font=("Arial", 10, "bold"))
btn_delete.grid(row=0, column=3, padx=5)

btn_clear = tk.Button(button_frame, text="Clear Fields", command=clear_fields, bg='#4A6A8A', fg='white', font=("Arial", 10, "bold"))
btn_clear.grid(row=0, column=4, padx=5)

root.mainloop()

