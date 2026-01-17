# Employee Management System

![image](./screenshots/fullScreen.png)

## Description

A GUI-based Employee Management System using Python, Tkinter, and MongoDB.

## Features

- User Login
- CRUD Operations
- Search
- Input Validation
- CSV Export
- MongoDB Integration

## Technologies

- Python
- Tkinter
- MongoDB
- PyMongo

## Sample Data for reference

There is sample data present in the `data/` folder.  
(Source: [Kaggle](https://www.kaggle.com))

## How to Run

### Prerequisite

- Python version 3.11 or greater
- Mongodb database

1. Create .env file and put your mongodb url in the following format.

```
MONGODB_URI=<Your_mongodb_url>
```

2. Install requirements: pip install pymongo

```
pip install -r requirements.txt
```

3. Run: python main.py

```
python main.py
```

## Scenario

Company employee record management system.

## Showcase

### Authentication

- **Login Screen**  
  ![Login](./screenshots/login.png)
- **Login Required Field Error**  
  ![Login Required](./screenshots/loginRequiredFiled.png)
- **Incorrect Password**  
  ![Incorrect Password](./screenshots/passwordIncorrrect.png)
- **Register Screen**  
  ![Register](./screenshots/register.png)
- **Register Name Error**  
  ![Register Error](./screenshots/registerNameError.png)
- **Username Already Exists Error**  
  ![Already Exists](./screenshots/alreadyExit.png)
- **Register Success**  
  ![Register Success](./screenshots/registerSucess.png)

### Employee Management

- **Full Screen Employee Table**  
  ![Full Screen](./screenshots/fullScreen.png)
- **Add Employee**  
  ![Add Employee](./screenshots/add.png)
- **Add Employee Success**  
  ![Add Success](./screenshots/addSuccess.png)
- **Update Employee Selection Warning**  
  ![Update Select](./screenshots/updateFirstSelect.png)
- **Update Employee Form**  
  ![Update Form](./screenshots/update.png)
- **Update Success**  
  ![Update Success](./screenshots/updateSucc.png)
- **Delete Employee Warning**  
  ![Delete Alert](./screenshots/deletealert.png)
- **Delete Employee Success**  
  ![Delete Employee](./screenshots/anyEmpDelete.png)
- **Search Employee**  
  ![Search](./screenshots/search.png)
- **Export CSV**  
  ![Export CSV](./screenshots/exportCSV.png)
- **Logout**  
  ![Logout](./screenshots/logout.png)
