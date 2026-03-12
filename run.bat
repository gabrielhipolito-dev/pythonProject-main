@echo off
setlocal

REM Simple launcher for the Employee Management app.
REM If the virtual environment does not exist yet, run setup first.

if not exist .venv (
    echo Virtual environment not found. Running setup.bat...
    call setup.bat
)

echo Starting application...
call .venv\Scripts\python Project_Runner.py

