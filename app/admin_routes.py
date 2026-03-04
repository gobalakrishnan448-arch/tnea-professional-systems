from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from app.models import College, Course, Cutoff, Admin
from app import db

admin = Blueprint("admin", __name__, url_prefix="/admin")

@admin.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = Admin.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("admin.admin_home"))

    return render_template("login.html")

@admin.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("admin.login"))

@admin.route("/")
@login_required
def admin_home():
    return """
    <h2>Admin Panel</h2>
    <a href='/admin/add-college'>Add College</a><br>
    <a href='/admin/add-course'>Add Course</a><br>
    <a href='/admin/add-cutoff'>Add Cutoff</a><br>
    <a href='/admin/logout'>Logout</a>
    """

@admin.route("/add-college", methods=["GET", "POST"])
@login_required
def add_college():
    if request.method == "POST":
        name = request.form["name"]
        district = request.form["district"]

        college = College(college_name=name, district=district)
        db.session.add(college)
        db.session.commit()

        return redirect(url_for("admin.admin_home"))

    return """
    <h3>Add College</h3>
    <form method="POST">
        College Name: <input type="text" name="name"><br>
        District: <input type="text" name="district"><br>
        <button type="submit">Add</button>
    </form>
    """

@admin.route("/add-course", methods=["GET", "POST"])
@login_required
def add_course():
    colleges = College.query.all()

    if request.method == "POST":
        name = request.form["name"]
        college_id = request.form["college_id"]

        course = Course(course_name=name, college_id=college_id)
        db.session.add(course)
        db.session.commit()

        return redirect(url_for("admin.admin_home"))

    options = "".join([f"<option value='{c.id}'>{c.college_name}</option>" for c in colleges])

    return f"""
    <h3>Add Course</h3>
    <form method="POST">
        Course Name: <input type="text" name="name"><br>
        College: <select name="college_id">{options}</select><br>
        <button type="submit">Add</button>
    </form>
    """

@admin.route("/add-cutoff", methods=["GET", "POST"])
@login_required
def add_cutoff():
    courses = Course.query.all()

    if request.method == "POST":
        course_id = request.form["course_id"]
        community = request.form["community"]
        round_number = request.form["round"]
        closing_cutoff = request.form["cutoff"]
        quota = request.form["quota"]

        cutoff = Cutoff(
            course_id=course_id,
            community=community,
            round_number=round_number,
            closing_cutoff=closing_cutoff,
            quota_type=quota
        )

        db.session.add(cutoff)
        db.session.commit()

        return redirect(url_for("admin.admin_home"))

    options = "".join([f"<option value='{c.id}'>{c.course_name}</option>" for c in courses])

    return f"""
    <h3>Add Cutoff</h3>
    <form method="POST">
        Course: <select name="course_id">{options}</select><br>
        Community: <input type="text" name="community"><br>
        Round: <input type="number" name="round"><br>
        Closing Cutoff: <input type="number" step="0.1" name="cutoff"><br>
        Quota:
        <select name="quota">
            <option>Government</option>
            <option>Management</option>
        </select><br>
        <button type="submit">Add</button>
    </form>
    """