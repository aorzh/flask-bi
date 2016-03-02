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
    new_dict = []
    for ar, dep in top.to_dict()['id']:
        count_value = top.to_dict()['id'][(ar, dep)]
        item = [ar + '-' + dep, count_value]
        new_dict.append(item)

    string = '['
    to_d = top.to_dict()['id']
    for r, a in to_d:
        string += '[' + "'" + str(r) + "-" + str(a) + "'" + ', ' + str(to_d[r, a]) + '],'

    string += ']'
    print(new_dict)
    return render_template('frame.html', td=new_dict, top=string, top_html=top.to_html(classes="table table-striped"))
