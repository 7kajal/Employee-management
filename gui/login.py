import tkinter as tk
from tkinter import messagebox
from database.mongodb_connection import get_database

db = get_database()
users = db["users"]

def login():
    u = username.get()
    p = password.get()

    if users.find_one({"username": u, "password": p}):
        root.destroy()
        import gui.employee_gui
    else:
        messagebox.showerror("Error", "Invalid Credentials")

root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

tk.Button(root, text="Login", command=login).pack()
root.mainloop()
