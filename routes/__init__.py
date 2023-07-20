from flask import Blueprint

hello_bp = Blueprint('hello', __name__)
products_bp = Blueprint('products', __name__)
categories_bp = Blueprint('categories', __name__)

from .hello import *
from .products import *
from .categories import *

