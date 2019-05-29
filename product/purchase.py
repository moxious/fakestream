from faker import Faker
import random
import json
from streamentry import StreamEntry
import datetime
from domain import Domain

fake = Faker()

class Purchase(StreamEntry):
    def __init__(self, id, customer_id, product_id, company_id, date, quantity):
        StreamEntry.__init__(self)
        self.id = id
        self.customer_id = customer_id
        self.product_id = product_id
        self.company_id = company_id
        self.date = date
        self.quantity = quantity
        self.type = 'purchase'

    @staticmethod
    def create():
        id = random.randint(1, Domain.PURCHASES)
        customer_id = random.randint(1, Domain.CUSTOMERS)
        product_id = random.randint(1, Domain.PRODUCTS)
        company_id = random.randint(1, Domain.COMPANIES)
        date = datetime.datetime.now().isoformat()
        quantity = random.randint(1, 10)

        return Purchase(id, customer_id, product_id, company_id, date, quantity)
