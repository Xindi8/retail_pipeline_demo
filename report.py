def summary(db):
    n = db.exec("SELECT COUNT(*) FROM products;").fetchone()[0]
    total_stock = db.exec("SELECT COALESCE(SUM(stock),0) FROM products;").fetchone()[0]
    avg_price = db.exec("SELECT COALESCE(AVG(price),0) FROM products;").fetchone()[0]
    return {"products": n, "total_stock": total_stock, "avg_price": round(avg_price, 2)}

def top_expensive(db, k=5):
    rows = db.exec(
        "SELECT product_id, name, price FROM products ORDER BY price DESC, product_id ASC LIMIT ?;",
        (k,)
    ).fetchall()
    return [dict(r) for r in rows]
