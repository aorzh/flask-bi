from flask import Flask
from bi.utils import get_instance_folder_path
from bi.main.controllers import main
from flask_login import LoginManager
from bi import config
from flask_admin import Admin


app = Flask(__name__,
            instance_path=get_instance_folder_path(),
            instance_relative_config=True,
            template_folder='templates')

admin = Admin(app, name='Business Intelligence', template_mode='bootstrap3')

app.config.from_object(config.ProductionConfig)
app.register_blueprint(main, url_prefix='/')
login_manager = LoginManager()
login_manager.init_app(app)


# app.register_blueprint(admin, url_prefix='/admin')
