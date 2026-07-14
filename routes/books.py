from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Book, Category

books_bp = Blueprint("books", __name__)


# Display all books
@books_bp.route("/books")
def books():

    books = Book.query.all()

    return render_template(
        "books.html",
        books=books
    )


# Add new book
@books_bp.route("/add_book", methods=["GET", "POST"])
def add_book():

    categories = Category.query.all()

    if request.method == "POST":

        book_id = request.form["book_id"]
        title = request.form["title"]
        author = request.form["author"]
        isbn = request.form["isbn"]
        publisher = request.form["publisher"]
        quantity = int(request.form["quantity"])
        category_id = request.form["category_id"]

        existing_book = Book.query.filter_by(book_id=book_id).first()

        if existing_book:
            flash("Book ID already exists!", "danger")
            return redirect(url_for("books.add_book"))

        new_book = Book(
            book_id=book_id,
            title=title,
            author=author,
            isbn=isbn,
            publisher=publisher,
            quantity=quantity,
            available_quantity=quantity,
            category_id=category_id
        )

        db.session.add(new_book)
        db.session.commit()

        flash("Book added successfully!", "success")

        return redirect(url_for("books.books"))

    return render_template(
        "add_book.html",
        categories=categories
    )


# Edit book
@books_bp.route("/books/edit/<int:id>", methods=["GET", "POST"])
def edit_book(id):

    book = Book.query.get_or_404(id)
    categories = Category.query.all()

    if request.method == "POST":

        book.book_id = request.form["book_id"]
        book.title = request.form["title"]
        book.author = request.form["author"]
        book.isbn = request.form["isbn"]
        book.publisher = request.form["publisher"]
        book.category_id = int(request.form["category_id"])
        book.quantity = int(request.form["quantity"])

        # Keep available quantity within total quantity
        if book.available_quantity > book.quantity:
            book.available_quantity = book.quantity

        db.session.commit()

        flash("Book updated successfully!", "success")
        return redirect(url_for("books.books"))

    return render_template(
        "edit_book.html",
        book=book,
        categories=categories
    )


# Delete book
@books_bp.route("/delete_book/<int:id>")
def delete_book(id):

    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    flash("Book deleted successfully!", "success")

    return redirect(url_for("books.books"))