def validate_products(db):
    issues = {}

    issues["missing_name"] = db.exec(
        "SELECT COUNT(*) FROM products WHERE name IS NULL OR TRIM(name)='';"
    ).fetchone()[0]

    issues["negative_price"] = db.exec(
        "SELECT COUNT(*) FROM products WHERE price < 0;"
    ).fetchone()[0]

    issues["negative_stock"] = db.exec(
        "SELECT COUNT(*) FROM products WHERE stock < 0;"
    ).fetchone()[0]

    return issues

def print_validation_report(issues):
    print("=== Data Quality Report ===")
    for k, v in issues.items():
        tag = "PASS" if v == 0 else "WARN"
        print(f"[{tag}] {k}: {v}")
