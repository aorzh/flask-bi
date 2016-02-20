from flask import Blueprint, render_template, current_app, request, make_response, app, jsonify
from flask_login import login_required

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.html")
