import tkinter as tk
from tkinter import messagebox
from database.mongodb_connection import get_database

db = get_database()
users = db["users"]


def register():
    u = username.get().strip()
    p = password.get().strip()

    # Input validation
    if not u or not p:
        messagebox.showerror("Input Error", "Username and Password are required")
        return
    if len(u) < 3:
        messagebox.showerror("Input Error", "Username must be at least 3 characters")
        return
    if len(p) < 6:
        messagebox.showerror("Input Error", "Password must be at least 6 characters")
        return
    if users.find_one({"username": u}):
        messagebox.showerror("Error", "Username already exists")
        return

    # Insert new user
    users.insert_one({"username": u, "password": p})
    messagebox.showinfo("Success", "Registration successful")

    # Go back to login
    root.destroy()
    import gui.login


def go_to_login():
    """Navigate back to login window."""
    root.destroy()
    import gui.login


def on_close():
    """Confirm before closing the window."""
    if messagebox.askyesno("Exit", "Are you sure you want to close?"):
        root.destroy()


root = tk.Tk()
root.title("Register")
root.geometry("350x360")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_close)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

tk.Label(frame, text="Register", font=("Arial", 18, "bold")).pack(pady=(0, 20))

tk.Label(frame, text="Username", anchor="w").pack(fill="x")
username = tk.Entry(frame)
username.pack(fill="x", pady=(0, 10))

tk.Label(frame, text="Password", anchor="w").pack(fill="x")
password = tk.Entry(frame, show="*")
password.pack(fill="x", pady=(0, 20))

tk.Button(
    frame, text="Register", command=register, bg="#2196F3", fg="white", height=2
).pack(fill="x")

tk.Label(frame, text="").pack(pady=5)

tk.Button(
    frame, text="Back to Login", command=go_to_login, relief="flat", fg="#2196F3"
).pack()

root.mainloop()
