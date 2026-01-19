from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
  return render_template("index.html")
# here we can also pass names and access them in html
  # return render_template("index.html", name="Joe")
  # and we access them in html by using double curly braces {{}}
#
