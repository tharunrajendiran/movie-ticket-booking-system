# movie.py
from Db import get_connection

class Movie:
    @staticmethod
    def add_movie(title, genre, show_time, available_seats):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Movies (title, genre, show_time, available_seats) VALUES (?, ?, ?, ?)",
                       (title, genre, show_time, available_seats))
        conn.commit()
        conn.close()
        print("✅ Movie added successfully!")

    @staticmethod
    def update_movie(movie_id, new_show_time):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Movies SET show_time=? WHERE movie_id=?", (new_show_time, movie_id))
        conn.commit()
        conn.close()
        print("✅ Movie updated successfully!")

    @staticmethod
    def delete_movie(movie_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Movies WHERE movie_id=?", (movie_id,))
        conn.commit()
        conn.close()
        print("✅ Movie deleted successfully!")

    @staticmethod
    def get_all_movies():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Movies")
        movies = cursor.fetchall()
        conn.close()
        return movies