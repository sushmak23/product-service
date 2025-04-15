from flask import jsonify
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
