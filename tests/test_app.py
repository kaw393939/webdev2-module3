# tests/test_app.py
import pytest
import json
import os

from application import create_app, db

# A pytest fixture that sets up an application instance for testing
# It is scoped at the module level, so it is created once per test module
# The application is configured for testing and uses an in-memory SQLite database
# The database is created before and dropped after the tests are run
@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()

# A pytest fixture that sets up a client to make requests to the application
# It is scoped at the function level, so it is created for each test function
# The client allows you to make HTTP requests and exposes other methods for testing
@pytest.fixture(scope='function')
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client

# A pytest fixture that returns a dictionary with data for a resume
# This can be used as input for POST requests to create a resume
@pytest.fixture(scope='function')
def resume_data():
    return {
      "name": "John Doe",
      "tagline": "Software Engineer",
      "email": "john.doe@example.com",
      "phone": "1234567890",
      "address": "123 Main Street, Anytown, USA",
      "socialLinks": [
        "https://github.com/johndoe",
        "https://linkedin.com/in/johndoe"
      ],
      "objective": "Looking for a challenging role...",
      "education": [
        "B.S. in Computer Science from XYZ University",
        "High School Diploma from ABC High School"
      ],
      "experience": [
        "Software Engineer at Tech Corp from 2020 to Present",
        "Intern at Startup Inc from 2019 to 2020"
      ],
      "skills": [
        "Python",
        "Java",
        "C++",
        "Machine Learning",
        "Web Development"
      ]
    }

# Test that an empty database returns an empty list when GET /resumes/ is requested
def test_get_resumes_empty_db(client):
    response = client.get('/resumes/')
    assert response.status_code == 200
    assert response.get_json() == []

# Test that a POST request to /resumes/ creates a resume
def test_post_resume(client, resume_data):
    response = client.post('/resumes/', json=resume_data)
    assert response.status_code == 201
    assert 'id' in response.get_json()

# Test that a POST request to /resumes/ with invalid data returns a 422 status
def test_post_resume_invalid_data(client):
    invalid_data = {"invalid_key": "invalid_value"}
    response = client.post('/resumes/', json=invalid_data)
    assert response.status_code == 422  # Unprocessable Entity

# Test that a GET request to /resumes/{id} returns a resume
def test_get_resume(client, resume_data):
    response_post = client.post('/resumes/', json=resume_data)
    assert response_post.status_code == 201
    resume_id = response_post.get_json()['id']
    response = client.get(f'/resumes/{resume_id}')
    assert response.status_code == 200

# Test that a GET request to /resumes/{id} with a non-existent ID returns a 404 status
def test_get_resume_nonexistent(client):
    response = client.get('/resumes/9999/')
    assert response.status_code == 404

# Test that a PUT request to /resumes/{id} updates a resume
def test_put_resume(client, resume_data):
    response_post = client.post('/resumes/', json=resume_data)
    resume_id = response_post.get_json()['id']
    updated_resume_data = resume_data.copy()
    updated_resume_data["name"] = "Updated Name"
    response = client.put(f'/resumes/{resume_id}', json=updated_resume_data)
    assert response.status_code == 200
    assert response.get_json()['name'] == "Updated Name"

# Test that a PUT request to /resumes/{id} with a non-existent ID returns a 404 status
def test_put_resume_nonexistent(client, resume_data):
    updated_resume_data = resume_data.copy()
    updated_resume_data["name"] = "Updated Name"
    response = client.put('/resumes/9999/', json=updated_resume_data)
    assert response.status_code == 404

# Test that a DELETE request to /resumes/{id} deletes a resume
def test_delete_resume(client, resume_data):
    response_post = client.post('/resumes/', json=resume_data)
    resume_id = response_post.get_json()['id']
    response = client.delete(f'/resumes/{resume_id}')
    assert response.status_code == 204
    # Verify the resume is actually deleted
    response = client.get(f'/resumes/{resume_id}')
    assert response.status_code == 404

# Test that a DELETE request to /resumes/{id} with a non-existent ID returns a 404 status
def test_delete_resume_nonexistent(client):
    response = client.delete('/resumes/9999')
    assert response.status_code == 404
