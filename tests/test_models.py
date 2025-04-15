import unittest
from service.models import db, Product
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    """ Test Cases for Product Model """

    def setUp(self):
        """Initialize test database and create a sample product"""
        db.create_all()
        self.product = ProductFactory()
        db.session.add(self.product)
        db.session.commit()

    def tearDown(self):
        """Clean up after each test"""
        db.session.remove()
        db.drop_all()

    def test_create_a_product(self):
        """Test creating a product"""
        product = ProductFactory()
        self.assertIsNotNone(product)
        self.assertIsNotNone(product.id)

    def test_read_a_product(self):
        """Test reading a product from the database"""
        found = Product.find(self.product.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.id, self.product.id)

    def test_update_a_product(self):
        """Test updating a product in the database"""
        self.product.name = "Updated Name"
        self.product.update()
        updated = Product.find(self.product.id)
        self.assertEqual(updated.name, "Updated Name")

    def test_delete_a_product(self):
        """Test deleting a product from the database"""
        product_id = self.product.id
        self.product.delete()
        result = Product.find(product_id)
        self.assertIsNone(result)

    def test_list_all_products(self):
        """Test listing all products"""
        ProductFactory.create_batch(3)
        products = Product.all()
        self.assertGreaterEqual(len(products), 3)

    def test_find_by_name(self):
        """Test finding products by name"""
        name = "UniqueTestName"
        self.product.name = name
        self.product.update()
        results = Product.find_by_name(name)
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0].name, name)

    def test_find_by_category(self):
        """Test finding products by category"""
        category = "Fruit"
        self.product.category = category
        self.product.update()
        results = Product.find_by_category(category)
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0].category, category)

    def test_find_by_availability(self):
        """Test finding products by availability"""
        self.product.available = True
        self.product.update()
        results = Product.find_by_availability(True)
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(results[0].available)

