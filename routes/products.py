from flask import request, jsonify
from routes import products_bp
from config.db_config import get_connection


@products_bp.route('/products', methods=['GET'])
def get_products():
    mysqlConn = get_connection()
    cursor = mysqlConn.cursor()
    cursor.execute('SELECT * FROM products')
    categories = cursor.fetchall()
    cursor.close()
    mysqlConn.close()
    return categories


@products_bp.route('/products/<int:id>', methods=['POST'])
def post_product(id):
    if (request.is_json):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        category_id = data.get('category_id')
        created_by = id
        mysqlConn = get_connection()
        cursor = mysqlConn.cursor()
        query = f'''
        INSERT INTO products(
          name, description,
          category_id, 
          created_at, created_by) 
          VALUES('{name}','{description}',
          {category_id},
          NOW(),{created_by})
        '''
        try:
            cursor.execute(query)
            mysqlConn.commit()
            return jsonify({'message': 'producto insertado'}), 200
        except Exception as e:
            print(e)
            mysqlConn.rollback()
            return jsonify({'message': 'Error categoria no insertada'+e}), 400
        finally:
            cursor.close()
            mysqlConn.close()
    else:
        name = request.form.get('name')
        description = request.form.get('description')
        category_id = request.form.get('category_id')
        created_by = id
        mysqlConn = get_connection()
        cursor = mysqlConn.cursor()
        query = f'''
        INSERT INTO products(
          name, description,
          category_id, 
          created_at, created_by) 
          VALUES('{name}','{description}',
          {category_id},
          NOW(),{created_by})
        '''
        try:
            cursor.execute(query)
            mysqlConn.commit()
            return jsonify({'message': 'Producto insertada'}), 200
        except Exception as e:
            print(e)
            mysqlConn.rollback()
            return jsonify({'message': 'Error categoria no insertada'+e}), 400
        finally:
            cursor.close()
            mysqlConn.close()
