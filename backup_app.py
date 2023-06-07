from flask import Flask, send_from_directory, request, jsonify, make_response, g

def create_app():
    app = Flask(__name__)

    app.config['resume'] = {}

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    def validate_resume(new_resume):
        keys = ['name', 'tagline', 'email', 'phone', 'address', 'socialLinks', 'objective', 'education', 'experience', 'skills']
        for key in keys:
            if key not in new_resume:
                return False
        return True

    @app.route('/resume', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def handle_resume():
        if request.method == 'GET':
            if app.config['resume']:
                return jsonify(app.config['resume']), 200
            else:
                return make_response(jsonify({'error': 'Resume not found'}), 404)
        elif request.method == 'POST':
            new_resume = request.get_json()
            if not validate_resume(new_resume):
                return make_response(jsonify({'error': 'Bad Request'}), 400)
            if app.config['resume']:
                return make_response(jsonify({'error': 'Resume already exists'}), 409)
            else:
                app.config['resume'] = new_resume
                return jsonify(app.config['resume']), 201
        elif request.method == 'PUT':
            if not app.config['resume']:
                return make_response(jsonify({'error': 'No resume to update'}), 404)
            new_resume = request.get_json()
            if validate_resume(new_resume):
                app.config['resume'] = new_resume
                return jsonify(app.config['resume']), 200
            else:
                return make_response(jsonify({'error': 'Bad Request'}), 400)
        elif request.method == 'DELETE':
            if not app.config['resume']:
                return make_response(jsonify({'error': 'No resume to delete'}), 404)
            app.config['resume'] = {}
            return make_response('', 204)

    return app
