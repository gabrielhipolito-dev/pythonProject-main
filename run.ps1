$ErrorActionPreference = 'Stop'

# Simple launcher for the Employee Management app.
# If the virtual environment does not exist yet, run setup first.

if (-not (Test-Path '.venv')) {
    Write-Host 'Virtual environment not found. Running setup.ps1...'
    & .\setup.ps1
}

Write-Host 'Starting application...'
& .\.venv\Scripts\python Project_Runner.py

