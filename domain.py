import json
import numpy
import math
import uuid

from faker import Faker
from faker.providers import BaseProvider

class Domain:
    A = 5.
    DEFAULT = 1000
    BANKS = 1000
    PRODUCTS = 1000
    CUSTOMERS = 1000
    COMPANIES = 1000
    ACCOUNTS = 1000
    TRANSFERS = 1000
    PURCHASES = 1000000

    @staticmethod
    def faker():
        fake = Faker()
        fake.add_provider(FakeStreamProvider)
        return fake

    """Generates a power law distribution of IDs in a given range"""
    @staticmethod
    def id(range=DEFAULT):
        return math.floor(numpy.random.power(Domain.A) * range)

    def __init__(self, f="domain.json"):
        if not f:
            f = "domain.json"

        with open(f) as file:
            data = json.load(file)
        self.spec = data

    def __str__(self):
        return json.dumps(self.spec, indent=3)

class FakeStreamProvider(BaseProvider):
    """
    A Provider for web-related test data.
    >>> from faker import Faker
    >>> from domain import FakeStreamProvider
    >>> fake = Faker()
    >>> fake.add_provider(FakeStreamProvider)
    """
    def bank_id(self): return Domain.id(Domain.BANKS)
    def account_id(self): return Domain.id(Domain.ACCOUNTS)
    def customer_id(self): return Domain.id(Domain.CUSTOMERS)
    def uuid(self): return str(uuid.uuid4())
    def purchase_id(self): return Domain.id(Domain.PURCHASES)
    def transfer_id(self): return Domain.id(Domain.TRANSFERS)
    def company_id(self): return Domain.id(Domain.COMPANIES)
    def product_id(self): return Domain.id(Domain.PRODUCTS)

