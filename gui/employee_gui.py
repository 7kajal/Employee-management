import tkinter as tk
from tkinter import ttk, messagebox
from database.mongodb_connection import get_database
import csv

# ---------------- DB ----------------
db = get_database()
employees = db["employees"]

# ---------------- ROOT ----------------
root = tk.Tk()
root.title("Employee Management System")
root.geometry("1100x550")
root.configure(bg="#f4f6f9")

# ---------------- UTIL ----------------
def get_next_emp_id():
    last = employees.find_one(sort=[("emp_id", -1)])
    return last["emp_id"] + 1 if last else 1

def refresh_table(data=None):
    table.delete(*table.get_children())
    records = data if data else employees.find()
    for emp in records:
        table.insert("", "end", values=(
            emp["emp_id"],
            emp["first_name"],
            emp["last_name"],
            emp["gender"],
            emp["email"],
            emp["phone"],
            emp["dob"],
            emp["job_title"]
        ))

# ---------------- SEARCH ----------------
def search_employee():
    key = search_entry.get()
    if key == "":
        refresh_table()
        return

    result = employees.find({
        "$or": [
            {"first_name": {"$regex": key, "$options": "i"}},
            {"phone": {"$regex": key}}
        ]
    })
    refresh_table(result)

# ---------------- ADD WINDOW ----------------
def open_add_window():
    win = tk.Toplevel(root)
    win.title("Add Employee")
    win.geometry("400x420")
    win.grab_set()

    labels = ["First Name", "Last Name", "Gender", "Email", "Phone", "DOB", "Job Title"]
    entries = []

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, pady=5, padx=5, sticky="w")
        e = tk.Entry(win, width=30)
        e.grid(row=i, column=1, pady=5)
        entries.append(e)

    def save():
        if entries[0].get() == "" or entries[3].get() == "":
            messagebox.showerror("Validation Error", "First Name and Email are required")
            return

        employees.insert_one({
            "emp_id": get_next_emp_id(),
            "first_name": entries[0].get(),
            "last_name": entries[1].get(),
            "gender": entries[2].get(),
            "email": entries[3].get(),
            "phone": entries[4].get(),
            "dob": entries[5].get(),
            "job_title": entries[6].get()
        })

        refresh_table()
        win.destroy()

    tk.Button(win, text="Add Employee", bg="#2ecc71", fg="white", command=save)\
        .grid(row=8, column=0, columnspan=2, pady=15)

# ---------------- UPDATE ----------------
def open_update_window():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to update")
        return

    data = table.item(selected)["values"]
    win = tk.Toplevel(root)
    win.title("Update Employee")
    win.geometry("400x420")
    win.grab_set()

    fields = ["First Name","Last Name","Gender","Email","Phone","DOB","Job Title"]
    values = data[1:]
    entries = []

    for i, (f, v) in enumerate(zip(fields, values)):
        tk.Label(win, text=f).grid(row=i, column=0, pady=5, sticky="w")
        e = tk.Entry(win, width=30)
        e.insert(0, v)
        e.grid(row=i, column=1, pady=5)
        entries.append(e)

    def update():
        employees.update_one(
            {"emp_id": data[0]},
            {"$set": {
                "first_name": entries[0].get(),
                "last_name": entries[1].get(),
                "gender": entries[2].get(),
                "email": entries[3].get(),
                "phone": entries[4].get(),
                "dob": entries[5].get(),
                "job_title": entries[6].get()
            }}
        )
        refresh_table()
        win.destroy()

    tk.Button(win, text="Update", bg="#3498db", fg="white", command=update)\
        .grid(row=8, column=0, columnspan=2, pady=15)

# ---------------- DELETE ----------------
def delete_employee():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to delete")
        return

    emp_id = table.item(selected)["values"][0]
    if messagebox.askyesno("Confirm", "Delete selected employee?"):
        employees.delete_one({"emp_id": emp_id})
        refresh_table()

# ---------------- EXPORT ----------------
def export_csv():
    with open("export/employees_export.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Index","First Name","Last Name","Sex",
            "Email","Phone","Date of birth","Job Title"
        ])
        for emp in employees.find():
            writer.writerow([
                emp["emp_id"],
                emp["first_name"],
                emp["last_name"],
                emp["gender"],
                emp["email"],
                emp["phone"],
                emp["dob"],
                emp["job_title"]
            ])
    messagebox.showinfo("Exported", "CSV exported successfully")

# ---------------- TOP SEARCH BAR ----------------
top = tk.Frame(root, bg="#f4f6f9")
top.pack(fill="x", padx=10, pady=10)

tk.Label(top, text="Search (Name / Phone):", bg="#f4f6f9").pack(side="left")
search_entry = tk.Entry(top, width=30)
search_entry.pack(side="left", padx=5)
tk.Button(top, text="Search", command=search_employee).pack(side="left")

# ---------------- MAIN AREA ----------------
main = tk.Frame(root)
main.pack(fill="both", expand=True, padx=10)

# TABLE
columns = ("ID","First Name","Last Name","Gender","Email","Phone","DOB","Job Title")
table = ttk.Treeview(main, columns=columns, show="headings", height=15)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=130)

table.pack(side="left", fill="both", expand=True)

# ACTION PANEL
actions = tk.Frame(main, width=200, bg="#ecf0f1")
actions.pack(side="right", fill="y", padx=10)

tk.Label(actions, text="Actions", bg="#ecf0f1", font=("Arial", 12, "bold")).pack(pady=10)

tk.Button(actions, text="➕ Add Employee", width=18, command=open_add_window).pack(pady=5)
tk.Button(actions, text="✏ Update Employee", width=18, command=open_update_window).pack(pady=5)
tk.Button(actions, text="🗑 Delete Employee", width=18, command=delete_employee).pack(pady=5)
tk.Button(actions, text="⬇ Export CSV", width=18, command=export_csv).pack(pady=20)

# ---------------- LOAD DATA ON START ----------------
refresh_table()
root.mainloop()
