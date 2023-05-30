# application/__init__.py
from flask import Flask, send_from_directory

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/static/<path:filename>')  
    def send_file(filename):  
        return send_from_directory(app.static_folder, filename)
    
    return app