from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from models import db, Category

categories_bp = Blueprint("categories", __name__)


# =====================================
# View Categories
# =====================================
@categories_bp.route("/categories")
@login_required
def categories():

    search = request.args.get("search")

    if search:
        categories = Category.query.filter(
            Category.name.contains(search)
        ).all()
    else:
        categories = Category.query.order_by(Category.name).all()

    return render_template(
        "categories.html",
        categories=categories
    )


# =====================================
# Add Category
# =====================================
@categories_bp.route("/categories/add", methods=["POST"])
@login_required
def add_category():

    name = request.form["name"].strip()

    existing = Category.query.filter_by(name=name).first()

    if existing:
        flash("Category already exists!", "warning")
        return redirect(url_for("categories.categories"))

    category = Category(name=name)

    db.session.add(category)

    db.session.commit()

    flash("Category Added Successfully!", "success")

    return redirect(url_for("categories.categories"))


# =====================================
# Edit Category
# =====================================
@categories_bp.route("/categories/edit/<int:id>", methods=["POST"])
@login_required
def edit_category(id):

    category = Category.query.get_or_404(id)

    category.name = request.form["name"]

    db.session.commit()

    flash("Category Updated Successfully!", "success")

    return redirect(url_for("categories.categories"))


# =====================================
# Delete Category
# =====================================
@categories_bp.route("/categories/delete/<int:id>")
@login_required
def delete_category(id):

    category = Category.query.get_or_404(id)

    if category.books:
        flash(
            "Cannot delete category because books are assigned to it.",
            "danger"
        )
        return redirect(url_for("categories.categories"))

    db.session.delete(category)

    db.session.commit()

    flash("Category Deleted Successfully!", "warning")

    return redirect(url_for("categories.categories"))