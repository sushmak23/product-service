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

