# Python Employee Management System

> **For classmates – super quick start**
>
> 1. Make sure you have **Python 3** installed.
> 2. Clone and open this folder in a terminal:
>    - `git clone <YOUR_REPOSITORY_URL>`
>    - `cd pythonProject-main`
> 3. Run **one** of these commands (depending on what you use):
>    - PowerShell: `.\run.ps1`
>    - CMD: `run.bat`
>    - Linux/macOS/Git Bash: `bash run.sh`
>
> This will automatically create a virtual environment, install dependencies, and start the app.

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

Dependencies are listed in `requirements.txt` and are installed automatically by the setup scripts.

## Step-By-Step Setup (Clone To Run)

Important: `git clone` and `git pull` do not automatically install packages on another person's machine.

For security reasons, Git does not auto-run project scripts after clone/pull.

Use the quick **run** scripts below to make onboarding one command.

### Quick Setup + Run (Recommended)

1. Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
```

2. Go to the project folder:

```bash
cd pythonProject-main
```

3. Run one **run** script (this will create `.venv`, install dependencies, and start the app):

PowerShell (Windows):

```powershell
.\run.ps1
```

Command Prompt (Windows):

```bat
run.bat
```

Bash (Linux/macOS/Git Bash):

```bash
bash run.sh
```

If you prefer to do things manually, you can still run the setup scripts and start the app yourself.

PowerShell (Windows):

```powershell
.\setup.ps1
.\.venv\Scripts\python Project_Runner.py
```

Command Prompt (Windows):

```bat
setup.bat
.\.venv\Scripts\python Project_Runner.py
```

Bash (Linux/macOS/Git Bash):

```bash
bash setup.sh
.venv/bin/python Project_Runner.py
```

## How To Run

Run the main application from the project root (for example from an activated virtual environment):

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

## Environment Variables

No environment variable is required for normal use.

The app uses the local SQLite database at `Resources/OOP_Lab6_DB.db`.

## Default Login Accounts

Use any of the accounts below to access the system:

| Username | Password | User Type |
| --- | --- | --- |
| `Furina` | `1234567` | `HR` |
| `111` | `111` | `Admin` |
| `Romsi` | `1111` | `Accounting` |
| `12121` | `111` | `Employee` |

These values come from the bundled database at `Resources/OOP_Lab6_DB.db`.

## Optional Docker Setup (Automation)

This is a Tkinter desktop app, so the full GUI is meant to run on your local machine.

The Docker setup in this project is for automated installation checks and smoke testing only.

Build the Docker image:

```bash
docker build -t employee-mgmt-check .
```

Run the container smoke check:

```bash
docker run --rm employee-mgmt-check
```

## Optional YAML Workflow (GitHub Actions)

The workflow file at `.github/workflows/ci.yml` automates:

- Installing Python
- Installing dependencies from `requirements.txt`
- Running a Python compile smoke check across `.py` files

This helps verify that fresh clones can install dependencies and pass a basic validation step.

Note: this automation runs in GitHub's servers (CI), not automatically on each classmate's local machine.

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