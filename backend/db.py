import sqlite3

DATABASE = "backend/database.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS portal_config (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id TEXT NOT NULL,
            client_secret1 TEXT NOT NULL,
            client_secret2 TEXT NOT NULL,
            taxpayer_name TEXT NOT NULL,
            taxpayer_registration TEXT NOT NULL,
            taxpayer_address TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_number TEXT NOT NULL,
            invoice_date TEXT NOT NULL,
            customer_name TEXT NOT NULL,
            tax_registration TEXT NOT NULL,
            customer_address TEXT NOT NULL,
            document_type TEXT NOT NULL,
            items TEXT NOT NULL,
            tax_rate REAL DEFAULT 0,
            status TEXT DEFAULT 'pending'
        )
    ''')
    conn.commit()
    conn.close()

create_tables()
