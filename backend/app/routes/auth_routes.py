from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user import User  # Adjust the import based on your project structure
from models.user import db  # Adjust the import based on your project structure
from werkzeug.security import generate_password_hash
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.password_hash == password:  # Replace with hashed password check
        access_token = create_access_token(identity={'id': user.id, 'role': user.role})
        
        if user.role == 'admin':
            return jsonify(access_token=access_token), 200
        elif user.role == 'professional':
            return jsonify(access_token=access_token, redirect_url='/professional/dashboard'), 200
        elif user.role == 'customer':
            return jsonify(access_token=access_token, redirect_url='/user/dashboard'), 200

    return jsonify({"msg": "Bad username or password"}), 401





@auth_bp.route('/create_user_account', methods=['POST'])
def create_user_account():
    data = request.json
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    password_hash = generate_password_hash(password)
    address = data.get('address')
    pincode = data.get('pincode')
    phone = data.get('phone')
    
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "Username already exists"}), 400

    # Check for existing email
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        return jsonify({"message": "Email already exists"}), 400

    # Check for existing phone number
    existing_phone = User.query.filter_by(phone=phone).first()
    if existing_phone:
        return jsonify({"message": "Phone number already exists"}), 400
    user = User.query.filter_by(username=username).first()
    
    new_request = User(
    username=username,
    password_hash =  password_hash,
    email = email,
    address = address,
    pincode = pincode,
    phone = phone,
    role = 'customer'
    
    )
    try:
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message' : 'registered successfully'}),201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500
