# main.py
from Db import setup_database
from movie import Movie
from user import User
from bookings import Booking

def main():
    setup_database()

    while True:
        print("\n🎬 Movie Ticket Booking System 🎟️")
        print("1. Register User")
        print("2. View Movies")
        print("3. Add Movie (Admin)")
        print("4. Update Movie (Admin)")
        print("5. Delete Movie (Admin)")
        print("6. Book Ticket")
        print("7. Cancel Booking")
        print("8. View My Bookings")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            User.register_user(name, email)

        elif choice == "2":
            movies = Movie.get_all_movies()
            if  movies:
                print  (" movies available.")
            else:
                for m in movies:
                    print(m)

        elif choice == "3":
            title = input("Enter title: ")
            genre = input("Enter genre: ")
            show_time = input("Enter show time: ")
            seats = int(input("Enter available seats: "))
            Movie.add_movie(title, genre, show_time, seats)

        elif choice == "4":
            movie_id = int(input("Enter Movie ID: "))
            new_time = input("Enter new show time: ")
            Movie.update_movie(movie_id, new_time)

        elif choice == "5":
            movie_id = int(input("Enter Movie ID to delete: "))
            Movie.delete_movie(movie_id)

        elif choice == "6":
            email = input("Enter your email: ")
            user = User.get_user_by_email(email)
            if not user:
                print("⚠️ User not found. Please register first.")
                continue
            user_id = user[0]
            movie_id = int(input("Enter Movie ID: "))
            seats = int(input("Enter number of seats: "))
            Booking.book_ticket(user_id, movie_id, seats)

        elif choice == "7":
            booking_id = int(input("Enter Booking ID to cancel: "))
            Booking.cancel_booking(booking_id)

        elif choice == "8":
            email = input("Enter your email: ")
            user = User.get_user_by_email(email)
            if user:
                bookings = Booking.view_user_bookings(user[0])
                if not bookings:
                    print("⚠️ No bookings found.")
                else:
                    for b in bookings:
                        print(b)
            else:
                print("⚠️ User not found.")

        elif choice == "9":
            print("👋 Exiting... Bye!")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()