from flask import jsonify, render_template, request
from . import user_bp
from .models import db, User

# Route danh sách người dùng
@user_bp.route('/')
def list_users():
    # Lấy danh sách người dùng từ CSDL
    users = User.query.all()
    return render_template('user/list.html', users=users)

@user_bp.route('/<int:user_id>')
def user_detail(user_id):
    user = {'id': user_id, 'name': f'User {user_id}', 'email': f'user{user_id}@example.com'}
    return render_template('user/detail.html', user=user)
# Route để thêm người dùng
@user_bp.route('/add', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    # Kiểm tra dữ liệu
    if not name or not email:
        return jsonify({'error': 'Name and email are required!'}), 400

    # Thêm người dùng vào CSDL
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully!'})

# Route để cập nhật thông tin người dùng
@user_bp.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json  # Lấy dữ liệu từ yêu cầu JSON
    name = data.get('name')
    email = data.get('email')

    # Kiểm tra dữ liệu
    if not name or not email:
        return jsonify({'error': 'Name and email are required!'}), 400

    # Tìm người dùng trong CSDL
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found!'}), 404

    # Cập nhật thông tin người dùng
    user.name = name
    user.email = email
    db.session.commit()

    return jsonify({'message': 'User updated successfully!'})