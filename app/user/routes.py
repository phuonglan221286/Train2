from flask import render_template
from . import user_bp

# Route danh sách người dùng
@user_bp.route('/')
def list_users():
    users = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
        {'id': 2, 'name': 'Jane Doe', 'email': 'jane@example.com'}
    ]
    return render_template('user/list.html', users=users)
@user_bp.route('/<int:user_id>')
def user_detail(user_id):
    user = {'id': user_id, 'name': f'User {user_id}', 'email': f'user{user_id}@example.com'}
    return render_template('user/detail.html', user=user)