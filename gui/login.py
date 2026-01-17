import tkinter as tk
from tkinter import messagebox
from database.mongodb_connection import get_database

db = get_database()
users = db["users"]


def login():
    u = username.get().strip()
    p = password.get().strip()
    # Input validation

    if not u or not p:
        messagebox.showerror("Input Error", "Username and Password are required")
        return

    user = users.find_one({"username": u})

    if not user:
        messagebox.showerror("Error", "User does not exist")
        return

    if user["password"] != p:
        messagebox.showerror("Error", "Incorrect password")
        return

    root.destroy()
    import gui.employee_gui


def go_to_register():
    root.destroy()
    import gui.register


root = tk.Tk()
root.title("Login")
root.geometry("350x400")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

tk.Label(frame, text="Login", font=("Arial", 18, "bold")).pack(pady=(0, 20))

tk.Label(frame, text="Username", anchor="w").pack(fill="x")
username = tk.Entry(frame)
username.pack(fill="x", pady=(0, 10))

tk.Label(frame, text="Password", anchor="w").pack(fill="x")
password = tk.Entry(frame, show="*")
password.pack(fill="x", pady=(0, 20))

tk.Button(frame, text="Login", command=login, bg="#4CAF50", fg="white", height=2).pack(
    fill="x"
)

tk.Label(frame, text="").pack(pady=5)
tk.Label(frame, text="Don't have an account?").pack()

tk.Button(
    frame, text="Register", command=go_to_register, fg="#4CAF50", relief="flat"
).pack()

root.mainloop()
