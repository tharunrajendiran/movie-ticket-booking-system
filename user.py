# user.py
from Db import get_connection

class User:
    @staticmethod
    def register_user(name, email):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            print("✅ User registered successfully!")
        except:
            print("⚠️ Email already exists!")
        conn.close()

    @staticmethod
    def get_user_by_email(email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE email=?", (email,))
        user = cursor.fetchone()
        conn.close()
        return user