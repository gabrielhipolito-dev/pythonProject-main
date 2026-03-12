# Python Employee Management System

This project is a desktop employee management system built with Tkinter and SQLite. It provides a role-based workflow for logging in, encoding employee information, computing payroll, managing user accounts, and viewing records from an admin page.

## Overview

The application starts from `Project_Runner.py`, opens the login window, and then routes the user to the correct page based on the account type stored in the database.

Supported user flows:

- `HR`: encode and save personal employee information
- `Accounting`: search employees, compute payroll, and save payroll records
- `Employee`: view or update the employee account assigned to the logged-in user
- `Admin`: open the admin dashboard and navigate to info, payroll, or account management pages

The project uses the SQLite database file at `Resources/OOP_Lab6_DB.db`.

## Main Files

- `Project_Runner.py`: main entry point and role-based navigation
- `Lab8_Login.py`: login window and credential lookup
- `Lab8_AdminPage.py`: admin dashboard for viewing tables and opening data-entry pages
- `Lab8_B.py`: personal information form
- `Lab8_C.py`: payroll form and payroll computation logic
- `Lab8_D.py`: user account management form
- `Lab8_Class.py`: shared Tkinter UI helpers, widgets, frames, dialogs, and image handling

## Requirements

This project uses Python 3 and the following libraries:

- `tkinter`
- `sqlite3`
- `Pillow`
- `tkcalendar`

Install the external dependencies with:

```bash
pip install pillow tkcalendar
```

## How To Run

Run the main application from the project root:

```bash
python Project_Runner.py
```

You can also run individual screens directly for testing:

```bash
python Lab8_Login.py
python Lab8_AdminPage.py
python Lab8_B.py
python Lab8_C.py
python Lab8_D.py
```

## Project Structure

```text
pythonProject-main/
|- Project_Runner.py
|- Lab8_Login.py
|- Lab8_AdminPage.py
|- Lab8_B.py
|- Lab8_C.py
|- Lab8_D.py
|- Lab8_Class.py
|- Resources/
|  |- OOP_Lab6_DB.db
|  |- images and font assets
```

## Functional Summary

### 1. Login

- Validates the username and password against the `User_Info` table
- Returns the matching account record to the main runner

### 2. Personal Information Module

- Encodes employee personal, department, contact, and address details
- Supports image selection and storage of the image path
- Saves records to `Personal_InfoTbl`

### 3. Payroll Module

- Searches employee details by employee number
- Computes gross income from basic, honorarium, and other income
- Computes deductions such as SSS, PhilHealth, Pag-IBIG, withholding tax, and loans
- Saves and updates payroll records in the `Payroll` table

### 4. Account Management Module

- Searches employee data by employee number
- Creates or updates user accounts in `User_Info`
- Deletes user accounts when needed

### 5. Admin Page

- Displays data from `Personal_InfoTbl`, `Payroll`, and `User_Info`
- Routes to the corresponding data-entry page for adding new records

## Notes

- The app expects the database file to remain in `Resources/OOP_Lab6_DB.db`.
- Image assets used by the UI are stored in `Resources/`.
- `Lab8_Class.py` is the shared UI utility module used by all screens.
- The code references a custom font (`HYWenHei 85W`). If that font is not installed, the fallback line in `Lab8_Class.py` can be used instead.

## Database Dependency

The program depends on existing tables inside the bundled SQLite database:

- `User_Info`
- `Personal_InfoTbl`
- `Payroll`

If the schema is changed, the SQL queries in the modules must be updated to match.