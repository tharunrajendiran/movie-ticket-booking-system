# Movie Ticket Booking System

A Python‑based application for booking movie tickets, managing users, movies and showtimes from a simple interface.

## 🚀 Table of Contents
- [About](#about)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  

## About  
This project provides a basic movie‑ticket booking framework: users can browse movies, select showtimes/seats, and book tickets. Admins can add/edit movies, manage showtimes, etc.  
(It’s developed for academic / learning purposes — e.g., for a final year engineering project.)

## Features  
- User registration and login  
- Admin interface: add/edit/remove movies, showtimes  
- Browsing movie listings, viewing details  
- Ticket booking: select showtime, seats, confirm booking  
- Simple database backend for users, movies, bookings  
- Front‑end folder included for UI components  

## Tech Stack  
- **Language**: Python  
- **Database**: SQLite / simple DB file (`Db.py`)  
- **UI / Front‑End**: Basic front‑end folder (HTML/CSS/JS)  
- **Modules**: `user.py`, `movie.py`, `bookings.py`, `admin.py`, `main.py`  
- OS: Cross‑platform (Windows / Linux with Python)  
- Requirements: Python 3.x  

## Getting Started  
### Prerequisites  
- Python 3.x installed  
- Optionally a virtual environment  
- Required packages (if any external libraries used)  

### Installation  
1. Clone the repository  
   ```bash
   git clone https://github.com/tharunrajendiran/movie-ticket-booking-system.git  
   ```  
2. Navigate into the project directory  
   ```bash
   cd movie-ticket-booking-system  
   ```  
3. Install required dependencies  
   ```bash
   pip install -r requirements.txt  
   ```  
   *If there is no `requirements.txt`, simply ensure your environment has the needed modules.*  
4. Initialize the database (if needed)  
   ```bash
   python Db.py  
   ```  
   *This depends on how your DB initialization is implemented.*  
5. Run the main application  
   ```bash
   python main.py  
   ```  

## Usage  
- Open `main.py` to launch the app.  
- Use the interface to register as a user or log in as admin.  
- Explore movies, book tickets, view bookings.  
- Admin: modify movies/showtimes, remove bookings.  
- Front‑end files are in the `front end` folder — you can open the HTML pages in a browser to view or test the UI.

## Project Structure  
```
movie-ticket-booking-system/
├── Db.py              # Database setup / utilities  
├── admin.py           # Admin module  
├── user.py            # User module  
├── movie.py           # Movie management  
├── bookings.py        # Booking logic  
├── main.py            # Entry point  
├── front end/         # UI front‑end folder (HTML, CSS, JS)  
└── README.md          # This file  
```

## Contributing  
If you’d like to contribute improvements or new features (e.g., seat map visualization, payment integration, better UI, REST API), you’re very welcome!  
Please fork the repo, create a branch, make your changes, then submit a pull request.

## License  
Specify your license here (e.g., MIT License).  
```text
MIT License  
Copyright (c) 2025 Tharun R  
```
