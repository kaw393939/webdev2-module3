# Import necessary modules from Flask
from flask import Flask, send_from_directory, request, jsonify, make_response, g

# Function to create a Flask application
def create_app():
    # Instantiate a Flask object
    app = Flask(__name__)

    # Initialize an empty dictionary to hold resume data
    app.config['resume'] = {}

    # Define a route for the root URL ("/")
    @app.route('/')
    # When this route is hit, it will return the string 'Hello, World!'
    def hello_world():
        return 'Hello, World!'

    # Function to validate the data in the resume
    def validate_resume(new_resume):
        # Define the expected keys in the resume
        keys = ['name', 'tagline', 'email', 'phone', 'address', 'socialLinks', 'objective', 'education', 'experience', 'skills']
        # Check that all expected keys are present in the data
        for key in keys:
            if key not in new_resume:
                return False  # If any key is missing, return False
        return True  # If all keys are present, return True

    # Define a route for handling resume data
    @app.route('/resume', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def handle_resume():
        # If the HTTP method is GET
        if request.method == 'GET':
            # If a resume exists, return it with a 200 status code
            if app.config['resume']:
                return jsonify(app.config['resume']), 200
            # If no resume exists, return an error with a 404 status code
            else:
                return make_response(jsonify({'error': 'Resume not found'}), 404)
        # If the HTTP method is POST
        elif request.method == 'POST':
            # Get the resume data from the request
            new_resume = request.get_json()
            # Validate the resume data
            if not validate_resume(new_resume):
                # If the data is invalid, return an error with a 400 status code
                return make_response(jsonify({'error': 'Bad Request'}), 400)
            # If a resume already exists, return an error with a 409 status code
            if app.config['resume']:
                return make_response(jsonify({'error': 'Resume already exists'}), 409)
            else:
                # If no resume exists, store the new resume and return it with a 201 status code
                app.config['resume'] = new_resume
                return jsonify(app.config['resume']), 201
        # If the HTTP method is PUT
        elif request.method == 'PUT':
            # If no resume exists, return an error with a 404 status code
            if not app.config['resume']:
                return make_response(jsonify({'error': 'No resume to update'}), 404)
            # Get the updated resume data from the request
            new_resume = request.get_json()
            # Validate the updated resume data
            if validate_resume(new_resume):
                # If the data is valid, update the resume and return it with a 200 status code
                app.config['resume'] = new_resume
                return jsonify(app.config['resume']), 200
            else:
                # If the data is invalid, return an error with a 400 status code
                return make_response(jsonify({'error': 'Bad Request'}), 400)
        # If the HTTP method is DELETE
        elif request.method == 'DELETE':
            # If no resume exists, return an error with a 404 status code
            if not app.config['resume']:
                return make_response(jsonify({'error': 'No resume to delete'}), 404)
            # Remove the resume and return a 204 status code
            app.config['resume'] = {}
            return make_response('', 204)

    # Return the Flask application
    return app
