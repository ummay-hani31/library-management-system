from flask import Blueprint, render_template
from flask_login import login_required

from models import Transaction

reports_bp = Blueprint("reports", __name__)


@reports_bp.route("/reports")
@login_required
def reports():

    transactions = Transaction.query.order_by(
        Transaction.id.desc()
    ).all()

    total_transactions = len(transactions)

    total_returned = len(
        [t for t in transactions if t.status == "Returned"]
    )

    total_issued = len(
        [t for t in transactions if t.status == "Issued"]
    )

    total_fine = sum(
        t.fine for t in transactions
    )

    return render_template(

        "reports.html",

        transactions=transactions,

        total_transactions=total_transactions,

        total_returned=total_returned,

        total_issued=total_issued,

        total_fine=total_fine

    )