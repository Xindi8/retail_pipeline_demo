## Retail Pipeline Demo (Python + SQLite)

This is a small **Python + SQLite** demo project that shows a simple end-to-end data workflow:

1. Create a clean database schema  
2. Insert sample data (seeded in the SQL file)  
3. Run data quality validation checks  
4. Generate basic summary reports


## How to Run

From the project root folder:

python cli.py

You will see a menu:

1 = Initialize database schema + insert sample data

2 = Run validation checks

3 = Generate summary report

4 = Exit

## What validate.py Checks

The validation step checks:

Missing product names

Negative prices

Negative stock values

Recommended order:
1 → 2 → 3
