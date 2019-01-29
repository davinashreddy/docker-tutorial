from flask_assets import Bundle, Environment
from app import app

bundles = {

    'materialize_js': Bundle(
        'js/materialize.min.js',
        'js/init.js',
        output='gen/home.js'),

    'materialize_css': Bundle(
        'css/materialize.min.css',
        'css/style.css',
        output='gen/main.css'),
}

assets = Environment(app)

assets.register(bundles)
