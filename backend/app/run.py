from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from flask_jwt_extended import JWTManager

from routes.auth_routes import auth_bp  
from models.user import db  
app = Flask(__name__)
CORS(app)  
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'your_super_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///house.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  
app.register_blueprint(auth_bp, url_prefix='/auth') 
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True, host='0.0.0.0', port=5000)