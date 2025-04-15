from behave import given
from service import db
from service.models import Product

@given('we have the following products in the database')
def step_impl(context):
    """Load product data into the database before the tests"""
    products = [
        Product(name='Product 1', category='Category A', price=10.0, available=True),
        Product(name='Product 2', category='Category B', price=15.5, available=False),
        Product(name='Product 3', category='Category A', price=22.0, available=True),
        Product(name='Product 4', category='Category C', price=30.0, available=True),
    ]
    db.session.bulk_save_objects(products)
    db.session.commit()
