# Db.py
import sqlite3

def get_connection():
    return sqlite3.connect("movies.db")

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (
                        movie_id INTEGER PRIMARY KEY,
                        title TEXT,
                        genre TEXT,
                        show_time TEXT,
                        available_seats INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        user_id INTEGER PRIMARY KEY,
                        name TEXT,
                        email TEXT UNIQUE)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Bookings (
                        booking_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        movie_id INTEGER,
                        seats_booked INTEGER,
                        booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY(user_id) REFERENCES Users(user_id),
                        FOREIGN KEY(movie_id) REFERENCES Movies(movie_id))''')

    conn.commit()
    conn.close()