import factory
from service.models import Product

class ProductFactory(factory.Factory):
    """Factory for creating fake Products"""
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    category = factory.Faker("word")
    available = factory.Faker("boolean")
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
