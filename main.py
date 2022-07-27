from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect

import databaseDAO as DAO

app = Flask(__name__)


@app.route("/")
def index():
    list_birds = DAO.database_query()
    pagetitle = "Feathers Database Content"
    credits = ["Artwork \'Database\' by https://icons8.com/icon/8305/database",
               "Artwork \'Tools\' by https://icons8.com/icon/SX59ewiDOzjU/tool",
               "Background created by Harryarts https://www.freepik.com/vectors/quill"]

    return render_template("query.html", mytitle=pagetitle, length=len(list_birds), list_birds=list_birds, credits=credits)


@app.route("/login", methods=["GET", "POST"])
def login():
    pagetitle = "Feathers Database Login"
    credits = ["Artwork \'Database\' by https://icons8.com/icon/8305/database",
               "Artwork \'Back\' created by https://icons8.com/icon/1O6HFhy1QjW3/back",
               "Artwork \'Name\' created by https://icons8.com/icon/11779/name",
               "Artwork \'Password\' created by https://icons8.com/icon/10480/password",
               "Background created by Harryarts https://www.freepik.com/vectors/quill"]

    error = ""
    if request.method == 'POST':
        if request.form['username'] != 'birdy' or request.form['password'] != 'bird':
            error = 'Invalid Credentials. Please try again!'
        else:
            return redirect(url_for('datamanipulation'))
    return render_template("login.html", mytitle=pagetitle, error=error, credits=credits)


@app.route("/dataManipulation")
def datamanipulation():
    pagetitle = "Feathers Database Manipulation Page"
    credits = ["Artwork \'Database\' by https://icons8.com/icon/8305/database",
               "Artwork \'Back\' created by https://icons8.com/icon/1O6HFhy1QjW3/back",
               "Artwork \'Add\' created by https://icons8.com/icon/37839/add",
               "Artwork \'Remove\' created by https://icons8.com/icon/fxyhG29jgJRt/remove",
               "Artwork \'Database Export\' created by https://icons8.com/icon/UInkwhA_ADMW/database-export",
               "Background created by Harryarts https://www.freepik.com/vectors/quill"]

    return render_template("datamanipulation.html", mytitle=pagetitle, credits=credits)


@app.route("/dataManipulation_insert", methods=["GET", "POST"])
def data_manipulation_insert():
    pagetitle = "Feathers Database Data Insertion"
    credits = ["Artwork \'Database\' by https://icons8.com/icon/8305/database",
               "Artwork \'Back\' created by https://icons8.com/icon/1O6HFhy1QjW3/back",
               "Background created by Harryarts https://www.freepik.com/vectors/quill"]
    msg = ""

    if request.method == 'POST':
        name_GER = request.form["name_GER"]
        name_ENG = request.form["name_ENG"]
        name_LAT = request.form["name_LAT"]
        red_list_category = request.form["red_list_category"]

        msg = DAO.database_insert(name_GER, name_ENG, name_LAT, red_list_category)

    return render_template("manipulationinsert.html", mytitle=pagetitle, msg=msg, credits=credits)


@app.route("/dataManipulation_delete", methods=["GET", "POST"])
def data_manipulation_delete():
    pagetitle = "Feathers Database Data Deletion"
    credits = ["Artwork \'Database\' by https://icons8.com/icon/8305/database",
               "Artwork \'Back\' created by https://icons8.com/icon/1O6HFhy1QjW3/back",
               "Background created by Harryarts https://www.freepik.com/vectors/quill"]
    msg = ""

    if request.method == 'POST':
        column = request.form["column"]
        element = request.form["element"]

        if column == "German Denotation":
            column = "name_GER"
        if column == "English Denotation":
            column = "name_ENG"
        if column == "Latin Denotation":
            column = "name_LAT"

        msg = DAO.database_delete_row(column, element)

    return render_template("manipulationdelete.html", mytitle=pagetitle, msg=msg, credits=credits)


if __name__ == '__main__':
    app.run(port=1337, debug=False, threaded=True)
