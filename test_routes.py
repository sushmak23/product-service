import unittest
import json
from service import app, db
from service.models import Product
from tests.factories import ProductFactory

class TestProductRoutes(unittest.TestCase):
    """Test Cases for Product API Routes"""

    def setUp(self):
        """Initialize test client and sample data"""
        self.client = app.test_client()
        db.create_all()
        self.product = ProductFactory()
        db.session.add(self.product)
        db.session.commit()

    def tearDown(self):
        """Clean up"""
        db.session.remove()
        db.drop_all()

    def test_read_a_product(self):
        """Test reading a single product via GET"""
        response = self.client.get(f"/api/products/{self.product.id}")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["id"], self.product.id)
        self.assertEqual(data["name"], self.product.name)

    def test_update_a_product(self):
        """Test updating a product via PUT"""
        updated_data = {
            "name": "Updated Product Name",
            "category": "Updated Category",
            "price": 20.99
        }
        response = self.client.put(f"/api/products/{self.product.id}", json=updated_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["name"], updated_data["name"])
        self.assertEqual(data["category"], updated_data["category"])
        self.assertEqual(data["price"], updated_data["price"])

    def test_delete_a_product(self):
        """Test deleting a product via DELETE"""
        response = self.client.delete(f"/api/products/{self.product.id}")
        self.assertEqual(response.status_code, 200)
        # Check that the product is actually deleted
        response = self.client.get(f"/api/products/{self.product.id}")
        self.assertEqual(response.status_code, 404)  # Not found

    def test_list_all_products(self):
        """Test listing all products via GET"""
        ProductFactory.create_batch(3)  # Add 3 more products
        response = self.client.get("/api/products")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreaterEqual(len(data), 4)  # Should have 4 or more products

    def test_find_by_name(self):
        """Test finding a product by name via GET"""
        name = self.product.name
        response = self.client.get(f"/api/products?name={name}")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreaterEqual(len(data), 1)  # Should return at least 1 product
        self.assertEqual(data[0]["name"], name)

    def test_find_by_category(self):
        """Test finding products by category via GET"""
        category = self.product.category
        response = self.client.get(f"/api/products?category={category}")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreaterEqual(len(data), 1)  # Should return at least 1 product
        self.assertEqual(data[0]["category"], category)

    def test_find_by_availability(self):
        """Test finding products by availability via GET"""
        available = self.product.available
        response = self.client.get(f"/api/products?available={available}")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreaterEqual(len(data), 1)  # Should return at least 1 product
        self.assertEqual(data[0]["available"], available)
