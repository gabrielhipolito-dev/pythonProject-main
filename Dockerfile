FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Compile all Python files as a lightweight smoke check.
CMD ["python", "-c", "import pathlib, py_compile; [py_compile.compile(str(p), doraise=True) for p in pathlib.Path('.').rglob('*.py')]"]