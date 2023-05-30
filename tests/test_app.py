# tests/test_app.py
import pytest
import json

from application import create_app

# Fixture to set up the Flask app for testing
@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

# Fixture to create a test client - an instance of the Flask app that we can use to make requests
@pytest.fixture
def client(app):
    return app.test_client()

# A test to make sure the '/' route returns the correct response
def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!', 'The root route does not return the expected response.'

# A test to check that the '/static/data.json' route returns a JSON object with the correct keys
def test_json_response(client):
    # Get the JSON data
    response = client.get('/static/resume.json')

    # Parse the JSON data
    data = json.loads(response.data)

    # Define the keys that we expect to find in the JSON data
    expected_keys = ["name", "tagline", "email", "phone", "address", "socialLinks", "objective", "education", "experience", "skills"]
    expected_social_links_keys = ["linkedin", "twitter", "github"]
    expected_education_keys = ["degree", "institution", "years"]
    expected_experience_keys = ["jobTitle", "company", "years"]

    # Assert that the response data is a dictionary
    assert isinstance(data, dict), 'The JSON response is not a dictionary.'

    # Assert that all expected keys are present in the root of the JSON data
    assert all(key in data for key in expected_keys), 'Some expected keys are missing from the JSON response.'

    # Assert that all expected keys are present in the "socialLinks" dictionary of the JSON data
    assert all(key in data["socialLinks"] for key in expected_social_links_keys), 'Some expected keys are missing from the "socialLinks" dictionary in the JSON response.'

    # Assert that all expected keys are present in each dictionary in the "education" list of the JSON data
    assert all(all(key in item for key in expected_education_keys) for item in data["education"]), 'Some expected keys are missing from the dictionaries in the "education" list in the JSON response.'

    # Assert that all expected keys are present in each dictionary in the "experience" list of the JSON data
    assert all(all(key in item for key in expected_experience_keys) for item in data["experience"]), 'Some expected keys are missing from the dictionaries in the "experience" list in the JSON response.'
