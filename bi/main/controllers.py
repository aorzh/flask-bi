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
    return render_template('frame.html', top=top)
