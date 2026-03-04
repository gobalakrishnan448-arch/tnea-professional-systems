from app import create_app, db
from app.models import College, Course, Cutoff

app = create_app()

with app.app_context():

    # ---------------- COLLEGE 1 ----------------
    college1 = College(college_name="ABC Engineering College", district="Chennai")
    db.session.add(college1)
    db.session.flush()

    cse1 = Course(course_name="CSE", college_id=college1.id)
    ece1 = Course(course_name="ECE", college_id=college1.id)
    db.session.add_all([cse1, ece1])
    db.session.flush()

    # ---------------- COLLEGE 2 ----------------
    college2 = College(college_name="XYZ Institute of Technology", district="Coimbatore")
    db.session.add(college2)
    db.session.flush()

    cse2 = Course(course_name="CSE", college_id=college2.id)
    it2 = Course(course_name="IT", college_id=college2.id)
    db.session.add_all([cse2, it2])
    db.session.flush()

    # ---------------- COLLEGE 3 ----------------
    college3 = College(college_name="Government Engineering College", district="Vellore")
    db.session.add(college3)
    db.session.flush()

    mech3 = Course(course_name="Mechanical", college_id=college3.id)
    civil3 = Course(course_name="Civil", college_id=college3.id)
    db.session.add_all([mech3, civil3])
    db.session.flush()

    # ---------------- CUT OFF DATA ----------------

    cutoff_data = [
        # College1 CSE
        Cutoff(course_id=cse1.id, community="OC", round_number=1, closing_cutoff=197.5, quota_type="Government"),
        Cutoff(course_id=cse1.id, community="OC", round_number=2, closing_cutoff=195.0, quota_type="Government"),
        Cutoff(course_id=cse1.id, community="OC", round_number=1, closing_cutoff=180.0, quota_type="Management"),

        # College2 CSE
        Cutoff(course_id=cse2.id, community="BC", round_number=1, closing_cutoff=190.0, quota_type="Government"),
        Cutoff(course_id=cse2.id, community="BC", round_number=2, closing_cutoff=187.0, quota_type="Government"),

        # College3 Mechanical
        Cutoff(course_id=mech3.id, community="MBC", round_number=1, closing_cutoff=175.0, quota_type="Government"),
        Cutoff(course_id=mech3.id, community="MBC", round_number=2, closing_cutoff=170.0, quota_type="Government"),
    ]

    db.session.add_all(cutoff_data)
    db.session.commit()

print("Realistic Dataset Inserted Successfully ✅")