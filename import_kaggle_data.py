import csv
from database.mongodb_connection import get_database

db = get_database()
employees = db["employees"]

employees.delete_many({})  # Optional: clear old data

with open("data/employees.csv", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = []
    for row in reader:
        data.append({
            "emp_id": int(row["Index"]),
            "first_name": row["First Name"],
            "last_name": row["Last Name"],
            "gender": row["Sex"],
            "email": row["Email"],
            "phone": row["Phone"],
            "dob": row["Date of birth"],
            "job_title": row["Job Title"]
        })

if data:
    employees.insert_many(data)
    print("✅ Employees imported successfully")
else:
    print("❌ No data found in CSV")
