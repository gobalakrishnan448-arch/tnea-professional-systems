from flask import Blueprint, render_template, request
from app.prediction import predict_seat

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        cutoff = float(request.form["cutoff"])
        community = request.form["community"]
        district = request.form["district"]
        quota = request.form["quota"]

        results = predict_seat(cutoff, community, district, quota)

        return render_template("index.html", results=results)

    return render_template("index.html")