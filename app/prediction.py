from app.models import Course, Cutoff, College

def predict_seat(student_cutoff, community, district=None):

    results = []
    courses = Course.query.join(College).all()

    for course in courses:
        if district and course.college. district.lower() !=district.lower():
            continue



        cutoffs = Cutoff.query.filter_by(
            course_id=course.id,
            community=community
        ).order_by(Cutoff.round_number).all()

        for cutoff in cutoffs:

            difference = student_cutoff - cutoff.closing_cutoff

            if difference >= 0:

                if difference >= 5:
                    chance = "Very High - Safe Seat"
                elif difference >= 2:
                    chance = "High Chance"
                else:
                    chance = "Borderline - Risky"

                results.append({
                    "college": course.college.college_name,
                    "district": course.college.district,
                    "course": course.course_name,
                    "eligible_round": cutoff.round_number,
                    "closing_cutoff": cutoff.closing_cutoff,
                    "difference": round(difference, 2),
                    "chance": chance
                })

                break

    results = sorted(results, key=lambda x: x["difference"], reverse=True)

    return results[:3]