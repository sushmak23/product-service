from flask import jsonify, request
from service import app, db
from service.models import Product

@app.route("/api/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    """Endpoint to read a product by its ID"""
    product = Product.query.get(product_id)
    if product:
        return jsonify(product.serialize()), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """Endpoint to update a product by its ID"""
    product = Product.query.get(product_id)
    
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Get data from request
    data = request.get_json()

    # Update product details
    product.name = data.get("name", product.name)
    product.category = data.get("category", product.category)
    product.price = data.get("price", product.price)
    product.available = data.get("available", product.available)

    # Commit changes to the database
    db.session.commit()

    return jsonify(product.serialize()), 200

@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Endpoint to delete a product by its ID"""
    product = Product.query.get(product_id)
    
    if not product:
        return jsonify({"error": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted successfully"}), 200

@app.route("/api/products", methods=["GET"])
def list_all_products():
    """Endpoint to list all products"""
    products = Product.query.all()
    return jsonify([product.serialize() for product in products]), 200

@app.route("/api/products/name/<string:name>", methods=["GET"])
def list_products_by_name(name):
    """Endpoint to list products by name"""
    products = Product.query.filter(Product.name.ilike(f"%{name}%")).all()
    return jsonify([product.serialize() for product in products]), 200

@app.route("/api/products/category/<string:category>", methods=["GET"])
def list_products_by_category(category):
    """Endpoint to list products by category"""
    products = Product.query.filter(Product.category.ilike(f"%{category}%")).all()
    return jsonify([product.serialize() for product in products]), 200

@app.route("/api/products/availability/<bool:available>", methods=["GET"])
def list_products_by_availability(available):
    """Endpoint to list products by availability"""
    products = Product.query.filter_by(available=available).all()
    return jsonify([product.serialize() for product in products]), 200
