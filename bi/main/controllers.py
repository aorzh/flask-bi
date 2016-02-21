from flask import Blueprint, render_template, current_app, request, make_response, app, jsonify
from flask_login import login_required
from bi.main import efl

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.html")


@main.route('top20')
def top_twenty():
    top = efl.top20()
    string = '['
    to_d = top.to_dict()['id']
    for r, a in to_d:

        print(r, a)

        string += '['
        string += "'"
        string += str(r)
        string += "-"
        string += str(a)
        string += "'"
        string += ', '
        string += str(to_d[r, a])
        string += '],'

    string += ']'

    return render_template('frame.html', top=string, top_html=top.to_html(classes="table table-striped"))
