# Import the Flask class and the send_from_directory function from the flask module.
# The Flask class is used to create instances of the Flask web application.
# The send_from_directory function is used to send a file from a given directory.
from flask import Flask, send_from_directory

# Define a function called create_app that takes no arguments.
# This function will create and configure an instance of a Flask application.
def create_app():
    # Create a new instance of a Flask application.
    # The argument __name__ is a special variable in Python that is automatically set to the name of the module in which it is used. 
    # In this case, it will be set to "application". Flask uses this to know where to find other files such as templates and static files.
    app = Flask(__name__)

    # Define a route for the URL "/", which is the root URL.
    # When someone accesses the root URL of your web application, Flask will call the hello_world function and return its response.
    @app.route('/')
    def hello_world():
        # This function simply returns the string 'Hello, World!'.
        return 'Hello, World!'

    # Define a route for the URL "/static/<path:filename>".
    # "<path:filename>" is a variable part of the URL, it means any path after "/static/" will be passed to the send_file function as the filename parameter.
    @app.route('/static/<path:filename>')  
    def send_file(filename):
        # Call send_from_directory to send a file from the static directory.
        # The first argument to send_from_directory is the directory from which to send the file, and the second argument is the filename of the file to send.
        # app.static_folder is the path to the static directory of your Flask application.
        # So this function sends the requested file from the static directory of your application.
        return send_from_directory(app.static_folder, filename)

    # After setting up the Flask application, the create_app function returns the configured application to the caller.
    return app