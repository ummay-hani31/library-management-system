from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()



# =========================
# ADMIN MODEL
# =========================

class Admin(db.Model, UserMixin):

    __tablename__ = "admins"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )


    password = db.Column(
        db.String(200),
        nullable=False
    )



    def set_password(self, password):

        from werkzeug.security import generate_password_hash

        self.password = generate_password_hash(password)



    def check_password(self, password):

        from werkzeug.security import check_password_hash

        return check_password_hash(
            self.password,
            password
        )





# =========================
# CATEGORY MODEL
# =========================

class Category(db.Model):

    __tablename__ = "categories"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )


    books = db.relationship(
        "Book",
        backref="category",
        lazy=True
    )





# =========================
# BOOK MODEL
# =========================

class Book(db.Model):

    __tablename__ = "books"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    book_id = db.Column(
        db.String(30),
        unique=True,
        nullable=False
    )


    title = db.Column(
        db.String(200),
        nullable=False
    )


    author = db.Column(
        db.String(150),
        nullable=False
    )


    isbn = db.Column(
        db.String(50)
    )


    publisher = db.Column(
        db.String(150)
    )


    quantity = db.Column(
        db.Integer,
        default=1
    )


    available_quantity = db.Column(
        db.Integer,
        default=1
    )


    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )





# =========================
# STUDENT MODEL
# =========================

class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.String(30), unique=True, nullable=False)

    name = db.Column(db.String(150), nullable=False)

    email = db.Column(db.String(150))

    phone = db.Column(db.String(20))

    department = db.Column(db.String(100))

    year = db.Column(db.String(20))





# =========================
# TRANSACTION MODEL
# =========================
class Transaction(db.Model):

    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer,
                           db.ForeignKey("students.id"),
                           nullable=False)

    book_id = db.Column(db.Integer,
                        db.ForeignKey("books.id"),
                        nullable=False)

    issue_date = db.Column(db.Date,
                           default=datetime.utcnow)

    due_date = db.Column(db.Date)

    return_date = db.Column(db.Date)

    fine = db.Column(db.Integer,
                     default=0)

    status = db.Column(db.String(20),
                       default="Issued")

    student = db.relationship("Student",
                              backref="transactions")

    book = db.relationship("Book",
                           backref="transactions")