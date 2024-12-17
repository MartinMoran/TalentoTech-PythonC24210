import sqlite3 as sql

def crearDB():
    conn = sql.connect("inventario.db")
    conn.commit()
    conn.close()
    
def crearTabla():
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS productos(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nombre TEXT NOT NULL,
       cantidad INTEGER NOT NULL,
       precio_unitario REAL NOT NULL,
       categoria TEXT NOT NULL,
       descripcion TEXT
    )""")
    conn.commit()
    conn.close()
    

