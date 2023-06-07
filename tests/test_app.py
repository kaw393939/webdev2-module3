# tests/test_app.py
import pytest
import json
import os

from application import create_app

@pytest.fixture(scope='function')
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture(scope='function')
def client(app):
    with app.test_client() as client:
        with app.app_context():
            # Clear data before each test
            app.resume = {}
            yield client

@pytest.fixture(scope='function')
def resume_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, '..', 'data', 'resume.json'), 'r') as f:
        data = json.load(f)
    return data

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'

def test_post_resume(client, resume_data):
    response = client.post('/resume', data=json.dumps(resume_data), content_type='application/json')
    assert response.status_code == 201

def test_post_resume_with_invalid_data(client):
    invalid_data = {"invalid_key": "invalid_value"}
    response = client.post('/resume', data=json.dumps(invalid_data), content_type='application/json')
    assert response.status_code == 400

def test_get_resume(client, resume_data):
    client.post('/resume', data=json.dumps(resume_data), content_type='application/json')
    response = client.get('/resume')
    assert response.status_code == 200

def test_get_resume_without_post(client):
    response = client.get('/resume')
    assert response.status_code == 404

def test_put_resume(client, resume_data):
    client.post('/resume', data=json.dumps(resume_data), content_type='application/json')
    resume_data["name"] = "Updated Name"
    response = client.put('/resume', data=json.dumps(resume_data), content_type='application/json')
    assert response.status_code == 200

def test_put_resume_without_post(client, resume_data):
    resume_data["name"] = "Updated Name"
    response = client.put('/resume', data=json.dumps(resume_data), content_type='application/json')
    assert response.status_code == 404

def test_delete_resume(client, resume_data):
    client.post('/resume', data=json.dumps(resume_data), content_type='application/json')
    response = client.delete('/resume')
    assert response.status_code == 204

def test_delete_resume_without_post(client):
    response = client.delete('/resume')
    assert response.status_code == 404
