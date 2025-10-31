import sqlite3
import os

def init_db():
    conn = sqlite3.connect("baccarat.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            balance INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect("baccarat.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def get_balance(user_id):
    conn = sqlite3.connect("baccarat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0

def update_balance(user_id, balance):
    conn = sqlite3.connect("baccarat.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = ? WHERE user_id = ?", (balance, user_id))
    conn.commit()
    conn.close()
