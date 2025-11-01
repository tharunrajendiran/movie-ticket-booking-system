from src.admin import  Admin
class Movie:
    def __init__(self, title, genre, seats):
        self.title = title
        self.genre = genre
        self.seats = seats

    def __str__(self):
        return f"{self.title} ({self.genre}) - Seats Available: {self.seats}"


class Admin:
    def __init__(self):
        # Stores movies in a list for now (you can later connect to database.py)
        self.movies = []

    def add_movie(self, title, genre, seats):
        movie = Movie(title, genre, seats)
        self.movies.append(movie)
        print(f"\n✅ Movie '{title}' added successfully!")

    def view_movies(self):
        if not self.movies:
            print("\n⚠️ No movies available.")
            return
        print("\n📽 Available Movies:")
        for idx, movie in enumerate(self.movies, start=1):
            print(f"{idx}. {movie}")

    def update_movie(self, index, title=None, genre=None, seats=None):
        if 0 <= index < len(self.movies):
            movie = self.movies[index]
            if title:
                movie.title = title
            if genre:
                movie.genre = genre
            if seats is not None:
                movie.seats = seats
            print(f"\n✅ Movie updated: {movie}")
        else:
            print("\n❌ Invalid movie index.")

    def delete_movie(self, index):
        if 0 <= index < len(self.movies):
            removed = self.movies.pop(index)
            print(f"\n🗑 Movie '{removed.title}' deleted successfully!")
        else:
            print("\n❌ Invalid movie index.")
