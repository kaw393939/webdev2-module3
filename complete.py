# Import necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import select
from flask_smorest import Api, Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields, validate
import json

# Initialize the SQLAlchemy extension
db = SQLAlchemy()

# Define the Resume model that represents a resume in the database
class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tagline = db.Column(db.String(100))  # Reduced max length to 100
    email = db.Column(db.String)  # Made nullable
    phone = db.Column(db.String(15))
    address = db.Column(db.String, nullable=False)
    socialLinks = db.Column(db.PickleType)  # Changed to PickleType
    objective = db.Column(db.String(500))  # Increased max length to 500
    education = db.Column(db.PickleType)  # Changed to PickleType
    experience = db.Column(db.PickleType)  # Changed to PickleType
    skills = db.Column(db.PickleType)  # Changed to PickleType

# Define the schema for serializing and deserializing Resume instances to/from HTTP requests
class ResumeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1))
    tagline = fields.String(validate=validate.Length(
        max=100))  # Updated validation
    email = fields.Email()  # Removed required=True
    phone = fields.String(validate=validate.Length(min=1, max=15))
    address = fields.String(required=True, validate=validate.Length(min=1))
    socialLinks = fields.List(fields.String(), required=True)
    objective = fields.String(validate=validate.Length(
        min=1, max=500))  # Updated validation
    # Updated to List of Strings
    education = fields.List(fields.String(), required=True)
    # Updated to List of Strings
    experience = fields.List(fields.String(), required=True)
    # Updated to List of Strings
    skills = fields.List(fields.String(), required=True)

# Create a Blueprint for the resumes API
blp = Blueprint(
    'resumes', 'resumes', url_prefix='/resumes',
    description='This blueprint allows operations on the resumes of users. It supports basic CRUD operations.'
)

# Define the Resumes resource at the root URL '/'
@blp.route('/')
class Resumes(MethodView):

    # The GET method retrieves all resumes from the database
    @blp.response(200, ResumeSchema(many=True))
    def get(self):
        """Retrieve all resumes from the database"""
        resumes = db.session.execute(select(Resume)).scalars().all()
        return resumes

    # The POST method creates a new resume in the database
    @blp.arguments(ResumeSchema)
    @blp.response(201, ResumeSchema)
    def post(self, new_item):
        """Create a new resume entry in the database"""
        item = Resume(**new_item)
        db.session.add(item)
        db.session.commit()
        return item

# Define the Resumes resource with a specific ID
@blp.route('/<int:item_id>')
class ResumesById(MethodView):

    # The GET method retrieves a specific resume from the database by its ID
    @blp.response(200, ResumeSchema)
    def get(self, item_id):
        """Retrieve a specific resume by ID from the database"""
        item = db.get_or_404(Resume, item_id)
        return item

    # The PUT method updates a specific resume in the database by its ID
    @blp.arguments(ResumeSchema)
    @blp.response(200, ResumeSchema)
    def put(self, update_data, item_id):
        """Update existing resume"""
        item = db.get_or_404(Resume, item_id)
        for key, value in update_data.items():
            setattr(item, key, value)
        db.session.commit()
        return item

    # The DELETE method deletes a specific resume from the database by its ID
    @blp.response(204)
    def delete(self, item_id):
        """Delete a specific resume"""
        item = db.get_or_404(Resume, item_id)
        db.session.delete(item)
        db.session.commit()

# Factory function to create the Flask application
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["API_TITLE"] = "Resume Manager"
    app.config["API_VERSION"] = "v.1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config['OPENAPI_JSON_PATH'] = 'api-spec.json'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_REDOC_PATH'] = '/redoc'
    app.config['OPENAPI_REDOC_VERSION'] = 'next'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
    app.config['OPENAPI_SWAGGER_UI_VERSION'] = '3.23.11'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.23.11/'
    db.init_app(app)
    api = Api(app)
    api.register_blueprint(blp)

    # Create all database tables
    with app.app_context():
        db.create_all()

    return app

# Run the application if this script is run directly
if __name__ == "__main__":
    create_app().run(debug=True)
