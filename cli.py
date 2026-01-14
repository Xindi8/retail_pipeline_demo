from pathlib import Path
from db import DB

def init_schema(db):
    sql = Path("sample.sql").read_text(encoding="utf-8")
    db.conn.executescript(sql)
    db.commit()

def main():
    db = DB("demo.db")
    try:
        while True:
            print("\n1) init schema+seed  2) validate  3) report  4) exit")
            c = input("> ").strip()

            if c == "1":
                init_schema(db)
                print("[OK] schema initialized + sample data inserted")

            elif c == "2":
                from validate import validate_products, print_validation_report
                issues = validate_products(db)
                print_validation_report(issues)

            elif c == "3":
                from report import summary, top_expensive
                print("Summary:", summary(db))
                print("Top expensive:", top_expensive(db))

            elif c == "4":
                break

            else:
                print("Please choose 1-4.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
