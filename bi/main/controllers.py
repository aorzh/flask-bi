from flask import Blueprint, render_template, current_app, request, make_response, app, jsonify, flash, abort, url_for, redirect
from flask_login import login_required, current_user, logout_user, login_user, session
from bi.main import efl
from bi.main import forms
from bi.main.models import User
from bi.main.forms import LoginForm


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template("index.html")


@main.route("login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate():
        flash(u'Successfully logged in as %s' % form.user.username)
        session['user_id'] = form.user.id
        return redirect(url_for('admin'))
    return render_template('login.html', form=form)


"""
@main.route("/logout", methods=["GET"])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("logout.html")
"""


@login_required
@main.route('top20')
def top_twenty():
    top = efl.top20()
    new_dict = []
    for ar, dep in top.to_dict()['id']:
        count_value = top.to_dict()['id'][(ar, dep)]
        item = [ar + '-' + dep, count_value]
        new_dict.append(item)

    """
    string = '['
    to_d = top.to_dict()['id']
    for r, a in to_d:
        string += '[' + "'" + str(r) + "-" + str(a) + "'" + ', ' + str(to_d[r, a]) + '],'

    string += ']'
    """
    print(new_dict)
    return render_template('frame.html', td=new_dict)


@main.route("predict")
def predict():
    pass
