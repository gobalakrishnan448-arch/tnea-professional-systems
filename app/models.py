from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin

class College(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    college_name = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100))
    type = db.Column(db.String(50))

    def __repr__(self):
        return f"<College {self.college_name}>"

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    college_id = db.Column(db.Integer, db.ForeignKey('college.id'), nullable=False)

    college = db.relationship('College', backref=db.backref('courses', lazy=True))

    def __repr__(self):
        return f"<Course {self.course_name}>"

class Cutoff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    community = db.Column(db.String(50))
    round_number = db.Column(db.Integer)
    closing_cutoff = db.Column(db.Float)
    
    
    
    quota_type = db.column(db.String(50))

    course = db.relationship('Course', backref=db.backref('cutoffs', lazy=True))

    def __repr__(self):
        return f"<Cutoff {self.closing_cutoff}>"
    from flask_login import UserMixin

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)