import csv
from database.mongodb_connection import get_database

# Connect to MongoDB
db = get_database()
employees = db["employees"]

# Clear existing employee records
employees.delete_many({})

# Read employee data from CSV file
with open("data/employees.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = []

    # Convert each CSV row into MongoDB document format
    for row in reader:
        data.append(
            {
                "emp_id": int(row["Index"]),
                "first_name": row["First Name"],
                "last_name": row["Last Name"],
                "gender": row["Sex"],
                "email": row["Email"],
                "phone": row["Phone"],
                "dob": row["Date of birth"],
                "job_title": row["Job Title"],
            }
        )

# Insert all records into database
if data:
    employees.insert_many(data)
    print("Employees imported successfully")
else:
    print("No data found in CSV")
