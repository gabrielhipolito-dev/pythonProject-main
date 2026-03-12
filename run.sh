#!/usr/bin/env bash
set -euo pipefail

# Simple launcher for the Employee Management app.
# If the virtual environment does not exist yet, run setup first.

if [ ! -d ".venv" ]; then
  echo "Virtual environment not found. Running setup.sh..."
  bash setup.sh
fi

echo "Starting application..."
.venv/bin/python Project_Runner.py

