from flask import request, jsonify
from routes import categories_bp
from config.db_config import get_connection


@categories_bp.route('/categories', methods=['GET'])
def get_categories():
    mysqlConn = get_connection()
    cursor = mysqlConn.cursor()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    cursor.close()
    mysqlConn.close()
    return categories


@categories_bp.route('/categories/<int:id>', methods=['POST'])
def post_categories(id):
    if (request.is_json):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        created_by = id
        mysqlConn = get_connection()
        cursor = mysqlConn.cursor()
        query = f'''
        INSERT INTO categories(
          name, description, 
          created_at, created_by) 
          VALUES('{name}','{description}',
          NOW(),{created_by})
        '''
        try:
            cursor.execute(query)
            mysqlConn.commit()
            return jsonify({'message': 'categoria insertada'}), 200
        except Exception as e:
            print(e)
            mysqlConn.rollback()
            return jsonify({'message': 'Error categoria no insertada'}), 400
        finally:
            cursor.close()
            mysqlConn.close()
    else:
        name = request.form.get('name')
        description = request.form.get('description')
        created_by = id
        mysqlConn = get_connection()
        cursor = mysqlConn.cursor()
        query = f'''
        INSERT INTO categories(
          name, description, 
          created_at, created_by) 
          VALUES('{name}','{description}',
          NOW(),{created_by})
        '''
        try:
            cursor.execute(query)
            mysqlConn.commit()
            return jsonify({'message': 'categoria insertada'}), 200
        except Exception as e:
            print(e)
            mysqlConn.rollback()
            return jsonify({'message': 'Error categoria no insertada'}), 400
        finally:
            cursor.close()
            mysqlConn.close()


@categories_bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_categories(id):
    mysqlConn = get_connection()
    cursor = mysqlConn.cursor()
    query = f'''
    DELETE FROM categories WHERE id={id}
    '''
    try:
        cursor.execute(query)
        mysqlConn.commit()
        return jsonify({'message': f'categoria {id} eliminada'}), 200
    except Exception as e:
        print(e)
        mysqlConn.rollback()
        return jsonify({'message': 'Error categoria no eliminada'}), 400
    finally:
        cursor.close()
        mysqlConn.close()


@categories_bp.route('/categories/<int:id>', methods=['PUT'])
def put_categories(id):
    if (request.is_json):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        mysqlConn = get_connection()
        cursor = mysqlConn.cursor()
        query = f'''
        UPDATE SET 
          name = '{name}', 
          description = '{description}'
          WHERE id = '{id}'          
        '''
        try:
            cursor.execute(query)
            mysqlConn.commit()
            return jsonify({'message': 'categoria insertada'}), 200
        except Exception as e:
            print(e)
            mysqlConn.rollback()
            return jsonify({'message': 'Error categoria no insertada'}), 400
        finally:
            cursor.close()
            mysqlConn.close()
    else:
        name = request.form.get('name')
        description = request.form.get('description')
        mysqlConn = get_connection()
        cursor = mysqlConn.cursor()
        query = f'''
        UPDATE categories
        SET 
          name = '{name}', 
          description = '{description}'
          WHERE id = '{id}'          
        '''
        try:
            cursor.execute(query)
            mysqlConn.commit()
            return jsonify({'message': 'categoria actualizada'}), 200
        except Exception as e:
            print(e)
            mysqlConn.rollback()
            return jsonify({'message': 'Error categoria no actualizada'}), 400
        finally:
            cursor.close()
            mysqlConn.close()
