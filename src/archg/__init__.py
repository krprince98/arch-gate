from flask import Flask
import os
from . import db
from . import auth
from . import blog

def make_app():
	app = Flask(__name__)
	os.makedirs(app.instance_path, exist_ok=True)
	app.config.from_mapping(
		DATABASE=os.path.join(app.instance_path, 'app_db.sqlite'),
		SECRET_KEY='secure-it'
	)

	db.before_start(app)

	app.register_blueprint(auth.bp)
	app.register_blueprint(blog.bp)
	app.add_url_rule('/', endpoint='index')

	return app
