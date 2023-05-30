# Import the create_app function from the application package.
# This function is responsible for creating a new Flask application.
from application import create_app

# Call the create_app function to create a new instance of a Flask application.
# The create_app function sets up your Flask application and returns it so it can be used to run your server.
app = create_app()

# Check if this script is being run directly by Python (as opposed to being imported by another script).
# __name__ is a special variable in Python that gets set to "__main__" when the script is run directly.
# This is usually used to ensure that certain parts of code are only run when the script is run directly, and not when it is imported as a module.
if __name__ == "__main__":
    # If the script is being run directly, start the Flask development server.
    # The app.run() function runs the Flask development server locally on your machine.
    # The server will run in debug mode because debug=True. In debug mode, the server will automatically reload if it detects any changes in your code, and it will provide detailed error messages in your web browser if anything goes wrong.
    app.run(debug=True)
