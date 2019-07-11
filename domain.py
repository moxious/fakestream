import json
import numpy
import math
import uuid
import random
import datetime

from faker import Faker
from faker.providers import BaseProvider

class Domain:
    A = 5.
    DEFAULT = 1000
    BANKS = 200
    PRODUCTS = 1000
    CUSTOMERS = 1000
    COMPANIES = 1000
    ACCOUNTS = 3000
    TRANSFERS = 1000000
    PURCHASES = 1000000
    PARTIES = 100000
    currencies = ['USD', 'USD', 'USD', 'USD', 'EUR', 'EUR', 'EUR', 'GBP', 'GBP', 'CHF', 'AUD', 'CNY', 'RUB']

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
    c = 0
    """
    A Provider for web-related test data.
    >>> from faker import Faker
    >>> from domain import FakeStreamProvider
    >>> fake = Faker()
    >>> fake.add_provider(FakeStreamProvider)
    """
    fake = Faker()
    def counter(self): 
        FakeStreamProvider.c = FakeStreamProvider.c + 1
        return FakeStreamProvider.c

    def party_id(self): return Domain.id(Domain.PARTIES)
    def bank_id(self): return Domain.id(Domain.BANKS)
    def account_id(self): return Domain.id(Domain.ACCOUNTS)
    def customer_id(self): return Domain.id(Domain.CUSTOMERS)
    def uuid(self): return str(uuid.uuid4())
    def purchase_id(self): return Domain.id(Domain.PURCHASES)
    def transfer_id(self): return Domain.id(Domain.TRANSFERS)
    def company_id(self): return Domain.id(Domain.COMPANIES)
    def product_id(self): return Domain.id(Domain.PRODUCTS)
    def common_currency(self): return random.choice(Domain.currencies)
    def currency_amount(self): return random.randint(1, 10000000)
    def now(self): return datetime.datetime.now().isoformat()
    def recent_date(self): return FakeStreamProvider.fake.date_this_year(before_today=True)
    def product_name(self): return ' '.join(list(map(lambda e: e.capitalize(), FakeStreamProvider.fake.words(nb=2, ext_word_list=None, unique=False))))
    def quantity(self): return random.randint(1, 10)