from routes import hello_bp

@hello_bp.route('/hello', methods=['GET'])
def hello():
    return 'Hello, world!'
