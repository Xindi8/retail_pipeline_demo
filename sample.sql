-- Demo sample
DROP TABLE IF EXISTS products;

CREATE TABLE products (
  product_id INTEGER PRIMARY KEY,
  name       TEXT NOT NULL,
  category   TEXT,
  price      REAL NOT NULL CHECK(price >= 0),
  stock      INTEGER NOT NULL CHECK(stock >= 0)
);

-- Seed sample data (synthetic examples)
INSERT INTO products (product_id, name, category, price, stock) VALUES
  (1001, 'Test1',        'test1',  12.99, 40),
  (1002, 'Test2',        'test2',  79.50, 15),
  (1003, 'Test3',         'test3',  6.25, 120),
  (1004, 'Test4',   'test4',  18.00, 25),
  (1005, 'Test5',       'test5', 9.99, 60);
