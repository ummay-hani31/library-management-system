from flask import Blueprint, render_template
from flask_login import login_required

from models import Book, Student, Category, Transaction

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    total_books = Book.query.count()

    total_students = Student.query.count()

    total_categories = Category.query.count()

    issued_books = Transaction.query.filter_by(
        status="Issued"
    ).count()

    returned_books = Transaction.query.filter_by(
        status="Returned"
    ).count()

    recent_transactions = Transaction.query.order_by(
        Transaction.id.desc()
    ).limit(5).all()

    return render_template(

        "dashboard.html",

        total_books=total_books,

        total_students=total_students,

        total_categories=total_categories,

        issued_books=issued_books,

        returned_books=returned_books,

        recent_transactions=recent_transactions

    )