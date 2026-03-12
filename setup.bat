@echo off
setlocal

if not exist .venv (
    python -m venv .venv
)

call .venv\Scripts\python -m pip install --upgrade pip
call .venv\Scripts\python -m pip install -r requirements.txt

echo Setup complete.
echo Run the app with:
echo .venv\Scripts\python Project_Runner.py