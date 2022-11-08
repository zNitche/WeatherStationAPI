from flask import Blueprint, render_template


dashboard = Blueprint("dashboard", __name__, template_folder="templates", static_folder="static", url_prefix="/")


@dashboard.route("/")
def home():
    return render_template("index.html")
