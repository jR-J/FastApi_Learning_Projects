from fastapi import FastAPI
import sqlite3

app = FastAPI()

def query_db(sql, params= ()):
    conn = sqlite3.connect("product.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/products")
def get_out_of_stock():
    sql = "SELECT * FROM products WHERE in_stock = 0"
    return query_db(sql)


@app.get("/products/most_expensive")
def get_most_expensive_product():
    sql = "SELECT * FROM products ORDER BY price DESC LIMIT 1"
    return query_db(sql)[0]

@app.get("/products/count_out_of_stock")
def count_out_of_stock():
    sql = "SELECT COUNT(*) as count FROM products WHERE in_stock = 0"
    return query_db(sql)[0]