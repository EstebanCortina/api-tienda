from flask import Flask
from routes import hello_bp, products_bp, categories_bp
app = Flask(__name__)

app.register_blueprint(hello_bp)
app.register_blueprint(products_bp)
app.register_blueprint(categories_bp)

if __name__ == '__main__':
    app.run()
