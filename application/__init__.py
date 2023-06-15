from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api, Blueprint, Page
from flask.views import MethodView
from marshmallow import Schema, fields, validate, post_dump

db = SQLAlchemy()

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tagline = db.Column(db.String(200))
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(15))
    address = db.Column(db.String, nullable=False)
    socialLinks = db.Column(db.String)
    objective = db.Column(db.String)
    education = db.Column(db.String)
    experience = db.Column(db.String)
    skills = db.Column(db.String)

class ResumeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1))
    tagline = fields.String(validate=validate.Length(max=200))
    email = fields.Email(required=True)
    phone = fields.String(validate=validate.Length(min=1, max=15))
    address = fields.String(required=True, validate=validate.Length(min=1))
    socialLinks = fields.String(validate=validate.Length(min=1))
    objective = fields.String(validate=validate.Length(min=1))
    education = fields.String(validate=validate.Length(min=1))
    experience = fields.String(validate=validate.Length(min=1))
    skills = fields.String(validate=validate.Length(min=1))

blp = Blueprint(
    'resumes', 'resumes', url_prefix='/resumes',
    description='Operations on resumes'
)

@blp.route('/')
class Resumes(MethodView):

    @blp.response(200, ResumeSchema(many=True))
    
    def get(self):
        """List all resumes"""
        return Resume.query.all()
    
    @blp.arguments(ResumeSchema)
    @blp.response(201, ResumeSchema)
    def post(self, new_item):
        """Add a new resume"""
        item = Resume(**new_item)
        db.session.add(item)
        db.session.commit()
        return item

@blp.route('/<int:item_id>')
class ResumesById(MethodView):

    @blp.response(200, ResumeSchema)
    def get(self, item_id):
        """Get resume by ID"""
        return Resume.query.get_or_404(item_id)

    @blp.arguments(ResumeSchema)
    @blp.response(200, ResumeSchema)
    def put(self, new_item, item_id):
        """Replace resume by ID"""
        item = Resume.query.get_or_404(item_id)
        for key, value in new_item.items():
            setattr(item, key, value)
        db.session.commit()
        return item

    @blp.response(204)
    def delete(self, item_id):
        """Delete resume by ID"""
        item = Resume.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["API_TITLE"] = "Your API"
    app.config["API_VERSION"] = "v1"
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
    
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
