import tkinter as tk
from tkinter import messagebox
from database.mongodb_connection import get_database

db = get_database()
users = db["users"]

def register():
    u = username.get()
    p = password.get()
    
    user=users.find_one({"username": u})

    if not u or not p:
        print("All fields required.")

    if user:
        print("user exist")
        return

    final = users.insert_one({"username": u,"password":p,})
    print(final)

   
root = tk.Tk()
root.title("Register")

tk.Label(root, text="Username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()



tk.Button(root, text="Register", command=register).pack()
root.mainloop()
