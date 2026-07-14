from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from models import db, Student
from sqlalchemy import func

students_bp = Blueprint("students", __name__)


# ======================================
# View Students
# ======================================
@students_bp.route("/students")
@login_required
def students():

    search = request.args.get("search")

    if search:

        students = Student.query.filter(
            Student.name.contains(search)
        ).all()

    else:

        students = Student.query.order_by(Student.id.desc()).all()

    return render_template(
        "students.html",
        students=students
    )


# ======================================
# Add Student
# ======================================
# ======================================
# Add Student
# ======================================
@students_bp.route("/students/add", methods=["GET", "POST"])
@login_required
def add_student():

    if request.method == "POST":

        student_id = request.form["student_id"].strip()
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()
        department = request.form["department"]
        year = request.form["year"]

        # Student ID validation
        if not student_id:
            flash("Student ID is required.", "danger")
            return redirect(url_for("students.add_student"))

        # Check duplicate Student ID
        existing = Student.query.filter_by(student_id=student_id).first()

        if existing:
            flash("Student ID already exists.", "danger")
            return redirect(url_for("students.add_student"))

        # Phone validation
        if not phone.isdigit() or len(phone) != 10:
            flash("Phone number must contain exactly 10 digits.", "danger")
            return redirect(url_for("students.add_student"))

        student = Student(
            student_id=student_id,
            name=name,
            email=email,
            phone=phone,
            department=department,
            year=year
        )

        db.session.add(student)
        db.session.commit()

        flash("Student Added Successfully!", "success")

        return redirect(url_for("students.students"))

    return render_template("add_student.html")


# ======================================
# Edit Student
# ======================================
@students_bp.route("/students/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_student(id):

    student = Student.query.get_or_404(id)

    if request.method == "POST":

        student_id = request.form["student_id"].strip()
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()
        department = request.form["department"]
        year = request.form["year"]

        if not student_id:
            flash("Student ID is required.", "danger")
            return redirect(url_for("students.edit_student", id=id))

        existing = Student.query.filter(
            Student.student_id == student_id,
            Student.id != id
        ).first()

        if existing:
            flash("Student ID already exists.", "danger")
            return redirect(url_for("students.edit_student", id=id))

        if not phone.isdigit() or len(phone) != 10:
            flash("Phone number must contain exactly 10 digits.", "danger")
            return redirect(url_for("students.edit_student", id=id))

        student.student_id = student_id
        student.name = name
        student.email = email
        student.phone = phone
        student.department = department
        student.year = year

        db.session.commit()

        flash("Student Updated Successfully!", "success")

        return redirect(url_for("students.students"))

    return render_template("edit_student.html", student=student)


# ======================================
# Delete Student
# ======================================
@students_bp.route("/students/delete/<int:id>")
@login_required
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)

    db.session.commit()

    flash(
        "Student Deleted Successfully!",
        "warning"
    )

    return redirect(url_for("students.students"))