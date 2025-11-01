# booking.py
from Db import get_connection

class Booking:
    @staticmethod
    def book_ticket(user_id, movie_id, seats_booked):
        conn = get_connection()
        cursor = conn.cursor()

        # Check available seats
        cursor.execute("SELECT available_seats FROM Movies WHERE movie_id=?", (movie_id,))
        row = cursor.fetchone()
        if not row:
            print("⚠️ Movie not found!")
            return
        available = row[0]

        if seats_booked > available:
            print("❌ Not enough seats available!")
            conn.close()
            return

        # Insert booking
        cursor.execute("INSERT INTO Bookings (user_id, movie_id, seats_booked) VALUES (?, ?, ?)",
                       (user_id, movie_id, seats_booked))

        # Update movie seats
        cursor.execute("UPDATE Movies SET available_seats = available_seats - ? WHERE movie_id=?",
                       (seats_booked, movie_id))

        conn.commit()
        conn.close()
        print("✅ Ticket booked successfully!")

    @staticmethod
    def cancel_booking(booking_id):
        conn = get_connection()
        cursor = conn.cursor()

        # Find booking
        cursor.execute("SELECT movie_id, seats_booked FROM Bookings WHERE booking_id=?", (booking_id,))
        row = cursor.fetchone()
        if not row:
            print("⚠️ Booking not found!")
            return
        movie_id, seats = row

        # Delete booking
        cursor.execute("DELETE FROM Bookings WHERE booking_id=?", (booking_id,))

        # Restore seats
        cursor.execute("UPDATE Movies SET available_seats = available_seats + ? WHERE movie_id=?",
                       (seats, movie_id))

        conn.commit()
        conn.close()
        print("✅ Booking cancelled!")

    @staticmethod
    def view_user_bookings(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.booking_id, m.title, m.show_time, b.seats_booked, b.booking_time
            FROM Bookings b
            JOIN Movies m ON b.movie_id = m.movie_id
            WHERE b.user_id=?""", (user_id,))
        bookings = cursor.fetchall()
        conn.close()
        return bookings
5