$ErrorActionPreference = 'Stop'

if (-not (Test-Path '.venv')) {
    python -m venv .venv
}

& .\.venv\Scripts\python -m pip install --upgrade pip
& .\.venv\Scripts\python -m pip install -r requirements.txt

Write-Host 'Setup complete.'
Write-Host 'Run the app with:'
Write-Host '.\.venv\Scripts\python Project_Runner.py'