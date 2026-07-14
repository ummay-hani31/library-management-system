from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import date, timedelta

from models import db, Book, Student, Transaction

transactions_bp = Blueprint("transactions", __name__)


# ======================================
# Issue Book
# ======================================
@transactions_bp.route("/issue", methods=["GET", "POST"])
@login_required
def issue_book():

    students = Student.query.order_by(Student.name).all()
    books = Book.query.filter(Book.available_quantity > 0).all()

    if request.method == "POST":

        student = Student.query.get(request.form["student"])
        book = Book.query.get(request.form["book"])

        if not student or not book:
            flash("Invalid Student or Book.", "danger")
            return redirect(url_for("transactions.issue_book"))

        if book.available_quantity <= 0:
            flash("Book is currently unavailable.", "danger")
            return redirect(url_for("transactions.issue_book"))

        issue_date = date.today()
        due_date = issue_date + timedelta(days=14)

        transaction = Transaction(
            student_id=student.id,
            book_id=book.id,
            issue_date=issue_date,
            due_date=due_date,
            status="Issued"
        )

        book.available_quantity -= 1

        db.session.add(transaction)
        db.session.commit()

        flash("Book Issued Successfully!", "success")

        return redirect(url_for("dashboard.dashboard"))

    issue_date = date.today()
    due_date = issue_date + timedelta(days=14)

    return render_template(
        "issue_book.html",
        students=students,
        books=books,
        issue_date=issue_date,
        due_date=due_date
    )


# ======================================
# Return Books List
# ======================================
@transactions_bp.route("/returns")
@login_required
def return_book_list():

    search = request.args.get("search", "")

    transactions = Transaction.query.filter_by(status="Issued").all()

    if search:

        transactions = [
            t for t in transactions
            if search.lower() in t.student.name.lower()
            or search.lower() in t.student.student_id.lower()
            or search.lower() in t.book.title.lower()
        ]

    return render_template(
        "return_books.html",
        transactions=transactions,
        today=date.today()
    )


# ======================================
# Return Book
# ======================================
@transactions_bp.route("/return/<int:id>")
@login_required
def return_book(id):

    transaction = Transaction.query.get_or_404(id)

    if transaction.status == "Returned":
        flash("Book already returned.", "warning")
        return redirect(url_for("transactions.return_book_list"))

    today = date.today()

    transaction.return_date = today
    transaction.status = "Returned"

    if today > transaction.due_date:
        late_days = (today - transaction.due_date).days
        transaction.fine = late_days * 10
    else:
        transaction.fine = 0

    transaction.book.available_quantity += 1

    db.session.commit()

    flash(
        f"Book Returned Successfully! Fine: ₹{transaction.fine}",
        "success"
    )

    return redirect(url_for("transactions.return_book_list"))