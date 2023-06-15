# Assignment: Enhancing and Testing a Resume API

In this assignment, you will be enhancing a Flask application that serves as a Resume API. This assignment aims to introduce you to the professional Git workflow, the concept of Object Relational Mapping (ORM), and data validation, all of which are critical in professional software development. You will be utilizing SQLAlchemy, a popular ORM for Python, and will be introduced to how an ORM allows you to interact with your database like you would with SQL.

You will be given an existing codebase, and your task is to extend it by adding new fields, updating existing ones, and ensuring the OpenAPI documentation is up to date. The data model of the API is a resume, which has fields like name, title, skills, etc. 

This project uses Flask-Smorest, which integrates Flask, Marshmallow, and Open Api apispec to help you build a robust RESTful API with minimal effort. Marshmallow is used for data validation and serialization/deserialization, and we will use an in-memory SQL database for quick and reliable testing. 

You will be implementing and refining BREAD operations (Browse, Read, Edit, Add, and Delete) for the resume data and making Git commits throughout the process, which will highlight your understanding and application of good version control practices. 

## Learning Objectives

By the end of this project, you should be able to:

1. **Understand and Apply Professional Git Workflow**: Understand and apply Git commands like push, pull, merge, and commit with meaningful messages. You will be practicing collaboration on an existing codebase.

2. **Understand and Use an ORM**: Understand the concept of ORM and apply it in web development using SQLAlchemy. You will learn how SQLAlchemy interacts with Flask to manage an SQL database.

3. **Understand and Apply Data Validation**: Understand the concept of data validation and apply it using Marshmallow. Data validation ensures the integrity of the data before it's processed by the API.

4. **Extend and Refine a RESTful API**: You will be given a basic Flask API, and your task will be to extend and refine it according to the requirements and tests provided.

5. **Generate and Update OpenAPI Specifications**: Use Flask-smorest to automatically generate OpenAPI specifications for your API, and ensure they are kept up-to-date as you modify the API.

## Learning Materials

**Instructor Video** - [here](https://youtu.be/IiJ4p4ksqZU)

### Required Additionl Videos
- Real-world Examples in Git Command Line Cheat Sheet - [here](git.md)
- VSCode and Commits - [here](https://www.youtube.com/watch?v=E6ADS2k8oNQ)
- VSCode and Branches - [here](https://www.youtube.com/watch?v=b9LTz6joMf8)
- VSCode and Pull Requests - [here](https://www.youtube.com/watch?v=LdSwWxVzUpo)
- Collaborative Git Command-line between Two Students - [here](https://www.youtube.com/watch?v=_wQdY_5Tb5Q)

### Websites
- In-depth Git Tutorial - [here](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud) - Ensure you go through all sections for a complete understanding of collaboration.
- GitHub Flow - [here](https://docs.github.com/en/get-started/quickstart/github-flow)

## Assignment Instructions

Your task for this assignment is to modify the existing codebase to ensure it passes our grading tests. To start, clone the repository to your local machine and create a new branch. Spend some time reviewing the existing codebase and the [reference code](complete.py) I have provided. 

Familiarize yourself with our grading [tests](tests/test_app.py). This will provide clarity on how to test the API and the types of tests you will make in the future.

For each pull request(PR) I have included a name for the branch that you should use and an action section that has the commit message and what you need to do.

## Assignment Steps

1. **Initial Setup:** Start by accepting the assignment on GitHub Classroom to create your repository. Clone this repository to your local machine, and initiate your changes in a new branch.
2. **Making Changes:** Modify the resume to meet the requirements of one of the pull requests listed below.
3. **Committing Changes and Push:** Once you've confirmed the changes via testing, commit them with clear and descriptive commit messages and push them to GitHub
4. **Creating Pull Requests:** After committing your changes, push your branch to the remote repository and create a new pull request via the GitHub page of your repository.
5. **Review and Merge:** Normally, your teammates would review your changes and give feedback. For this assignment, you'll be self-reviewing and merging the pull request after providing comments.
6. **Iteration:** After successfully merging your pull request, switch to the `master` branch and pull the latest updates. For additional modifications, create a new branch and repeat the process.


## Pull Requests

1. **PR #1: Update String Length Limits in DB Model and Schema**
   - Branch Name: `update-string-length-limits`
   - Action: Update `tagline` field in `Resume` model to have a max length of 100.
     - Commit Message: "Refactor: Updated max length of `tagline` field in `Resume` model to 100"
   - Action: Update `tagline` field in `ResumeSchema` to validate a max length of 100.
     - Commit Message: "Refactor: Enforced max length validation of 100 for `tagline` in `ResumeSchema`"
   - Action: Add max length of 500 to `objective` field in `Resume` model.
     - Commit Message: "Feature: Added max length of 500 to `objective` field in `Resume` model"
   - Action: Update `objective` field in `ResumeSchema` to validate max length of 500.
     - Commit Message: "Feature: Updated `objective` field in `ResumeSchema` to validate max length of 500"

2. **PR #2: Adjust Email Field Nullability**
   - Branch Name: `adjust-email-nullability`
   - Action: Make `email` field in `Resume` model nullable.
     - Commit Message: "Refactor: Made `email` field in `Resume` model nullable"
   - Action: Remove required validation for `email` field in `ResumeSchema`.
     - Commit Message: "Refactor: Removed required validation for `email` field in `ResumeSchema`"

3. **PR #3: Migrate SocialLinks, Education, Experience, Skills to PickleType and List Fields**
   - Branch Name: `migrate-fields-to-pickletype-and-list`
   - Action: Change `socialLinks`, `education`, `experience`, and `skills` fields in `Resume` model to `PickleType`.
     - Commit Message: "Refactor: Migrated `socialLinks`, `education`, `experience`, and `skills` to `PickleType` in `Resume` model"
   - Action: Change `socialLinks`, `education`, `experience`, and `skills` fields in `ResumeSchema` to `List(fields.String())` and make them required.
     - Commit Message: "Refactor: Updated `socialLinks`, `education`, `experience`, and `skills` fields in `ResumeSchema` to `List(fields.String())` and made them required"

4. **PR #4: Update Blueprint Description**
   - Branch Name: `update-blueprint-description`
   - Action: Update the description of the blueprint from 'Operations on resumes' to 'This blueprint allows operations on the resumes of users. It supports basic CRUD operations.'
     - Commit Message: "Docs: Updated blueprint description for clarity and detail"

5. **PR #5: Update GET Method for All Resumes**
   - Branch Name: `update-get-method-all-resumes`
   - Action: Replace `Resume.query.all()` with `db.session.execute(select(Resume)).scalars().all()` in the `get` method of the `Resumes` class to improve SQL query execution.
     - Commit Message: "Refactor: Optimized SQL query execution in `get` method of `Resumes` class"
   - Action: Update the method comment to reflect this change: from "List all resumes" to "Retrieve all resumes from the database".
     - Commit Message: "Docs: Updated method comment in `get` method of `Resumes` class for accuracy"

6. **PR #6: Update POST Method for All Resumes**
   - Branch Name: `update-post-method-all-resumes`
   - Action: Update the method comment to reflect this change: from "Add a new resume" to "Create a new resume entry in the database".
     - Commit Message: "Docs: Updated method comment in `post` method for `Resumes` for accuracy"

7. **PR #7: Update ALL the GET Methods for Resumes By ID**
   - Branch Name: `update-all-get-method-resumes-by-id`
   - Action: Replace `Resume.query.get_or_404(item_id)` with `db.get_or_404(Resume, item_id)` in the `get` method of the `ResumesById` class to handle not found exceptions.
     - Commit Message: "Refactor: Updated `get` method in `ResumesById` class to handle not found exceptions"
   - Action: Update the method comment to reflect this change: from "Get resume by ID" to "Retrieve a specific resume by ID from the database".
     - Commit Message: "Docs: Updated method comment in `get` method for `ResumesById` class for accuracy"

8. **PR #8: Update PUT Method for Resumes By ID**
   - Branch Name: `update-put-method-resumes-by-id`
   - Action: Change the name of the first parameter from `new_item` to `update_data` in the `put` method of the `ResumesById` class.
     - Commit Message: "Refactor: Renamed first parameter in `put` method for `ResumesById` class for clarity"
   - Action: Update the method comment to "Update existing resume".
     - Commit Message: "Docs: Updated method comment in `put` method for `ResumesById` class for accuracy"

9. **PR #9: Update API_TITLE**
   - Branch Name: `update-api-title`
   - Action: Change the value of `app.config["API_TITLE"]` from "Your API" to "Resume Manager".
     - Commit Message: "Refactor: Updated `API_TITLE` to `Resume Manager` for relevancy"

10. **PR #10: Update API_VERSION**
   - Branch Name: `update-api-version`
   - Action: Change the value of `app.config["API_VERSION"]` from "v1" to "v.1".
     - Commit Message: "Refactor: Updated `API_VERSION` to `v.1` for consistency"

## Submission Guidelines - MUST FOLLOW OR YOU GET A 0 WITH NO RESUBMIT

- Remove the content in the current readme.md file and replace it with a screenshot of your commit history on GIThub - [see example](commit-history.png)

- Push your changes to GitHub and submit the link to your repository to Canvas when you get all green for github Actions. 

- Make sure all your tests pass

- Make sure you at have all the commits required and no more.

## Grading

This assignment will be graded based on:

1. The functionality of your API: Does it perform all the required operations correctly?

2. Your use of Git: Did you make regular commits with meaningful messages? Did you successfully merge your branch

Remember, the main goal of this assignment is to understand and apply the concepts of Git collaboration, ORM, and data validation. Don't worry if you don't get everything perfect on the first try. The important thing is to learn and improve as you go.

Good luck

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

    ```shell
    flask run
    ```