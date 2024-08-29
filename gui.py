import tkinter as tk
from tkinter import messagebox
import requests


def add_employee():
    employee_data = {
        "Department": entry_department.get(),
        "Name": entry_name.get(),
        "Designation": entry_designation.get(),
        "Email": entry_email.get(),
        "Address": entry_address.get(),
        "location": entry_location.get(),
        "DOB": entry_dob.get(),
        "DOJ": entry_doj.get(),
        "id_proof_type": entry_id_proof_type.get(),
        "id_proof": entry_id_proof.get(),
        "Gender": entry_gender.get(),
        "Phone": entry_phone.get(),
        "Country": entry_country.get(),
        "Salary": entry_salary.get()
    }

    response = requests.post("http://127.0.0.1:3031/employee", json=employee_data)

    if response.status_code == 201:
        messagebox.showinfo("Success", "User added successfully")
    else:
        messagebox.showerror("Error", f"Failed to add user: {response.json().get('message')}")


def get_all_employees():
    response = requests.get("http://127.0.0.1:3031/employee")
    if response.status_code == 200:
        employees = response.json()
        display_employees(employees)
    else:
        messagebox.showerror("Error", "Failed to retrieve employees")



def display_employees(employees):
    display_window = tk.Toplevel(root)
    display_window.title("Employees")
    
    for i, employee in enumerate(employees):
        tk.Label(display_window, text=f"Employee {i + 1}: {employee}").pack()


def update_employee():
    employee_data = {
        "Department": entry_department.get(),
        "Name": entry_name.get(),
        "Designation": entry_designation.get(),
        "Email": entry_email.get(),
        "Address": entry_address.get(),
        "location": entry_location.get(),
        "DOB": entry_dob.get(),
        "DOJ": entry_doj.get(),
        "id_proof_type": entry_id_proof_type.get(),
        "Gender": entry_gender.get(),
        "Phone": entry_phone.get(),
        "Country": entry_country.get(),
        "Salary": entry_salary.get()
    }

    emp_id = entry_id_proof.get()
    response = requests.put(f"http://127.0.0.1:3031/employee/{emp_id}", json=employee_data)

    if response.status_code == 200:
        messagebox.showinfo("Success", "User updated successfully")
    else:
        messagebox.showerror("Error", f"Failed to update user: {response.json().get('message')}")


def delete_employee():
    emp_id = entry_id_proof.get()
    response = requests.delete(f"http://127.0.0.1:3031/employee/{emp_id}")

    if response.status_code == 200:
        messagebox.showinfo("Success", "User deleted successfully")
    else:
        messagebox.showerror("Error", f"Failed to delete user: {response.json().get('message')}")



root = tk.Tk()
root.title("Employee Management")


labels = [
    "Department", "Name", "Designation", "Email", "Address", "Location",
    "DOB", "DOJ", "ID Proof Type", "ID Proof", "Gender", "Phone", "Country", "Salary"
]

entries = []
for label in labels:
    lbl = tk.Label(root, text=label)
    lbl.pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

(
    entry_department, entry_name, entry_designation, entry_email, entry_address,
    entry_location, entry_dob, entry_doj, entry_id_proof_type, entry_id_proof,
    entry_gender, entry_phone, entry_country, entry_salary
) = entries


btn_add = tk.Button(root, text="Add Employee", command=add_employee)
btn_add.pack()

btn_get_all = tk.Button(root, text="Get All Employees", command=get_all_employees)
btn_get_all.pack()

btn_update = tk.Button(root, text="Update Employee", command=update_employee)
btn_update.pack()

btn_delete = tk.Button(root, text="Delete Employee", command=delete_employee)
btn_delete.pack()


root.mainloop()
