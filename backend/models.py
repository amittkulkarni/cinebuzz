from . import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Enum('Admin', 'Customer', 'SuperAdmin', name='role'), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    reservations = db.relationship('Reservation', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.name}>'


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=True)
    language = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    trailer = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text, nullable=True)
    duration = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    showtimes = db.relationship('Showtime', backref='movie', lazy=True)

    def __repr__(self):
        return f'<Movie {self.title}>'


class Theatre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    ticket_price = db.Column(db.Float, nullable=False)
    seats = db.Column(db.JSON, nullable=False)  # Stored as JSON for flexible seat arrangement
    image = db.Column(db.String(200), nullable=True)
    showtimes = db.relationship('Showtime', backref='theatre', lazy=True)

    def __repr__(self):
        return f'<Theatre {self.name}>'


class Showtime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_price = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id'), nullable=False)
    reservations = db.relationship('Reservation', backref='showtime', lazy=True)

    def __repr__(self):
        return f'<Showtime Movie: {self.movie.title}, Theatre: {self.theatre.name}>'


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    start_at = db.Column(db.DateTime, nullable=False)
    seats = db.Column(db.JSON, nullable=False)  # Stored as JSON for seat details
    order_id = db.Column(db.String(100), unique=True, nullable=False)
    ticket_price = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Reservation {self.order_id} by {self.name}>'

