from routes import products_bp
from config.db_config import get_connection


@products_bp.route('/products', methods=['GET'])
def get_users():
    mysqlConn = get_connection()
    users = [
        {'id': 1, 'name': 'Usuario 1'},
        {'id': 2, 'name': 'Usuario 2'},
        {'id': 3, 'name': 'Usuario 3'}
    ]
    return users
