# Welcome to the Flask Web Development Project

In this project, you'll learn and apply your skills in Python, Flask, Pytest, and JSON. We've designed a basic Flask application which serves a static JSON file. You'll be coding your own resume into this JSON file, and learn about the importance of testing in web development. 

## Getting Started

1. **Accept the GitHub Classroom assignment**: Click on the assignment link provided by your instructor. You'll be redirected to GitHub Classroom where you'll need to accept the assignment.

2. **Code your resume**: Navigate to `application/static/` and open `resume.json`. Fill in your own information in the appropriate fields in the JSON file. Ensure that you're maintaining the correct JSON format as you do this.

## How the program works

This program is a simple Flask web application. When you run the program, it starts a web server on your local machine. It's configured to serve two routes:

- The root URL ("/") returns a "Hello, World!" message.
- The "/static/resume.json" URL serves the `resume.json` file from the `static` directory. 

The `resume.json` file is where you'll be coding your resume. When you navigate to "/static/resume.json" in your web browser, you'll see your resume displayed as a JSON object.

## Installation and Setup

1. **Clone the repository**: After accepting the assignment, clone the repository to your local machine.

2. **Create a virtual environment**: Navigate to the project directory in your terminal and run the command `python3 -m venv venv` to create a virtual environment. This keeps your project's dependencies isolated from other projects.

3. **Activate the virtual environment**: Activate the virtual environment using the command `source venv/bin/activate` on Unix/macOS or `venv\Scripts\activate` on Windows.

4. **Install the requirements**: Install the necessary packages using the command `pip install -r requirements.txt`.

5. **Run the application**: Start the application with the command `flask run`. Then, navigate to `http://localhost:5000/` in your web browser to see your application running. To run the server in debug mode, which provides more detailed error messages and automatically restarts the server when it detects changes in your code, use the command `flask run --debug`.

## Testing with Pytest

Testing is a crucial part of web development. In this project, you'll be using Pytest, a testing framework for Python.

There are some predefined tests in the `tests` directory. To run these tests, simply use the command `pytest` in your terminal while you're in the project directory. 

Make sure your application is serving the `resume.json` file correctly by running the predefined tests and ensuring they all pass. If the tests fail, they will provide feedback about what's going wrong, which can guide you in debugging your application.

Remember, in the real world, a project would have many more tests and you'd typically write tests for any new features you develop.

Enjoy coding and learning!
