from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum('admin', 'professional', 'customer'), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(100), nullable=True)
    pincode = db.Column(db.String(20), nullable=True)
    
    service_type = db.Column(db.String(100), nullable=True)
    experience = db.Column(db.Integer, nullable=True)
    is_verified = db.Column(db.Boolean, default=False)
    is_blocked = db.Column(db.Boolean, default=False)



class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)  
    base_price = db.Column(db.Float, nullable=False)  
    time_required = db.Column(db.Integer, nullable=False) 
    description = db.Column(db.Text, nullable=True) 



class ServiceRequest(db.Model):
    __tablename__ = 'service_requests'
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False) 
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  
    professional_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)  
    date_of_request = db.Column(db.DateTime, default=db.func.current_timestamp()) 
    date_of_completion = db.Column(db.DateTime, nullable=True) 
    service_status = db.Column(db.Enum('requested', 'assigned', 'closed'), nullable=False) 
    remarks = db.Column(db.Text, nullable=True) 
    service = db.relationship('Service', backref=db.backref('requests', lazy=True))
    customer = db.relationship('User', foreign_keys=[customer_id], backref='service_requests')
    professional = db.relationship('User', foreign_keys=[professional_id], backref='assigned_requests')



class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_requests.id'), nullable=False)  
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  
    rating = db.Column(db.Integer, nullable=False) 
    comments = db.Column(db.Text, nullable=True)  
    
    service_request = db.relationship('ServiceRequest', backref=db.backref('reviews', lazy=True))
    customer = db.relationship('User', backref='reviews')
