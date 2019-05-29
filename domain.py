import json
import numpy
import math

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
