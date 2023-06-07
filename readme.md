# Assignment: Building and Testing a Resume API

In this assignment, you will work on a Flask application that serves as a Resume API. You'll be responsible for both implementing the API to pass the automated Pytest.  I have removed the code from [application/__init__py and put a copy for reference here](backup_app.py)

From a code poinit of view this unit is easy and it is just to introduce you to the concepts and basic termiinology used to make REST API.  I'm giving you the code for the assignment because you really need to understand it and we will be building on this to make it a more complete API.  Currently, the data is just stored in the application instance and not a database.  There are a lot of features we need to add to make this a complete professional standards compliant API, but you will get lost when we do this, if you don't understand the basics.  In later units, i'm going to show you some libraries that automate some things for you; however, you need to completely understand the code we have now and the concepts in the presentation.

- Instructor Video - [here]()

## Learning Objectives

By the end of this project, you should be able to:

1. **Build and Run a RESTful API**: Use Flask, a lightweight web framework for Python, to construct a RESTful API.
2. **Work with JSON**: Understand how JSON is used as a data interchange format in web development, and use it to structure the data in your API.
3. **Apply HTTP Methods**: Implement CRUD (Create, Read, Update, Delete) operations using appropriate HTTP methods.
4. **Understand HTTP Response Codes**: Use appropriate HTTP status codes to indicate the success or failure of a request.
5. **Write Code and Pass Tests**: Code your App  to Pass the Tests

    ```shell
    flask run
    ```

## Project Steps

### Step 1: Understanding Your Resume

1. Navigate to `data/` and open `resume.json`.
2. This file contains a sample resume. Take a moment to understand the structure and contents of this JSON file. If you wish, you can replace the sample resume with your own. Be careful to maintain the correct JSON format.

### Step 2: Implementing the API

* *Your task is to implement a RESTful API based on the structure of the resume. Your API should have routes corresponding to the main sections of the resume: basics, work, volunteer, education, awards, publications, skills, languages, interests, and references. Each route should support the four main HTTP methods: GET, POST, PUT, DELETE and return appropriate status codes.

### Step 3: Testing the API

* Write tests for your API using Pytest. You should write tests for each of the routes and HTTP methods that you've implemented. Make sure to test for both expected and unexpected inputs, checking that your API behaves appropriately in each case.  You should also install the REST Client in VsCode and run the API using this [file](requests.http).  This file has the requests and you can see your API responses, its helpful for testing and development to undertand this.  You can see this immedietly by just copying the code I am giving you and runinig the server.

## Submission Guidelines

- Push your changes to GitHub and submit the link to your repository to Canvas. Make sure that your repository is set to public so that we can access your work.


## Project Setup

### Step 0: Setup the Application

1. **Clone the repository**: After accepting the assignment, clone the repository to your local machine. Use the following command:

    ```shell
    git clone <repository-url>
    ```

2. **Navigate into the cloned directory**: Use the `cd` command to navigate into the directory of the cloned repository:

    ```shell
    cd <repository-name>
    ```

3. **Create a virtual environment**: Use `python3 -m venv venv` to create a virtual environment in the project directory:

    ```shell
    python3 -m venv venv
    ```

4. **Activate the virtual environment**: Use `source venv/bin/activate` (Unix/macOS) or `venv\Scripts\activate` (Windows):

    ```shell
    source venv/bin/activate
    ```

5. **Install necessary packages**: Use `pip install -r requirements.txt` to install the necessary packages:

    ```shell
    pip install -r requirements.txt
    ```

6. **Run the application**: Use `flask run` to start the application and then visit `http://127.0.0.1:5000/` on your browser: