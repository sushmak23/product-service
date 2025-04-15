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
